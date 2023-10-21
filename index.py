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

#routers
from content.cruds.controllers.controllerPartners import router

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
        route("/kk", html.h1("kk Page 🏠")),
        route("*", html.h1("Missing Link 🔗‍💥"))
    )


app.include_router(router)

configure(app, App)
