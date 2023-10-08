import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc


def sidebar(available_seasons=None) -> html.Div:
    if available_seasons is None:
        available_seasons = []

    options = [{'label': season, 'value': season} for season in available_seasons]

    return html.Div(
        [
            dbc.Row([
                dbc.Col(
                    [
                        html.Label("Select Season", className="text-light"),
                        dcc.Dropdown(
                            id="season-dropdown",
                            options=options,
                            value=None,
                            multi=True,
                            className="dropdown-dark",
                            style={'width': '100%', 'height': '38px'}
                        )
                    ]
                )
            ]),
            html.Br()
        ],
        className="border-right px-4 bg-dark mb-3"
    )
