from fastapi import FastAPI
from reactpy.backend.fastapi import configure
from reactpy import component, html, use_state, use_effect

import asyncio
from components.cruds.controllers.controllerProducts import router  # Asegúrate de importar el módulo correcto
import reactpy
from api import getProducts, postProduct, deleteProduct  # Asegúrate de importar las funciones correctas

bootstrap_css = html.link({
    "rel": "stylesheet",
    "href": "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css"
})

@component
def App():
    products, set_products = use_state([])
    name, set_name = use_state("")
    description, set_description = use_state("")
    props, set_props = use_state({})
    enabled, set_enabled = use_state(True)

    editing, set_editing = use_state(False)
    product_id, set_product_id = use_state(None)

    async def fillItems():
        products_data = await getProducts()
        set_products(products_data)

    use_effect(fillItems)

    @reactpy.event(prevent_default=True)
    async def handle_submit(e):
        if not name or not description:
            return

        if not editing:
            new_product = {
                "name": name,
                "description": description,
                "props": props,
                "enabled": enabled
            }

            await postProduct(new_product)
            await fillItems()
        else:
            updated_products = [product if product["id"] != product_id else {
                "name": name,
                "description": description,
                "props": props,
                "enabled": enabled,
                "id": product_id
            } for product in products]
            set_products(updated_products)

        set_name("")
        set_description("")
        set_props({})
        set_enabled(True)
        set_editing(False)
        set_product_id(None)

    async def handle_delete(product_id):
        await deleteProduct(product_id)
        await fillItems()

    async def handle_edit(product):
        set_editing(True)
        set_name(product["name"])
        set_description(product["description"])
        set_props(product["props"])
        set_enabled(product["enabled"])
        set_product_id(product["id"])

    def delete_button_click_handler(e, product_id):
        async def async_handler():
            await handle_delete(product_id)

        asyncio.ensure_future(async_handler())

    def edit_button_click_handler(e, product):
        async def async_handler():
            await handle_edit(product)

        asyncio.ensure_future(async_handler())

    list_items = [html.li({
        "key": index,
        "class_name": "card card-body mb-2"
    },
        html.div(
            html.p({
                "class_name": "fw-bold h3"
            }, f"{product['name']} - {product['description']}"),
            html.p(
                {
                    "class_name": "text-muted"
                },
                f"{product['id']}",
            ),
            html.button({
                "on_click": lambda e, prod=product["id"]: delete_button_click_handler(e, prod),
                "class_name": "btn btn-danger"
            }, "delete"),
            html.button({
                "on_click": lambda e, product=product: edit_button_click_handler(e, product),
                "class_name": "btn btn-secondary"
            }, "edit"),
        )
    ) for index, product in enumerate(products)]

    return html.div(
        {
            "style": {
                "padding": "3rem",
            }
        },
        bootstrap_css,
        html.form(
            {
                "on_submit": handle_submit
            },
            html.input({
                "type": "text",
                "placeholder": "Name",
                "on_change": lambda e: set_name(e["target"]["value"]),
                "autofocus": True,
                "value": name,
                "class_name": "form-control mb-2"
            }),
            html.input({
                "type": "text",
                "placeholder": "Description",
                "on_change": lambda e: set_description(e["target"]["value"]),
                "value": description,
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

configure(app, App)
