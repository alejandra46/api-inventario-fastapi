from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app import crud, schemas

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.post("/", response_model=schemas.ProductResponse, status_code=status.HTTP_201_CREATED)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db, product)


@router.get("/", response_model=list[schemas.ProductResponse])
def list_products(db: Session = Depends(get_db)):
    return crud.get_products(db)


@router.get("/{product_id}", response_model=schemas.ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = crud.get_product(db, product_id)

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Producto no encontrado"
        )

    return product


@router.put("/{product_id}", response_model=schemas.ProductResponse)
def update_product(
    product_id: int,
    product: schemas.ProductUpdate,
    db: Session = Depends(get_db)
):
    updated = crud.update_product(db, product_id, product)

    if updated is None:
        raise HTTPException(
            status_code=404,
            detail="Producto no encontrado"
        )

    return updated


@router.delete("/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_product(db, product_id)

    if deleted is None:
        raise HTTPException(
            status_code=404,
            detail="Producto no encontrado"
        )

    return {"message": "Producto eliminado correctamente"}