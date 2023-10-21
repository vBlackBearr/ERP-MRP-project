
from reactpy import html

topbar = html.nav({
    "class": "navbar navbar-expand navbar-light bg-white topbar mb-4 static-top shadow"
}, [
    # Sidebar Toggle (Topbar)
    html.button({
        "id": "sidebarToggleTop",
        "class": "btn btn-link d-md-none rounded-circle mr-3"
    }, html.i({
        "class": "fa fa-bars"
    })),

    # Topbar Search
    html.form({
        "class": "d-none d-sm-inline-block form-inline mr-auto ml-md-3 my-2 my-md-0 mw-100 navbar-search"
    }, [
        html.div({
            "class": "input-group"
        }, [
            html.input({
                "type": "text",
                "class": "form-control bg-light border-0 small",
                "placeholder": "Search for...",
                "aria-label": "Search",
                "aria-describedby": "basic-addon2"
            }),
            html.div({
                "class": "input-group-append"
            }, html.button({
                "class": "btn btn-primary",
                "type": "button"
            }, html.i({
                "class": "fas fa-search fa-sm"
            })))

        ])
    ]),

    # Topbar Navbar
    html.ul({
        "class": "navbar-nav ml-auto"
    }, [

        # Nav Item - Search Dropdown (Visible Only XS)
        html.li({
            "class": "nav-item dropdown no-arrow d-sm-none"
        }, [
            html.a({
                "class": "nav-link dropdown-toggle",
                "href": "#",
                "id": "searchDropdown",
                "role": "button",
                "data-toggle": "dropdown",
                "aria-haspopup": "true",
                "aria-expanded": "false"
            }, html.i({
                "class": "fas fa-search fa-fw"
            })),
            html.div({
                "class": "dropdown-menu dropdown-menu-right p-3 shadow animated--grow-in",
                "aria-labelledby": "searchDropdown"
            }, [
                html.form({
                    "class": "form-inline mr-auto w-100 navbar-search"
                }, [
                    html.div({
                        "class": "input-group"
                    }, [
                        html.input({
                            "type": "text",
                            "class": "form-control bg-light border-0 small",
                            "placeholder": "Search for...",
                            "aria-label": "Search",
                            "aria-describedby": "basic-addon2"
                        }),
                        html.div({
                            "class": "input-group-append"
                        }, html.button({
                            "class": "btn btn-primary",
                            "type": "button"
                        }, html.i({
                            "class": "fas fa-search fa-sm"
                        })))
                    ])
                ])
            ])
        ]),

        # Nav Item - Alerts
        html.li({
            "class": "nav-item dropdown no-arrow mx-1"
        }, [
            html.a({
                "class": "nav-link dropdown-toggle",
                "href": "#",
                "id": "alertsDropdown",
                "role": "button",
                "data-toggle": "dropdown",
                "aria-haspopup": "true",
                "aria-expanded": "false"
            }, [
                html.i({
                    "class": "fas fa-bell fa-fw"
                }),
                # Counter - Alerts
                html.span({
                    "class": "badge badge-danger badge-counter"
                }, "3+")
            ]),
            html.div({
                "class": "dropdown-list dropdown-menu dropdown-menu-right shadow animated--grow-in",
                "aria-labelledby": "alertsDropdown"
            }, [
                html.h6({
                    "class": "dropdown-header"
                }, "Alerts Center"),
                html.a({
                    "class": "dropdown-item d-flex align-items-center",
                    "href": "#"
                }, [
                    html.div({
                        "class": "mr-3"
                    }, [
                        html.div({
                            "class": "icon-circle bg-primary"
                        }, html.i({
                            "class": "fas fa-file-alt text-white"
                        }))
                    ]),
                    html.div({}, [
                        html.div({
                            "class": "small text-gray-500"
                        }, "December 12, 2019"),
                        html.span({
                            "class": "font-weight-bold"
                        }, "A new monthly report is ready to download!")
                    ])
                ]),
                html.a({
                    "class": "dropdown-item d-flex align-items-center",
                    "href": "#"
                }, [
                    html.div({
                        "class": "mr-3"
                    }, [
                        html.div({
                            "class": "icon-circle bg-success"
                        }, html.i({
                            "class": "fas fa-donate text-white"
                        }))
                    ]),
                    html.div({}, [
                        html.div({
                            "class": "small text-gray-500"
                        }, "December 7, 2019"),
                        "$290.29 has been deposited into your account!"
                    ])
                ]),
                html.a({
                    "class": "dropdown-item d-flex align-items-center",
                    "href": "#"
                }, [
                    html.div({
                        "class": "mr-3"
                    }, [
                        html.div({
                            "class": "icon-circle bg-warning"
                        }, html.i({
                            "class": "fas fa-exclamation-triangle text-white"
                        }))
                    ]),
                    html.div({}, [
                        html.div({
                            "class": "small text-gray-500"
                        }, "December 2, 2019"),
                        "Spending Alert: We've noticed unusually high spending for your account."
                    ])
                ]),
                html.a({
                    "class": "dropdown-item text-center small text-gray-500",
                    "href": "#"
                }, "Show All Alerts")
            ])
        ]),

        # Nav Item - Messages
        html.li({
            "class": "nav-item dropdown no-arrow mx-1"
        }, [
            html.a({
                "class": "nav-link dropdown-toggle",
                "href": "#",
                "id": "messagesDropdown",
                "role": "button",
                "data-toggle": "dropdown",
                "aria-haspopup": "true",
                "aria-expanded": "false"
            }, [
                html.i({
                    "class": "fas fa-envelope fa-fw"
                }),
                # Counter - Messages
                html.span({
                    "class": "badge badge-danger badge-counter"
                }, "7")
            ]),
            html.div({
                "class": "dropdown-list dropdown-menu dropdown-menu-right shadow animated--grow-in",
                "aria-labelledby": "messagesDropdown"
            }, [
                html.h6({
                    "class": "dropdown-header"
                }, "Message Center"),
                html.a({
                    "class": "dropdown-item d-flex align-items-center",
                    "href": "#"
                }, [
                    html.div({
                        "class": "dropdown-list-image mr-3"
                    }, [
                        html.img({
                            "class": "rounded-circle",
                            "src": "img/undraw_profile_1.svg",
                            "alt": "..."
                        }),
                        html.div({
                            "class": "status-indicator bg-success"
                        })
                    ]),
                    html.div({
                        "class": "font-weight-bold"
                    }, [
                        html.div({
                            "class": "text-truncate"
                        }, "Hi there! I am wondering if you can help me with a problem I've been having."),
                        html.div({
                            "class": "small text-gray-500"
                        }, "Emily Fowler · 58m")
                    ])
                ]),
                html.a({
                    "class": "dropdown-item d-flex align-items-center",
                    "href": "#"
                }, [
                    html.div({
                        "class": "dropdown-list-image mr-3"
                    }, [
                        html.img({
                            "class": "rounded-circle",
                            "src": "img/undraw_profile_2.svg",
                            "alt": "..."
                        }),
                        html.div({
                            "class": "status-indicator"
                        })
                    ]),
                    html.div({}, [
                        html.div({
                            "class": "text-truncate"
                        }, "I have the photos that you ordered last month, how would you like them sent to you?"),
                        html.div({
                            "class": "small text-gray-500"
                        }, "Jae Chun · 1d")
                    ])
                ]),
                html.a({
                    "class": "dropdown-item d-flex align-items-center",
                    "href": "#"
                }, [
                    html.div({
                        "class": "dropdown-list-image mr-3"
                    }, [
                        html.img({
                            "class": "rounded-circle",
                            "src": "img/undraw_profile_3.svg",
                            "alt": "..."
                        }),
                        html.div({
                            "class": "status-indicator bg-warning"
                        })
                    ]),
                    html.div({}, [
                        html.div({
                            "class": "text-truncate"
                        }, "Last month's report looks great, I am very happy with the progress so far, keep up the good work!"),
                        html.div({
                            "class": "small text-gray-500"
                        }, "Morgan Alvarez · 2d")
                    ])
                ]),
                html.a({
                    "class": "dropdown-item d-flex align-items-center",
                    "href": "#"
                }, [
                    html.div({
                        "class": "dropdown-list-image mr-3"
                    }, [
                        html.img({
                            "class": "rounded-circle",
                            "src": "https://source.unsplash.com/Mv9hjnEUHR4/60x60",
                            "alt": "..."
                        }),
                        html.div({
                            "class": "status-indicator bg-success"
                        })
                    ]),
                    html.div({}, [
                        html.div({
                            "class": "text-truncate"
                        }, "Am I a good boy? The reason I ask is because someone told me that people say this to all dogs, even if they aren't good..."),
                        html.div({
                            "class": "small text-gray-500"
                        }, "Chicken the Dog · 2w")
                    ])
                ]),
                html.a({
                    "class": "dropdown-item text-center small text-gray-500",
                    "href": "#"
                }, "Read More Messages")
            ])
        ]),

        html.div({
            "class": "topbar-divider d-none d-sm-block"
        }),

        # Nav Item - User Information
        html.li({
            "class": "nav-item dropdown no-arrow"
        }, [
            html.a({
                "class": "nav-link dropdown-toggle",
                "href": "#",
                "id": "userDropdown",
                "role": "button",
                "data-toggle": "dropdown",
                "aria-haspopup": "true",
                "aria-expanded": "false"
            }, [
                html.span({
                    "class": "mr-2 d-none d-lg-inline text-gray-600 small"
                }, "Douglas McGee"),
                html.img({
                    "class": "img-profile rounded-circle",
                    "src": "img/undraw_profile.svg"
                })
            ]),
            html.div({
                "class": "dropdown-menu dropdown-menu-right shadow animated--grow-in",
                "aria-labelledby": "userDropdown"
            }, [
                html.a({
                    "class": "dropdown-item",
                    "href": "#"
                }, [
                    html.i({
                        "class": "fas fa-user fa-sm fa-fw mr-2 text-gray-400"
                    }),
                    "Profile"
                ]),
                html.a({
                    "class": "dropdown-item",
                    "href": "#"
                }, [
                    html.i({
                        "class": "fas fa-cogs fa-sm fa-fw mr-2 text-gray-400"
                    }),
                    "Settings"
                ]),
                html.a({
                    "class": "dropdown-item",
                    "href": "#"
                }, [
                    html.i({
                        "class": "fas fa-list fa-sm fa-fw mr-2 text-gray-400"
                    }),
                    "Activity Log"
                ]),
                html.div({
                    "class": "dropdown-divider"
                }),
                html.a({
                    "class": "dropdown-item",
                    "href": "#",
                    "data-toggle": "modal",
                    "data-target": "#logoutModal"
                }, [
                    html.i({
                        "class": "fas fa-sign-out-alt fa-sm fa-fw mr-2 text-gray-400"
                    }),
                    "Logout"
                ])
            ])
        ])
    ])
])
