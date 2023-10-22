from pydantic import BaseModel
from typing import Dict

class PartnerBase(BaseModel):
    name: str
    details: str
    direction: str
    api_endpoint: str
    props: dict
    enabled: bool

class PartnerCreate(PartnerBase):
    pass


class PartnerUpdate(PartnerBase):
    pass


class Partner(PartnerBase):
    id: int

    class Config:
        orm_mode = True
#
#
#       Raw Material
#
#
class RawMaterialBase(BaseModel):
    name: str
    description: str
    props: Dict
    stock: int
    enabled: bool


class RawMaterialCreate(RawMaterialBase):
    pass


class RawMaterialUpdate(RawMaterialBase):
    pass


class RawMaterial(RawMaterialBase):
    id: int

    class Config:
        orm_mode = True


#
#
#       Raw Materials stock
#
#
class RawMaterialStockBase(BaseModel):
    raw_material_id: int
    partner_id: int
    props: dict
    enabled: bool


class RawMaterialStockCreate(RawMaterialStockBase):
    pass


class RawMaterialStockUpdate(RawMaterialStockBase):
    pass


class RawMaterialStock(RawMaterialStockBase):
    id: int

    class Config:
        orm_mode = True


#
#
#     Products
#
#
class ProductBase(BaseModel):
    name: str
    description: str = None
    props: dict = {}
    stock: int
    enabled: bool = True


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    pass


class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True


#
#
#     Products Stock
#
#
""""
class ProductStockBase(BaseModel):
    product_id: int
    stock: int
    props: dict
    enabled: bool


class ProductStockCreate(ProductStockBase):
    pass


class ProductStockUpdate(ProductStockBase):
    pass


class ProductStock(ProductStockBase):
    id: int

    class Config:
        orm_mode = True

"""
#
#
#        BOM
#
#
class BOMBase(BaseModel):
    product_id: int
    raw_material_id: int
    quantity: int
    props: dict
    enabled: bool


class BOMCreate(BOMBase):
    pass


class BOMUpdate(BOMBase):
    pass


class BOM(BOMBase):
    id: int

    class Config:
        orm_mode = True


#
#
#      Sales
#
#
class SaleBase(BaseModel):
    date: str  
    total: float
    props: dict
    enabled: bool


class SaleCreate(SaleBase):
    pass


class SaleUpdate(SaleBase):
    pass


class Sale(SaleBase):
    id: int

    class Config:
        orm_mode = True


#
#
#     product-sales
#
#
class ProductSaleBase(BaseModel):
    product_id: int
    sale_id: int
    quantity: int
    subtotal: float
    props: dict
    enabled: bool


class ProductSaleCreate(ProductSaleBase):
    pass


class ProductSaleUpdate(ProductSaleBase):
    pass


class ProductSale(ProductSaleBase):
    id: int

    class Config:
        orm_mode = True