import time

import httpx
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from content.database import get_db, SessionLocal
from content.cruds.models.models import Partner

router = APIRouter()


@router.post("/api/products")
async def post_pedido(data: dict):
    print("\n\nPedido recibido por " + str(data["cantidad"]) + " iphones, manos a la obra\n\n")
    time.sleep(5)
    async with httpx.AsyncClient() as client:

        data = {
            "cantidad": data["cantidad"]
        }

        response = await client.post("http://3.99.218.61:8000/api/products/plasticos", json=data)

    if response.status_code == 200:
        result = response.json()
        return result
    else:
        return None


@router.post("/api/products/carcasas")
async def post_pedido(data: dict):
    print("\n\nPedido recibido por " + str(data["cantidad"]) + " iphones, manos a la obra\n\n")
    time.sleep(5)
    print("\n\nCalculando stock disponible\n\n")
    time.sleep(5)
    print("\n\nNo existe stock en el inventario, haciendo pedido a los proveedores\n\n")

    async with httpx.AsyncClient() as client:

        data = {
            "cantidad": data["cantidad"]
        }

        response = await client.post("http://35.183.123.206:8000/api/products/plasticos", json=data)

    if response.status_code == 200:
        result = response.json()
        return result
    else:
        return None


@router.post("/api/products/plasticos")
def post_pedido(data: dict):
    print("\n\nPedido recibido por " + str(data["cantidad"]) + " iphones, manos a la obra\n\n")
    time.sleep(5)
    print("\n\nCalculando stock disponible\n\n")
    time.sleep(5)
    print("\n\nStock disponible, haciendo envio\n\n")

    return {"Mensaje": "Pedido exitoso"}