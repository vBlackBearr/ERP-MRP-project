from reactpy import component, html, run
from reactpy_router import route, simple
from components.cruds.views.partnersCrud import partners

@component
def root():
    return simple.router(
        route("/raw", partners()),
        route("/prueba", html.h1("Prueba page 🏠")),
        route("/kk", html.h1("kk Page 🏠")),
        route("*", html.h1("Missing Link 🔗‍💥")),
    )


run(root)
