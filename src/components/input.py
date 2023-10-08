# input.py
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc


def player_input() -> html.Div:
    return html.Div(
        [
            dbc.Row(
                dbc.Col(html.Label('Enter Player Name:', className="text-light"))
            ),
            dbc.Row(
                dbc.Col(
                    dcc.Input(
                        id='player-name-input',
                        type='text',
                        placeholder='Stephen Curry',
                        className="input-dark",
                        style={'width': '100%', 'height': '38px'}  # Set the height here
                    )
                )
            )
        ],
        className="border-right px-4 bg-dark mb-3"
    )

def player_input_plot() -> html.Div:
    return html.Div(
        [
            dbc.Row(
                dbc.Col(html.Label('Enter Player Name:', className="text-light"))
            ),
            dbc.Row(
                dbc.Col(
                    dcc.Input(
                        id='player-name-input-plot',
                        type='text',
                        placeholder='Stephen Curry',
                        className="input-dark",
                        style={'width': '100%', 'height': '38px'}  # Set the height here
                    )
                )
            )
        ],
        className="border-right px-4 bg-dark mb-3"
    )