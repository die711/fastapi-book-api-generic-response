from typing import Optional, Generic, TypeVar
from pydantic import BaseModel, ConfigDict
from pydantic.generics import GenericModel

T = TypeVar('T')


class BookSchema(BaseModel):
    id: int
    title: str
    description: str

    model_config = ConfigDict(
        from_attributes=True
    )


class BookSchemaCreate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None


class BookSchemaUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None


class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]
