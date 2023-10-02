from fastapi import FastAPI
from reactpy.backend.fastapi import configure
from reactpy import component, html, use_state, use_effect

import asyncio
from controllerRawMaterials import router
import reactpy
from api import getRawMaterials, postRawMaterial, deleteRawMaterial

bootstrap_css = html.link({
    "rel": "stylesheet",
    "href": "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css"
})


@component
def App():
    raw_materials, set_raw_materials = use_state([])  # Cambia el nombre de las variables
    name, set_name = use_state("")  # Cambia el nombre de las variables
    description, set_description = use_state("")  # Cambia el nombre de las variables
    partner_id, set_partner_id = use_state(None)  # Cambia el nombre de las variables
    props, set_props = use_state({})  # Cambia el nombre de las variables
    enabled, set_enabled = use_state(True)  # Cambia el nombre de las variables

    editing, set_editing = use_state(False)
    raw_material_id, set_raw_material_id = use_state(None)  # Cambia el nombre de las variables

    async def fillItems():
        raw_materials_data = await getRawMaterials()  # Cambia el nombre de la función
        set_raw_materials(raw_materials_data)

    use_effect(fillItems)

    @reactpy.event(prevent_default=True)
    async def handle_submit(e):
        if not name or not description or not partner_id:
            return

        if not editing:
            new_raw_material = {
                "name": name,
                "description": description,
                "partner_id": partner_id,
                "props": props,
                "enabled": enabled
            }

            await postRawMaterial(new_raw_material)  # Cambia el nombre de la función
            await fillItems()
        else:
            updated_raw_materials = [raw_material if raw_material["id"] != raw_material_id else {
                "name": name,
                "description": description,
                "partner_id": partner_id,
                "props": props,
                "enabled": enabled,
                "id": raw_material_id
            } for raw_material in raw_materials]
            set_raw_materials(updated_raw_materials)

        set_name("")
        set_description("")
        set_partner_id(None)
        set_props({})
        set_enabled(True)
        set_editing(False)
        set_raw_material_id(None)

    async def handle_delete(raw_material):
        await deleteRawMaterial(raw_material)  # Cambia el nombre de la función
        await fillItems()

    async def handle_edit(raw_material):
        set_editing(True)
        set_name(raw_material["name"])
        set_description(raw_material["description"])
        set_partner_id(raw_material["partner_id"])
        set_props(raw_material["props"])
        set_enabled(raw_material["enabled"])
        set_raw_material_id(raw_material["id"])

    def delete_button_click_handler(e, raw_material_id):
        async def async_handler():
            await handle_delete(raw_material_id)

        asyncio.ensure_future(async_handler())

    def edit_button_click_handler(e, raw_material):
        async def async_handler():
            await handle_edit(raw_material)

        asyncio.ensure_future(async_handler())

    list_items = [html.li({
        "key": index,
        "class_name": "card card-body mb-2"
    },
        html.div(
            html.p({
                "class_name": "fw-bold h3"
            }, f"{raw_material['name']} - {raw_material['description']}"),
            html.p(
                {
                    "class_name": "text-muted"
                },
                f"{raw_material['id']}",
            ),
            html.button({
                "on_click": lambda e, raw_mat=raw_material["id"]: delete_button_click_handler(e, raw_mat),
                "class_name": "btn btn-danger"
            }, "delete"),
            html.button({
                "on_click": lambda e, raw_material=raw_material: edit_button_click_handler(e, raw_material),
                "class_name": "btn btn-secondary"
            }, "edit"),
        )
    ) for index, raw_material in enumerate(raw_materials)]

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
            html.input({
                "type": "number",
                "placeholder": "Partner ID",
                "on_change": lambda e: set_partner_id(int(e["target"]["value"])),
                "value": partner_id,
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
