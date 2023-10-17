
def partners():
    return html.div(html.form(
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
    ))