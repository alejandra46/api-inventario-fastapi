from sqlalchemy.orm import Session

from app import models, schemas


def get_products(db: Session):
    return db.query(models.Product).all()


def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()


def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(
        name=product.name,
        price=product.price,
        stock=product.stock,
        category=product.category
    )

    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    return db_product


def update_product(db: Session, product_id: int, product: schemas.ProductUpdate):

    db_product = get_product(db, product_id)

    if db_product:

        db_product.name = product.name
        db_product.price = product.price
        db_product.stock = product.stock
        db_product.category = product.category

        db.commit()
        db.refresh(db_product)

    return db_product


def delete_product(db: Session, product_id: int):

    db_product = get_product(db, product_id)

    if db_product:
        db.delete(db_product)
        db.commit()

    return db_product