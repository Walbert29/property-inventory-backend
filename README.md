# PROPERTY INVENTORY API

This API is in charge of processing the information of a property inventory, there are instructions such as the main technologies used, the structure of the microservice, among others.

## 🛠 Used technology

- **Programming language:** Python
- **Web framework:** FastAPI
- **Database:** MySQL 
- **Testing:** The Test-Driven Development (TDD) approach is followed using unittest.
- **Web server:** Uvicorn
- **Data validation:** Pydantic

## 📚 Project Organization

The development of the project follows a layer-based architecture. The code is organized as follows:

- `src/`: Where the main source code of the project is stored.
    - `schemas/`: Directory used to define the structure, validation and serialization of the data.
    - `controllers/`: Directory where input requests are processed.
    - `database/`: Directory where database connections are controlled.
    - `services/`: Directory where the business logic is grouped and processed.
    - `main.py/`: Main entry point.
    - `settings.py/`: File where the microservice configurations are managed.
- `.gitignore/`: Specify which files should be ignored by Git.
- `README.md/`: Provides information and documentation about the project.
- `requirements.txt/`: Used to specify project dependencies.
- `test/`:Where the project tests are executed.

## ▶️Configuration and execution

1. Clone this repository
    ```bash
    https://github.com/Walbert29/property-inventory-backend.git
    ```
2. Create and activate a virtual environment

    **Linux:**
    
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

    **Windows:**

    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

3. Install the dependencies
    ```bash
    pip install -r requirements.txt
    ```
4. Start the server
    
    **Using the main entry point:**
    ```bash
    cd src/
    python main.py
    ```

## 🏁Endpoints

### Search properties
This endpoint returns the properties that meet the criteria sent
- **Path:** `/properties`
- **Method:** GET
- **Params:**
    - `status_id` (int): Filter by status
    - `year_construction` (int): Filter by year of construction
    - `city` (str): Filter by city

### React property
This endpoint allows a user to like a property
- **Path:** `/property/{property_id}/user/{user_id}`
- **Method:** POST

## 📃Versions

### v1.0.0

- Creation of the README with the project guidelines