from uuid6 import uuid7
from sqlalchemy import Column, DateTime, ForeignKey, String, func


class BaseModelMixin(object):
    id = Column(String(36), primary_key=True, default=uuid7())
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), nullable=True, onupdate=func.now())
    deleted_at = Column(DateTime(timezone=True), nullable=True)

    created_by = Column(String(36), ForeignKey("user.id"), nullable=True)
    updated_by = Column(String(36), ForeignKey("user.id"), nullable=True)
    deleted_by = Column(String(36), ForeignKey("user.id"), nullable=True)
