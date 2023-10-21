from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from components.cruds.models.models import RawMaterialStock
from schemas import RawMaterialStockCreate, RawMaterialStockUpdate

router = APIRouter()


@router.post("/raw_materials_stock")
def create_raw_material_stock(raw_material_stock: RawMaterialStockCreate, db: Session = Depends(get_db)):
    db_raw_material_stock = RawMaterialStock(**raw_material_stock.dict())
    db.add(db_raw_material_stock)
    db.commit()
    db.refresh(db_raw_material_stock)
    return db_raw_material_stock


@router.get("/raw_materials_stock/{raw_material_stock_id}")
def read_raw_material_stock(raw_material_stock_id: int, db: Session = Depends(get_db)):
    db_raw_material_stock = db.query(RawMaterialStock).filter(RawMaterialStock.id == raw_material_stock_id).first()
    if db_raw_material_stock is None:
        raise HTTPException(status_code=404, detail="Raw material stock not found")
    return db_raw_material_stock


@router.put("/raw_materials_stock/{raw_material_stock_id}")
def update_raw_material_stock(raw_material_stock_id: int, raw_material_stock_update: RawMaterialStockUpdate,
                              db: Session = Depends(get_db)):
    db_raw_material_stock = db.query(RawMaterialStock).filter(RawMaterialStock.id == raw_material_stock_id).first()
    if db_raw_material_stock is None:
        raise HTTPException(status_code=404, detail="Raw material stock not found")

    for key, value in raw_material_stock_update.dict().items():
        setattr(db_raw_material_stock, key, value)

    db.commit()
    db.refresh(db_raw_material_stock)
    return db_raw_material_stock


@router.delete("/raw_materials_stock/{raw_material_stock_id}", response_model=dict)
def delete_raw_material_stock(raw_material_stock_id: int, db: Session = Depends(get_db)):
    db_raw_material_stock = db.query(RawMaterialStock).filter(RawMaterialStock.id == raw_material_stock_id).first()
    if db_raw_material_stock is None:
        raise HTTPException(status_code=404, detail="Raw material stock not found")

    db.delete(db_raw_material_stock)
    db.commit()
    return {"message": "Raw material stock deleted"}
