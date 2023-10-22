from reactpy import html

sidebar = html.ul({
    "class": "navbar-nav bg-gradient-primary sidebar sidebar-dark accordion",
    "id": "accordionSidebar"
},
    # Sidebar - Brand
    html.a({
        "class": "sidebar-brand d-flex align-items-center justify-content-center",
        "href": "/"
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
            "href": "/"
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

    # # Heading - Addons
    # html.div({
    #     "class": "sidebar-heading"
    # },
    #     "Addons"
    # ),
    #
    # html.li({
    #     "class": "nav-item active"
    # },
    #     html.a({
    #         "class": "nav-link",
    #         "href": "partners"
    #     },
    #         html.i({
    #             "class": "fas fa-fw fa-table"
    #         }),
    #         html.span("Partners")
    #     ),
    #
    # ),
    #
    # html.li({
    #     "class": "nav-item active"
    # },
    #     html.a({
    #         "class": "nav-link",
    #         "href": "raw_materials"
    #     },
    #         html.i({
    #             "class": "fas fa-fw fa-table"
    #         }),
    #         html.span("Raw Materials")
    #     ),
    #
    # ),
    #
    # # Divider
    # html.hr({
    #     "class": "sidebar-divider my-0"
    # }),

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
            "Inventario"
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
                    "href": "products"
                },
                    "Productos"
                ),
                html.a({
                    "class": "collapse-item",
                    "href": "raw_materials"
                },
                    "Raw Materials"
                )
            )
        )
    ),

    html.li({
            "class": "nav-item active"
        },
            html.a({
                "class": "nav-link",
                "href": "sales"
            },
                html.i({
                    "class": "fas fa-fw fa-table"
                }),
                html.span("Ventas")
            ),

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
            "Compras"
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

)
