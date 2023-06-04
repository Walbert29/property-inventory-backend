import logging

from fastapi import status
from fastapi.responses import JSONResponse
from typing import List

from enums.status_property import StatusProperty
from schemas.property import Status, PropertyByFilterResponse
from crud.property import get_properties_by_filters

def search_properties_by_filters(status_ids: List[int] = None, year_construction: int = None, city: str = None):
    """
    Search properties filtered by status, year of construction and city.

    Args:
    - status_ids (List[int]): List of valid status IDs.
    - year_construction (int, optional): Year of construction of the properties.
    - city (str, optional): Property city.

    Returns:
    - List[PropertyByFilterResponse]: Filtered property list.

    Raises:
    - JSONResponse: If invalid statuses are provided in status_ids.
    - Exception: If an error occurs when executing the property lookup.
    """
    try:
        method = search_properties_by_filters.__name__

        # Validation that the sent states are valid
        valid_statuses = (StatusProperty.EN_VENTA.value, StatusProperty.PRE_VENTA.value, StatusProperty.VENDIDO.value)

        if status_ids:
            invalid_statuses = set(status_ids) - set(valid_statuses)

            if invalid_statuses:
                return JSONResponse(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    content={"message": f"The following states {invalid_statuses} are not available"},
                )
            if len(status_ids) > 1:
                status_ids = tuple(status_ids)
            else:
                status_ids = str(tuple(status_ids)).replace(',','')

        else:
            status_ids = valid_statuses
        
        # Request to the database and processing of the results
        properties_result = get_properties_by_filters(status_ids=status_ids, city=city, year_construction=year_construction)
        
        if not properties_result:
            return []
        
        properties_response = []

        for property in properties_result:
            try:
                current_status = Status(
                    id=property["status_id"],
                    name=property["status_name"]
                )
                current_property = PropertyByFilterResponse(
                    property_id=property["id"],
                    address=property["address"],
                    city=property["city"],
                    description=property["description"],
                    price=property["price"],
                    status=current_status,
                )
            except ValueError as ex:
                logging.warning(f"Error processing property: {property['id']}, detail: {ex.args}")
                continue
            
            properties_response.append(current_property)

        return properties_response

    except Exception as ex:
        logging.error(f"Error executing {method} with detail: {ex.args}")
        return JSONResponse(
            status_code=status.HTTP_424_FAILED_DEPENDENCY,
            content={"message": ex.args},
        )