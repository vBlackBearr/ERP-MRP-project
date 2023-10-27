import time

import httpx
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from content.database import get_db, SessionLocal
from content.cruds.models.models import Partner

router = APIRouter()


@router.post("/api/productss")
async def post_pedido(data: dict):
    print("\n\nPedido recibido por " + str(data["cantidad"]) + " iphones\n\n")
    time.sleep(5)
    async with httpx.AsyncClient() as client:

        data = {
            "cantidad": data["cantidad"]
        }

        response = await client.post("http://localhost:8003/api/products/plasticos", json=data)

    if response.status_code == 200:
        result = response.json()
        return result
    else:
        return None


@router.post("/api/products")
async def post_pedido(data: dict):
    print("\n\nPedido recibido por " + str(data["cantidad"]) + " iphones, manos a la obra\n\n")
    time.sleep(5)
    print("\n\nCalculando stock disponible\n\n")
    time.sleep(5)
    print("\n\nNo existe stock en el inventario, haciendo pedido a los proveedores\n\n")

    async with httpx.AsyncClient() as client:

        data = {
            "cantidad": data["cantidad"],
            "modelo": "adsajdlkas"
        }

        response = await client.post("http://localhost:8003/api/products/plasticos", json=data)

    if response.status_code == 200:
        print("\n\nPedido exitoso\n\n")
        result = response.json()
        return result
    else:
        return None


@router.post("/api/products/plasticos")
def post_pedido(data: dict):
    print("\n\nPedido recibido por " + str(data["cantidad"]) + " carcasas, manos a la obra\n\n")
    time.sleep(2)
    print("\n\nCalculando stock disponible\n\n")
    time.sleep(2)
    print("\n\nStock disponible, haciendo envio\n\n")

    return {"Mensaje": "Pedido exitoso"}