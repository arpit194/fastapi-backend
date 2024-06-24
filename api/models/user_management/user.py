from sqlalchemy import Column, String, null
from api.databases.base_class import mapper_registry
from api.models.mixins import BaseModelMixin


@mapper_registry.mapped
class User(BaseModelMixin):
    __tablename__ = "user"

    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True, index=True)
    password = Column(String(100), nullable=False)

    def __init__(
        self,
        first_name: str,
        last_name: str,
        email: str,
        password: str,
        created_by: str = None,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.created_by = created_by
