from reactpy import component, html, use_state, use_effect



def partners():

    name, set_name = use_state("")
    details, set_details = use_state("")
    direction, set_direction = use_state("")
    api_endpoint, set_api_endpoint = use_state("")
    page, setpage = use_state(html.h1("Bienvenido"))



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