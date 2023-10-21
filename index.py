from fastapi import FastAPI
from reactpy.backend.fastapi import configure
from reactpy import component, use_state, use_effect
from components.cruds.views.rawMaterialsCrud import rawMaterials
from components.cruds.controllers.controllerPartners import router
from fastapi.staticfiles import StaticFiles
from api import getPartners, postPartner, deletePartner, updatePartner
from my_util import *
import asyncio
import reactpy

# components
from components.topbar import topbar
from components.login import login
from components.sidebar import sidebar


app = FastAPI()
# por buenas prácticas según se montan así los recursos en fastapi, yo digo que le hacen a la mamada nomás
# x2
# x3 xd

app.mount("/css", StaticFiles(directory="css"), name="css")
app.mount("/js", StaticFiles(directory="js"), name="js")



@component
def App():
    HERE = Path(__file__)
    DATA_PATH = HERE.parent / "data.json"

    partners, set_partners = use_state([])
    name, set_name = use_state("")
    details, set_details = use_state("")
    direction, set_direction = use_state("")
    api_endpoint, set_api_endpoint = use_state("")
    page, setpage = use_state(html.h1("Bienvenido"))

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
            updated_partner = {
                "name": name,
                "details": details,
                "direction": direction,
                "api_endpoint": api_endpoint,
                "id": partner_id
            }
            await updatePartner(partner_id, updated_partner)
            await fillItems()
            # set_partners(updated_partners)

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

    def int1():
        setpage(html.h1("Bienvenido1"))

    def int2():
        setpage(rawMaterials())

    return html.main(

        html.link({
            "href": "/css/sb-admin-2.min.css",
            "rel": "stylesheet"
        }),
        html.link({
            "href": "/css/all.min.css",
            "rel": "stylesheet",
            "type": "text/css"
        }),
        html.script(
            {"src": "js/jquery.min.js"}),
        html.script(
            {"src": "js/bootstrap.bundle.min.js"}),
        html.script(
            {"src": "js/jquery.easing.min.js"}),
        html.script(
            {"src": "js/sb-admin-2.min.js"}),
        html.script(
            {"src": "js/Chart.min.js"}),
        html.script(
            {"src": "js/chart-area-demo.js"}),
        html.script(
            {"src": "js/chart-pie-demo.js"}),
        html.div(
            html.meta({
                "charset": "utf-8"
            }),
            html.meta({
                "http-equiv": "X-UA-Compatible",
                "content": "IE=edge"
            }),
            html.meta({
                "name": "viewport",
                "content": "width=device-width, initial-scale=1, shrink-to-fit=no"
            }),
            html.meta({
                "name": "description",
                "content": ""
            }),
            html.meta({
                "name": "author",
                "content": ""
            }),
            html.title("PANEL ADMINISTRADOR"),
            html.link({
                "href": "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css",
                "rel": "stylesheet",
                "type": "text/css"
            }),
            html.link({
                "href": "https://fonts.googleapis.com/css?family=Nunito:200,200i,300,300i,400,400i,600,600i,700,700i,800,800i,900,900i",
                "rel": "stylesheet"
            }),

        ),
        html.div({"id": "wrapper"},
                sidebar,
                 topbar,

                 ),
            login,


    )


app.include_router(router)

configure(app, App)
