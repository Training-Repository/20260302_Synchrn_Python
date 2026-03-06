from pydantic import ConfigDict
from sqlmodel import SQLModel, Field
import json
import os


class CarInput(SQLModel):
    size: str
    fuel: str | None = "electric"
    doors: int
    transmission: str | None = "auto"
    model_config = ConfigDict(
        json_schema_extra = {
            "example": {
                "size": "cfg-size",
                "fuel": "tesla",
                "doors": 4,
                "transmission": "automatic"
            }
        }
    )

class Car(CarInput):
    id: int

class Car_DBModel(CarInput, table=True):
    id: int|None = Field(primary_key=True, default=None)
