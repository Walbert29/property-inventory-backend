from typing import List
from fastapi import APIRouter, status, Query

from services.property import search_properties_by_filters

property_router = APIRouter()


@property_router.get(
    path="/properties",
    tags=["Properties"],
    status_code=status.HTTP_200_OK,
    summary="Get properties by filters"
)
def get_properties_by_filters(
    status_ids: List[int] = Query(default=None), year_construction: int = None, city: str = None
):
    """
    Gets filtered properties based on specified parameters.

    Args:
    - status_ids (List[int], optional): List of property status IDs.
    - year_construction (int, optional): Year of construction of the properties.
    - city (str, optional): Property city.

    Returns:
    - List[PropertyByFilterResponse]: Filtered property list.

    """
    return search_properties_by_filters(
        status_ids = status_ids, year_construction = year_construction, city = city
    )