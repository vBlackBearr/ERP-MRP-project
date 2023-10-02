
from fastapi import FastAPI
from reactpy.backend.fastapi import configure
from reactpy import component, html, use_state, use_effect

import asyncio
from controllerPartners import router
import reactpy
from api import getPartners, postPartner, deletePartner

bootstrap_css = html.link({
    "rel": "stylesheet",
    "href": "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css"
})


@component
def App():
    partners, set_partners = use_state([])
    name, set_name = use_state("")
    details, set_details = use_state("")
    direction, set_direction = use_state("")
    api_endpoint, set_api_endpoint = use_state("")

    editing, set_editing = use_state(False)
    partner_id, set_partner_id = use_state(None)

    async def fillItems():
        partners_data = await getPartners()
        set_partners(partners_data)

    use_effect(fillItems)

    @reactpy.event(prevent_default=True)
    async def handle_submit(e):
        if not name or not details or not direction or not api_endpoint:
            return

        if not editing:
            new_partner = {
                "name": name,
                "details": details,
                "direction": direction,
                "api_endpoint": api_endpoint
            }

            await postPartner(new_partner)
            await fillItems()
        else:
            updated_partners = [partner if partner["id"] != partner_id else {
                "name": name,
                "details": details,
                "direction": direction,
                "api_endpoint": api_endpoint,
                "id": partner_id
            } for partner in partners]
            set_partners(updated_partners)

        set_name("")
        set_details("")
        set_direction("")
        set_api_endpoint("")
        set_editing(False)
        set_partner_id(None)

    async def handle_delete(part):
        await deletePartner(part)
        await fillItems()

    async def handle_edit(partner):
        set_editing(True)
        set_name(partner["name"])
        set_details(partner["details"])
        set_direction(partner["direction"])
        set_api_endpoint(partner["api_endpoint"])
        set_partner_id(partner["id"])

    def delete_button_click_handler(e, partner_id):
        async def async_handler():
            await handle_delete(partner_id)

        asyncio.ensure_future(async_handler())

    def edit_button_click_handler(e, partner):
        async def async_handler():
            await handle_edit(partner)

        asyncio.ensure_future(async_handler())

    list_items = [html.li({
        "key": index,
        "class_name": "card card-body mb-2"
    },
        html.div(
            html.p({
                "class_name": "fw-bold h3"
            }, f"{partner['name']} - {partner['details']}"),
            html.p(
                {
                    "class_name": "text-muted"
                },
                f"{partner['id']}",
            ),
            html.button({
                "on_click": lambda e, partn=partner["id"]: delete_button_click_handler(e, partn),
                "class_name": "btn btn-danger"
            }, "delete"),
            html.button({
                "on_click": lambda e, partner=partner: edit_button_click_handler(e, partner),
                "class_name": "btn btn-secondary"
            }, "edit"),
        )
    ) for index, partner in enumerate(partners)]

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
                "placeholder": "Details",
                "on_change": lambda e: set_details(e["target"]["value"]),
                "value": details,
                "class_name": "form-control mb-2"
            }),
            html.input({
                "type": "text",
                "placeholder": "Direction",
                "on_change": lambda e: set_direction(e["target"]["value"]),
                "value": direction,
                "class_name": "form-control mb-2"
            }),
            html.input({
                "type": "text",
                "placeholder": "API Endpoint",
                "on_change": lambda e: set_api_endpoint(e["target"]["value"]),
                "value": api_endpoint,
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
