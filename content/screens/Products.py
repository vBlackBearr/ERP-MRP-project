from reactpy import component
from reactpy.core.hooks import use_context

# content
from content.cruds.views.productsCrud import ProductsCrud
from content.screens._base import Base


@component
def Products(context):
    context_value = use_context(context)

    return Base((
        ProductsCrud()
    ), context_value)
