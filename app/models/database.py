"""Database models for FraudNet.AI."""

from datetime import datetime, timezone
from typing import Optional, Dict, Any
import json
import hashlib
from sqlalchemy import (
    Column, Integer, String, DateTime, Numeric, Text, JSON, 
    ForeignKey, Boolean, Index, CheckConstraint, UniqueConstraint
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base = declarative_base()

class TimestampMixin:
    """Mixin for created_at and updated_at timestamps."""
    created_at = Column(DateTime(timezone=True), 
                       server_default=func.now(), 
                       nullable=False)
    updated_at = Column(DateTime(timezone=True), 
                       server_default=func.now(), 
                       onupdate=func.now(),
                       nullable=False)

class User(Base, TimestampMixin):
    """User model."""
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    
    # Relationships
    transactions = relationship("Transaction", back_populates="user", cascade="all, delete-orphan")
    
    # Indexes
    __table_args__ = (
        Index('idx_users_email', 'email'),
        Index('idx_users_created_at', 'created_at'),
    )
    
    def __repr__(self):
        return f"<User(id={self.id}, email='{self.email}')>"

class Transaction(Base, TimestampMixin):
    """Transaction model."""
    __tablename__ = 'transactions'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    amount = Column(Numeric(15, 2), nullable=False)
    currency = Column(String(3), nullable=False, default='USD')
    merchant_category = Column(String(100), nullable=False)
    device_id = Column(String(255), nullable=True)
    ip_address = Column(String(45), nullable=True)  # IPv6 compatible
    timestamp = Column(DateTime(timezone=True), nullable=False)
    raw_payload = Column(JSON, nullable=False)
    
    # Relationships
    user = relationship("User", back_populates="transactions")
    features = relationship("Feature", back_populates="transaction", cascade="all, delete-orphan")
    predictions = relationship("Prediction", back_populates="transaction", cascade="all, delete-orphan")
    
    # Constraints
    __table_args__ = (
        CheckConstraint('amount > 0', name='check_positive_amount'),
        Index('idx_transactions_user_id', 'user_id'),
        Index('idx_transactions_timestamp', 'timestamp'),
        Index('idx_transactions_merchant_category', 'merchant_category'),
        Index('idx_transactions_created_at', 'created_at'),
        Index('idx_transactions_user_timestamp', 'user_id', 'timestamp'),
    )
    
    def __repr__(self):
        return f"<Transaction(id={self.id}, amount={self.amount}, user_id={self.user_id})>"

class Feature(Base, TimestampMixin):
    """Feature model for storing extracted features."""
    __tablename__ = 'features'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    transaction_id = Column(Integer, ForeignKey('transactions.id'), nullable=False)
    feature_vector = Column(JSON, nullable=False)
    feature_schema_version = Column(String(100), nullable=False)
    
    # Relationships
    transaction = relationship("Transaction", back_populates="features")
    
    # Indexes
    __table_args__ = (
        Index('idx_features_transaction_id', 'transaction_id'),
        Index('idx_features_schema_version', 'feature_schema_version'),
        Index('idx_features_created_at', 'created_at'),
    )
    
    def __repr__(self):
        return f"<Feature(id={self.id}, transaction_id={self.transaction_id})>"

class Prediction(Base, TimestampMixin):
    """Prediction model for storing ML model outputs."""
    __tablename__ = 'predictions'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    transaction_id = Column(Integer, ForeignKey('transactions.id'), nullable=False)
    model_version = Column(String(100), nullable=False)
    fraud_probability = Column(Numeric(5, 4), nullable=False)  # 0.0000 to 1.0000
    prediction_label = Column(Boolean, nullable=False)
    confidence_score = Column(Numeric(5, 4), nullable=True)
    inference_time_ms = Column(Integer, nullable=True)
    
    # Relationships
    transaction = relationship("Transaction", back_populates="predictions")
    
    # Constraints
    __table_args__ = (
        CheckConstraint('fraud_probability >= 0 AND fraud_probability <= 1', 
                       name='check_probability_range'),
        CheckConstraint('confidence_score >= 0 AND confidence_score <= 1', 
                       name='check_confidence_range'),
        Index('idx_predictions_transaction_id', 'transaction_id'),
        Index('idx_predictions_model_version', 'model_version'),
        Index('idx_predictions_fraud_probability', 'fraud_probability'),
        Index('idx_predictions_created_at', 'created_at'),
    )
    
    def __repr__(self):
        return f"<Prediction(id={self.id}, fraud_probability={self.fraud_probability})>"

class AuditLog(Base):
    """Immutable audit log model.""" 
    __tablename__ = 'audit_logs'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    entity_type = Column(String(100), nullable=False)  # 'transaction', 'prediction', etc.
    entity_id = Column(Integer, nullable=False)
    action_type = Column(String(50), nullable=False)  # 'CREATE', 'UPDATE', 'DELETE'
    metadata = Column(JSON, nullable=False)
    checksum_hash = Column(String(64), nullable=False)  # SHA-256 hash
    created_at = Column(DateTime(timezone=True), 
                       server_default=func.now(), 
                       nullable=False)
    
    # Indexes
    __table_args__ = (
        Index('idx_audit_logs_entity', 'entity_type', 'entity_id'),
        Index('idx_audit_logs_action_type', 'action_type'),
        Index('idx_audit_logs_created_at', 'created_at'),
        Index('idx_audit_logs_checksum', 'checksum_hash'),
    )
    
    def __init__(self, entity_type: str, entity_id: int, action_type: str, metadata: Dict[str, Any]):
        self.entity_type = entity_type
        self.entity_id = entity_id
        self.action_type = action_type
        self.metadata = metadata
        self.checksum_hash = self._generate_checksum()
    
    def _generate_checksum(self) -> str:
        """Generate SHA-256 checksum for integrity verification."""
        data = json.dumps({
            'entity_type': self.entity_type,
            'entity_id': self.entity_id,
            'action_type': self.action_type,
            'metadata': self.metadata
        }, sort_keys=True, separators=(',', ':'))
        return hashlib.sha256(data.encode('utf-8')).hexdigest()
    
    def verify_integrity(self) -> bool:
        """Verify the integrity of the audit log entry."""
        return self.checksum_hash == self._generate_checksum()
    
    def __repr__(self):
        return f"<AuditLog(id={self.id}, entity_type='{self.entity_type}', action_type='{self.action_type}')>"

class ModelRegistry(Base, TimestampMixin):
    """Model registry for tracking ML model versions."""
    __tablename__ = 'model_registry'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    model_name = Column(String(100), nullable=False)
    model_version = Column(String(100), nullable=False)
    model_type = Column(String(50), nullable=False)  # 'logistic_regression', 'random_forest', etc.
    model_path = Column(String(500), nullable=False)
    preprocessing_path = Column(String(500), nullable=False)
    metrics = Column(JSON, nullable=False)
    is_active = Column(Boolean, default=False, nullable=False)
    training_data_hash = Column(String(64), nullable=False)
    feature_schema_version = Column(String(100), nullable=False)
    
    # Constraints
    __table_args__ = (
        UniqueConstraint('model_name', 'model_version', name='uq_model_name_version'),
        Index('idx_model_registry_active', 'is_active'),
        Index('idx_model_registry_model_type', 'model_type'),
        Index('idx_model_registry_created_at', 'created_at'),
    )
    
    def __repr__(self):
        return f"<ModelRegistry(id={self.id}, model_name='{self.model_name}', version='{self.model_version}')>"