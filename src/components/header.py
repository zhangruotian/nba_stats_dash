import dash_html_components as html
import dash_bootstrap_components as dbc


def header(title="NBA Player Stats Dashboard") -> dbc.Row:
    return dbc.Row(
        dbc.Col(
            html.Div(
                [
                    html.H1(title, className="text-center text-light d-inline-block p-3",
                            style={"fontSize": "50px"})
                    # html.Img(src='/assets/jordan.jpg', height="80px", className="d-inline-block align-top ml-3"),

                ],
                className="text-center"
            ),
            width=12
        ),
        align="center"
    )
