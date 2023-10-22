from fastapi import FastAPI
from reactpy.backend.fastapi import configure
from reactpy import component, html, use_state, use_effect

import asyncio
from content.cruds.controllers.controllerSales import router  # Cambia el import al controlador de ventas
import reactpy
from content.api import getSales, postSale, deleteSale  # Cambia los nombres de las funciones de API



@component
def SalesCrud():
    sales, set_sales = use_state([])  # Cambia el nombre de las variables
    date, set_date = use_state("")  # Cambia el nombre de las variables
    total, set_total = use_state("")  # Cambia el nombre de las variables
    props, set_props = use_state({})  # Cambia el nombre de las variables
    enabled, set_enabled = use_state(True)  # Cambia el nombre de las variables

    editing, set_editing = use_state(False)
    sale_id, set_sale_id = use_state(None)  # Cambia el nombre de las variables

    async def fillItems():
        sales_data = await getSales()  # Cambia el nombre de la función
        set_sales(sales_data)

    use_effect(fillItems)

    @reactpy.event(prevent_default=True)
    async def handle_submit(e):
        if not date or not total:
            return

        if not editing:
            new_sale = {
                "date": date,
                "total": total,
                "props": props,
                "enabled": enabled
            }

            await postSale(new_sale)  # Cambia el nombre de la función
            await fillItems()
        else:
            updated_sales = [sale if sale["id"] != sale_id else {
                "date": date,
                "total": total,
                "props": props,
                "enabled": enabled,
                "id": sale_id
            } for sale in sales]
            set_sales(updated_sales)

        set_date("")
        set_total("")
        set_props({})
        set_enabled(True)
        set_editing(False)
        set_sale_id(None)

    async def handle_delete(sale):
        await deleteSale(sale)  # Cambia el nombre de la función
        await fillItems()

    async def handle_edit(sale):
        set_editing(True)
        set_date(sale["date"])
        set_total(sale["total"])
        set_props(sale["props"])
        set_enabled(sale["enabled"])
        set_sale_id(sale["id"])

    def delete_button_click_handler(e, sale_id):
        async def async_handler():
            await handle_delete(sale_id)

        asyncio.ensure_future(async_handler())

    def edit_button_click_handler(e, sale):
        async def async_handler():
            await handle_edit(sale)

        asyncio.ensure_future(async_handler())

    list_items = [html.li({
        "key": index,
        "class_name": "card card-body mb-2"
    },
        html.div(
            html.p({
                "class_name": "fw-bold h3"
            }, f"Date: {sale['date']} - Total: {sale['total']}"),
            html.p(
                {
                    "class_name": "text-muted"
                },
                f"ID: {sale['id']}",
            ),
            html.button({
                "on_click": lambda e, sal=sale["id"]: delete_button_click_handler(e, sal),
                "class_name": "btn btn-danger"
            }, "Delete"),
            html.button({
                "on_click": lambda e, sale=sale: edit_button_click_handler(e, sale),
                "class_name": "btn btn-secondary"
            }, "Edit"),
        )
    ) for index, sale in enumerate(sales)]

    return html.div(
        {
            "style": {
                "padding": "3rem",
            }
        },
        html.form(
            {
                "on_submit": handle_submit
            },
            html.input({
                "type": "date",
                "placeholder": "Date",
                "on_change": lambda e: set_date(e["target"]["value"]),
                "value": date,
                "class_name": "form-control mb-2"
            }),
            html.input({
                "type": "number",
                "placeholder": "Total",
                "on_change": lambda e: set_total(e["target"]["value"]),
                "value": total,
                "class_name": "form-control mb-2"
            }),
            html.button({
                "type": "submit",
                "class_name": "btn btn-primary btn-block"
            }, "Create" if not editing else "Update"),
        ),
        html.ul(
            list_items
        )
    )


app = FastAPI()

app.include_router(router)

configure(app, SalesCrud)
