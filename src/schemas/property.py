from typing import Union
from pydantic import BaseModel, Field

class Status(BaseModel):
    """
    This class is in charge of validating and building the structure for the status.

    Attributes:
        id (int): Status ID.
        name (str): Status name.
    """
    id: int = Field()
    name: str = Field()


class PropertyByFilterResponse(BaseModel):
    """
    This class is responsible for validating and building the property information structure.

    Attributes:
        address (str): Property address.
        property_id (int): Property ID.
        city (str): City where the property is located.
        status (Status): Property status.
        price (int): Property price.
        description (str): Detailed description of the property.
    """
    address: str = Field(min_length=3)
    property_id: int = Field()
    city: str = Field(min_length=3)
    status: Status = Field()
    price: int = Field(gt=0)
    description: Union[str, None] = Field()
    