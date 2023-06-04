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
    - `controllers/`: Directory where input requests are processed.
    - `crud/`: Organize, store, and execute database operations.
    - `database/`: Directory where database connections are controlled.
    - `enums/`: Define the limited sets of options or states that can be used.
    - `schemas/`: Directory used to define the structure, validation and serialization of the data.
    - `services/`: Directory where the business logic is grouped and processed.
    - `main.py/`: Main entry point.
    - `settings.py/`: File where the microservice configurations are managed.
- `test/`:Where the project tests are executed.
- `.gitignore/`: Specify which files should be ignored by Git.
- `README.md/`: Provides information and documentation about the project.
- `requirements.txt/`: Used to specify project dependencies.

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

### **Search properties**
This endpoint returns the properties that meet the criteria sent.

The filters are applied through query params, so there is no JSON that should be sent by Front, but there are parameters wanted in the URL, described below.

- **Path:** `/properties`
- **Method:** GET
- **Params:**
    - `status_ids` List[int]: Filter by status
    - `year_construction` (int): Filter by year of construction
    - `city` (str): Filter by city

### **React property**
This endpoint allows a user to like a property
- **Path:** `/property/{property_id}/user/{user_id}`
- **Method:** POST

## 📃Versions

### v1.0.0

- Creation of the README with the project guidelines.

### v1.1.0

- Creation unit tests.

### v1.2.0

- The test cases have been defined.
- README update with the latest improvements and implementations.
- The properties microservice was created, with the respective validations of the models, queries to the database and transformation of the resulting data.