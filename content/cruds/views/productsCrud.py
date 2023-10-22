from reactpy import component, html, use_state, use_effect
import asyncio
import reactpy
from content.api import getProducts, postProduct, deleteProduct, updateProduct

@component
def ProductsCrud():
    products, set_products = use_state([])
    name, set_name = use_state("")
    description, set_description = use_state("")
    props, set_props = use_state({})
    stock, set_stock = use_state("")

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
                "stock": stock
            }
            print(new_product)
            await postProduct(new_product)
            await fillItems()
        else:
            updated_product = {
                "name": name,
                "description": description,
                "props": props,
                "stock": stock,
                "id": product_id
            }
            await updateProduct(product_id, updated_product)
            await fillItems()

        set_name("")
        set_description("")
        set_props({})
        set_stock("")
        set_editing(False)
        set_product_id(None)

    async def handle_delete(product):
        await deleteProduct(product)
        await fillItems()

    async def handle_edit(product):
        set_editing(True)
        set_name(product["name"])
        set_description(product["description"])
        set_props(product["props"])
        set_props(product["stock"])
        set_product_id(product["id"])

    def delete_button_click_handler(e, product_id):
        async def async_handler():
            await handle_delete(product_id)

        asyncio.ensure_future(async_handler())

    def edit_button_click_handler(e, product):
        async def async_handler():
            await handle_edit(product)

        asyncio.ensure_future(async_handler())

    def create_table_row(product):
        return html.tr(
            html.td(product['name']),
            html.td(product['description']),
            html.td(product['props']),
            html.td(product['stock']),
            html.td(product['enabled']),
            html.td(
                html.button({
                    "on_click": lambda e, product_id=product["id"]: delete_button_click_handler(e, product_id),
                    "class_name": "btn btn-danger"
                }, "delete"),
                html.button({
                    "on_click": lambda e, product=product: edit_button_click_handler(e, product),
                    "class_name": "btn btn-secondary"
                }, "edit"),
            )
        )

    list_items = html.div(
        {"class": "card shadow mb-4"},
        html.div(
            {"class": "card-header py-3"},
            html.h6({"class": "m-0 font-weight-bold text-primary"}, "Products Example"),
        ),
        html.div(
            {"class": "card-body"},
            html.div(
                {"class": "table-responsive"},
                html.table(
                    {"class": "table table-bordered", "id": "dataTable", "width": "100%", "cellspacing": "0"},
                    html.thead(
                        html.tr(
                            html.th("Name"),
                            html.th("Description"),
                            html.th("Props"),
                            html.th("Stock"),
                            html.th("Enabled"),
                            html.th(""),
                        ),
                    ),
                    html.tfoot(
                        html.tr(
                            html.th("Name"),
                            html.th("Description"),
                            html.th("Props"),
                            html.th("Stock"),
                            html.th("Enabled"),
                            html.th(""),
                        ),
                    ),
                    html.tbody(
                        [create_table_row(row) for row in products]
                    ),
                ),
            ),
        ),
    )

    return html.div(
        {
            "style": {
                "padding": "3rem",
            }
        },
        list_items,
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

            html.input({
                "type": "number",
                "placeholder": "Stock",
                "on_change": lambda e: set_stock(e["target"]["value"]),
                "value": stock,
                "class_name": "form-control mb-2"
            }),
            html.input({
                "type": "text",
                "placeholder": "Props",
                "on_change": lambda e: set_props(e["target"]["value"]),
                "value": props,
                "class_name": "form-control mb-2"
            }),
            html.button({
                "type": "submit",
                "class_name": "btn btn-primary btn-block"
            }, "Create" if not editing else "Update"),
        ),
    )
