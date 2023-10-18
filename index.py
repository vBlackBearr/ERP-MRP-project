from fastapi import FastAPI
from reactpy.backend.fastapi import configure
from reactpy import component, html, use_state, use_effect
from rawMaterialsCrud import rawMaterials

import asyncio
from controllerPartners import router
import reactpy
from api import getPartners, postPartner, deletePartner, updatePartner

bootstrap_css = html.link({
    "rel": "stylesheet",
    "href": "/_reactpy/assests/bootstrap.min.css"
})


@component
def App():
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

    return html.div(
        {
            "style": {
                "padding": "3rem",
            }
        },
        bootstrap_css,
        html.link({
            "href": "css/sb-admin-2.min.css",
            "rel": "stylesheet"
        }),
        html.link({
            "href": "css/all.min.css",
            "rel": "stylesheet",
            "type": "text/css"
        }),
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
                "href": "css/all.min.css",
                "rel": "stylesheet",
                "type": "text/css"
            }),
            html.link({
                "href": "https://fonts.googleapis.com/css?family=Nunito:200,200i,300,300i,400,400i,600,600i,700,700i,800,800i,900,900i",
                "rel": "stylesheet"
            }),


        ),
        html.div({"id": "wrapper"},
                 #sidebar
                 html.ul({
                     "class": "navbar-nav bg-gradient-primary sidebar sidebar-dark accordion",
                     "id": "accordionSidebar"
                 },
                     # Sidebar - Brand
                     html.a({
                         "class": "sidebar-brand d-flex align-items-center justify-content-center",
                         "href": "index.html"
                     },
                         html.div({
                             "class": "sidebar-brand-icon rotate-n-15"
                         },
                             html.i({
                                 "class": "fas fa-laugh-wink"
                             })
                         ),
                         html.div({
                             "class": "sidebar-brand-text mx-3"
                         },
                             "ADMINISTRADOR",
                             html.sup()
                         )
                     ),

                     # Divider
                     html.hr({
                         "class": "sidebar-divider my-0"
                     }),

                     # Nav Item - Dashboard
                     html.li({
                         "class": "nav-item active"
                     },
                         html.a({
                             "class": "nav-link",
                             "href": "index.html"
                         },
                             html.i({
                                 "class": "fas fa-fw fa-tachometer-alt"
                             }),
                             "Dashboard"
                         )
                     ),

                     # Divider
                     html.hr({
                         "class": "sidebar-divider"
                     }),

                     # Heading - Interface
                     html.div({
                         "class": "sidebar-heading"
                     },
                         "Interface"
                     ),

                     # Nav Item - Pages Collapse Menu (TIER1)
                     html.li({
                         "class": "nav-item"
                     },
                         html.a({
                             "class": "nav-link collapsed",
                             "href": "#",
                             "data-toggle": "collapse",
                             "data-target": "#collapseTwo",
                             "aria-expanded": "true",
                             "aria-controls": "collapseTwo"
                         },
                             html.i({
                                 "class": "fas fa-fw fa-cog"
                             }),
                             "TIER1"
                         ),
                         html.div({
                             "class": "collapse",
                             "id": "collapseTwo",
                             "aria-labelledby": "headingTwo",
                             "data-parent": "#accordionSidebar"
                         },
                             html.div({
                                 "class": "bg-white py-2 collapse-inner rounded"
                             },
                                 html.h6({
                                     "class": "collapse-header"
                                 },
                                     "Custom Components:"
                                 ),
                                 html.a({
                                     "class": "collapse-item",
                                     "href": "buttons.html"
                                 },
                                     "Compra"
                                 ),
                                 html.a({
                                     "class": "collapse-item",
                                     "href": "cards.html"
                                 },
                                     "Pedidos"
                                 )
                             )
                         )
                     ),

                     # Nav Item - Pages Collapse Menu (TIER2)
                     html.li({
                         "class": "nav-item"
                     },
                         html.a({
                             "class": "nav-link collapsed",
                             "href": "#",
                             "data-toggle": "collapse",
                             "data-target": "#collapseUtilities",
                             "aria-expanded": "true",
                             "aria-controls": "collapseUtilities"
                         },
                             html.i({
                                 "class": "fas fa-fw fa-wrench"
                             }),
                             "TIER2"
                         ),
                         html.div({
                             "class": "collapse",
                             "id": "collapseUtilities",
                             "aria-labelledby": "headingUtilities",
                             "data-parent": "#accordionSidebar"
                         },
                             html.div({
                                 "class": "bg-white py-2 collapse-inner rounded"
                             },
                                 html.h6({
                                     "class": "collapse-header"
                                 },
                                     "Custom Utilities:"
                                 ),
                                 html.a({
                                     "class": "collapse-item",
                                     "href": "utilities-color.html"
                                 },
                                     "Colors"
                                 ),
                                 html.a({
                                     "class": "collapse-item",
                                     "href": "utilities-border.html"
                                 },
                                     "Borders"
                                 ),
                                 html.a({
                                     "class": "collapse-item",
                                     "href": "utilities-animation.html"
                                 },
                                     "Animations"
                                 ),
                                 html.a({
                                     "class": "collapse-item",
                                     "href": "utilities-other.html"
                                 },
                                     "Other"
                                 )
                             )
                         )
                     ),

                     # Nav Item - Pages Collapse Menu (TIER3)
                     html.li({
                         "class": "nav-item"
                     },
                         html.a({
                             "class": "nav-link collapsed",
                             "href": "#",
                             "data-toggle": "collapse",
                             "data-target": "#collapseTIER3"
                         },
                             html.i({
                                 "class": "fas fa-fw fa-cog"
                             }),
                             "TIER3"
                         ),
                         html.div({
                             "class": "collapse",
                             "id": "collapseTIER3",
                             "aria-labelledby": "headingTwo",
                             "data-parent": "#accordionSidebar"
                         },
                             html.div({
                                 "class": "bg-white py-2 collapse-inner rounded"
                             },
                                 html.h6({
                                     "class": "collapse-header"
                                 },
                                     "Custom Components:"
                                 ),
                                 html.a({
                                     "class": "collapse-item",
                                     "href": "buttons.html"
                                 },
                                     "Buttons"
                                 ),
                                 html.a({
                                     "class": "collapse-item",
                                     "href": "cards.html"
                                 },
                                     "Cards"
                                 )
                             )
                         )
                     ),

                     # Nav Item - Pages Collapse Menu (LOGISTICA)
                     html.li({
                         "class": "nav-item"
                     },
                         html.a({
                             "class": "nav-link collapsed",
                             "href": "#",
                             "data-toggle": "collapse",
                             "data-target": "#collapseLOGISTICA"
                         },
                             html.i({
                                 "class": "fas fa-fw fa-cog"
                             }),
                             "LOGISTICA"
                         ),
                         html.div({
                             "class": "collapse",
                             "id": "collapseLOGISTICA",
                             "aria-labelledby": "headingTwo",
                             "data-parent": "#accordionSidebar"
                         },
                             html.div({
                                 "class": "bg-white py-2 collapse-inner rounded"
                             },
                                 html.h6({
                                     "class": "collapse-header"
                                 },
                                     "Custom Components:"
                                 ),
                                 html.a({
                                     "class": "collapse-item",
                                     "href": "buttons.html"
                                 },
                                     "Buttons"
                                 ),
                                 html.a({
                                     "class": "collapse-item",
                                     "href": "cards.html"
                                 },
                                     "Cards"
                                 )
                             )
                         )
                     ),

                     # Divider
                     html.hr({
                         "class": "sidebar-divider"
                     }),

                     # Heading - Addons
                     html.div({
                         "class": "sidebar-heading"
                     },
                         "Addons"
                     )
                 )
                 )

    )


app = FastAPI()

app.include_router(router)

configure(app, App)
