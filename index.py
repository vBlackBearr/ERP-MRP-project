from fastapi import FastAPI
from reactpy.backend.fastapi import configure
from reactpy import component, html
from fastapi.staticfiles import StaticFiles
from content.base.head import head
from reactpy.core.hooks import create_context
from reactpy_router import route, simple


# content
from content.screens.index import Index
from content.screens.Partners import Partners
from content.screens.RawMaterials import RawMaterials
from content.screens.Products import Products
from content.screens.Sales import Sales

#routers
from content.cruds.controllers.controllerPartners import router as router_partners
from content.cruds.controllers.controllerRawMaterials import router as router_raw_materials
from content.cruds.controllers.controllerProducts import router as router_products
from content.cruds.controllers.controllerSales import router as router_sales


app = FastAPI()
# por buenas prácticas según se montan así los recursos en fastapi, yo digo que le hacen a la mamada nomás
# x2
# x3 xd

app.mount("/content", StaticFiles(directory="content"), name="content")


@component
def App():
    context = create_context("value")

    return simple.router(
        route("/", Index(context)),
        route("/partners", Partners(context)),
        route("/raw_materials", RawMaterials(context)),
        route("/products", Products(context)),
        route("/sales", Sales(context)),
        route("*", html.h1("Missing Link 🔗‍💥"))
    )


app.include_router(router_partners)
app.include_router(router_raw_materials)
app.include_router(router_products)
app.include_router(router_sales)


configure(app, App)
