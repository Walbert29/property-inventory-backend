import uvicorn
from fastapi import FastAPI
from controllers.property import property_router


app = FastAPI(
    title="Habi Property API",
    description="This API is responsible for the management and search of properties",
    version="1.3.0",
    root_path=""
)

app.include_router(property_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)