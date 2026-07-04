from fastapi import FastAPI

from app.database import engine, Base
from app import models
from app.routers import products

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Product API",
    description="API para administrar un inventario de productos",
    version="1.0"
)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Product API!"}


app.include_router(products.router)