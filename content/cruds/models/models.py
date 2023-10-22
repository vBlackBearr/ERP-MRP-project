from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from sqlalchemy import Column, Integer, String, JSON, Boolean, ForeignKey, Date, DECIMAL
from sqlalchemy.orm import relationship
from content.database import Base

app = FastAPI()
app.mount("/content", StaticFiles(directory="content"), name="content")


class Partner(Base):
    __tablename__ = "partners"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    details = Column(String)
    direction = Column(String)
    api_endpoint = Column(String)
    props = Column(JSON)
    enabled = Column(Boolean)

    raw_materials_partners = relationship("RawMaterialPartner", back_populates="partner")




class RawMaterial(Base):
    __tablename__ = "raw_materials"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    props = Column(JSON)
    stock = Column(Integer)
    enabled = Column(Boolean)
    raw_materials_partners = relationship("RawMaterialPartner", back_populates="raw_material")
    bom = relationship("BOM", back_populates="raw_material")


class RawMaterialPartner(Base):
    __tablename__ = "raw_materials_partners"

    id = Column(Integer, primary_key=True, index=True)
    raw_material_id = Column(Integer, ForeignKey('raw_materials.id'))
    partner_id = Column(Integer, ForeignKey('partners.id'))
    props = Column(JSON)
    enabled = Column(Boolean)
    partner = relationship("Partner", back_populates="raw_materials_partners")
    raw_material = relationship("RawMaterial", back_populates="raw_materials_partners")



# class RawMaterialStock(Base):
#     __tablename__ = "raw_materials_stock"
#
#     id = Column(Integer, primary_key=True, index=True)
#     raw_material_id = Column(Integer, ForeignKey('raw_materials.id'))
#     stock = Column(Integer)
#     props = Column(JSON)
#     enabled = Column(Boolean)
#
#     raw_material = relationship("RawMaterial", back_populates="raw_material_stock")


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    props = Column(JSON)
    stock = Column(Integer)
    enabled = Column(Boolean)

    bom = relationship("BOM", back_populates="product")
    product_sale = relationship("ProductSale", back_populates="product")



# class ProductStock(Base):
#     __tablename__ = "products_stock"
#
#     id = Column(Integer, primary_key=True, index=True)
#     product_id = Column(Integer, ForeignKey('products.id'))
#     stock = Column(Integer)
#     props = Column(JSON)
#     enabled = Column(Boolean)
#     product = relationship("Product", back_populates="product_stock")


class BOM(Base):
    __tablename__ = "bom"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    raw_material_id = Column(Integer, ForeignKey('raw_materials.id'))
    quantity = Column(Integer)
    props = Column(JSON)
    enabled = Column(Boolean)
    product = relationship("Product", back_populates="bom")
    raw_material = relationship("RawMaterial", back_populates="bom")


class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)
    total = Column(DECIMAL(10, 2))
    props = Column(JSON)
    enabled = Column(Boolean)
    product_sale = relationship("ProductSale", back_populates="sale")


class ProductSale(Base):
    __tablename__ = "products_sales"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    sale_id = Column(Integer, ForeignKey('sales.id'))
    quantity = Column(Integer)
    subtotal = Column(DECIMAL(10, 2))
    props = Column(JSON)
    enabled = Column(Boolean)
    product = relationship("Product", back_populates="product_sale")
    sale = relationship("Sale", back_populates="product_sale")
