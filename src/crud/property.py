import logging

from database.database import create_connection

def get_properties_by_filters(status_ids, year_construction: int, city: str):
    """
    Get properties filtered by status, year built, and city.

    Args:
        status_id: Property Status ID.
        year_construction (int): Year of construction of the property.
        city (str): Property City.

    Returns:
        list: List of properties that meet the specified filters.
    """

    method = get_properties_by_filters.__name__

    try:
        connection, cursor = create_connection()
    
    except Exception as ex:
        logging.error(f"Error establishing connection to the database, method: {method} with detail: {ex.args}")
        raise ex

    try:
        where = ""

        if year_construction:
            where += f" AND p.year = {year_construction}"
        
        if city:
            where += f" AND lower(city) like '%{city.lower()}%'"

        query = f"""
            SELECT p.id, p.address, p.city, sh.status_id, s.name status_name, p.price, p.description
            FROM status s INNER JOIN status_history sh
            ON s.id = sh.status_id INNER JOIN property p
            ON p.id = sh.property_id INNER JOIN (
                SELECT property_id, MAX(id) AS max_id
                FROM status_history 
                GROUP BY property_id
                ) calc_max_status
            ON sh.id = calc_max_status.max_id
            WHERE sh.status_id IN {status_ids} {where}
        """

        cursor.execute(query)
        results = cursor.fetchall()
        column_names = cursor.column_names
        results = [dict(zip(column_names, record)) for record in results]

        return results

    except Exception as ex:
        logging.error(f"Error executing {method} with detail: {ex.args}")
        raise ex
    finally:
        cursor.close()
        connection.close()