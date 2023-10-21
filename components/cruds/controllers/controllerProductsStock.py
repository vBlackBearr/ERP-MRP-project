from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from components.cruds.models.models import ProductStock
from schemas import ProductStockCreate, ProductStockUpdate

router = APIRouter()

@router.get("/products_stock")
def get_products_stock(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    products_stock = db.query(ProductStock).offset(skip).limit(limit).all()
    return products_stock

@router.post("/products_stock")
def create_product_stock(product_stock: ProductStockCreate, db: Session = Depends(get_db)):
    db_product_stock = ProductStock(**product_stock.dict())
    db.add(db_product_stock)
    db.commit()
    db.refresh(db_product_stock)
    return db_product_stock

@router.get("/products_stock/{product_stock_id}")
def get_product_stock(product_stock_id: int, db: Session = Depends(get_db)):
    db_product_stock = db.query(ProductStock).filter(ProductStock.id == product_stock_id).first()
    if db_product_stock is None:
        raise HTTPException(status_code=404, detail="Product stock not found")
    return db_product_stock

@router.put("/products_stock/{product_stock_id}")
def update_product_stock(product_stock_id: int, product_stock: ProductStockUpdate, db: Session = Depends(get_db)):
    db_product_stock = db.query(ProductStock).filter(ProductStock.id == product_stock_id).first()
    if db_product_stock is None:
        raise HTTPException(status_code=404, detail="Product stock not found")

    for field, value in product_stock.dict(exclude_unset=True).items():
        setattr(db_product_stock, field, value)

    db.commit()
    db.refresh(db_product_stock)
    return db_product_stock

@router.delete("/products_stock/{product_stock_id}")
def delete_product_stock(product_stock_id: int, db: Session = Depends(get_db)):
    db_product_stock = db.query(ProductStock).filter(ProductStock.id == product_stock_id).first()
    if db_product_stock is None:
        raise HTTPException(status_code=404, detail="Product stock not found")

    db.delete(db_product_stock)
    db.commit()

    return {"message": "Product stock deleted"}
