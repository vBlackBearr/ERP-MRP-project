from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from content.cruds.models import models
from content.cruds.schemas import schemas
from content.database import get_db

router = APIRouter()


@router.post("/backend/sales")
def create_sale(sale: schemas.SaleCreate, db: Session = Depends(get_db)):
    db_sale = models.Sale(**sale.dict())
    db.add(db_sale)
    db.commit()
    db.refresh(db_sale)
    return db_sale


@router.get("/backend/sales/{sale_id}")
def read_sale(sale_id: int, db: Session = Depends(get_db)):
    db_sale = db.query(models.Sale).filter(models.Sale.id == sale_id).first()
    if db_sale is None:
        raise HTTPException(status_code=404, detail="Sale not found")
    return db_sale


@router.get("/backend/sales")
def read_sales(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    sales = db.query(models.Sale).offset(skip).limit(limit).all()
    return sales


@router.put("/backend/sales/{sale_id}")
def update_sale(sale_id: int, sale: schemas.SaleUpdate, db: Session = Depends(get_db)):
    db_sale = db.query(models.Sale).filter(models.Sale.id == sale_id).first()
    if db_sale is None:
        raise HTTPException(status_code=404, detail="Sale not found")

    for key, value in sale.dict().items():
        setattr(db_sale, key, value)

    db.commit()
    db.refresh(db_sale)
    return db_sale


@router.delete("/backend/sales/{sale_id}")
def delete_sale(sale_id: int, db: Session = Depends(get_db)):
    db_sale = db.query(models.Sale).filter(models.Sale.id == sale_id).first()
    if db_sale is None:
        raise HTTPException(status_code=404, detail="Sale not found")

    db.delete(db_sale)
    db.commit()

    return {"message": "Sale deleted"}
