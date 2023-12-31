from pydantic import BaseModel, Field, EmailStr


class CustomerSchema(BaseModel):
    username: str = Field(..., min_length=3, max_length=32)
    email: EmailStr
    first_name: str = Field(..., min_length=3, max_length=32)
    last_name: str = Field(..., min_length=3, max_length=32)


class CustomerOut(CustomerSchema):
    id: int
