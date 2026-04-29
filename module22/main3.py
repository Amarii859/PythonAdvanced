from pydantic import BaseModel, field_validator, constr

class Address(BaseModel):
    id: int
    city: str
    street: constr(min_length=3, max_length=49)  # 2 < street < 50

    @field_validator('id')
    def id_must_be_positive(cls, v):
        if v < 0:
            raise ValueError("id cannot be nagativ number")
        return v


try:
    a = Address(id=1, city="Prishtine", street="Rruga Nena Tereze")
    print(a)
except ValueError as e:
    print(e)