import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash import html, dcc
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate

from components import header, sidebar, mainContent, player_input, submit_btn, clear_btn, player_input_plot, \
    submit_btn_plot, clear_btn_plot, mainContentplot
from nba_player_data import FetchPlayerData, Player


def main() -> None:
    DARK_THEME = dbc.themes.SLATE

    app = dash.Dash(__name__, external_stylesheets=[DARK_THEME])
    app.config.suppress_callback_exceptions = True

    data_fetcher = FetchPlayerData()

    app.layout = html.Div([
        dcc.Location(id='url', refresh=False),
        html.Div(id='page-content')
    ])

    def main_dashboard():
        return dbc.Container(
            [
                dbc.Row(  # This row contains the header and the button
                    [
                        dbc.Col(  # Column for the header
                            header(),
                            width={"size": 10, "order": 1}  # Adjust size as necessary
                        ),
                        dbc.Col(  # Column for the button
                            dbc.Button(
                                "Go to Time Series Analysis",
                                href="/timeseries",
                                className="mr-1 mt-1"
                            ),
                            width={"size": 2, "order": 2},  # Adjust size as necessary
                            className="d-flex justify-content-end align-items-center"
                        )
                    ],
                    className="mb-3"  # Margin at the bottom for spacing
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                player_input(),
                                html.Div(id='feedback-div', children='', style={'color': 'red', 'margin': '10px 0'}),
                                sidebar(),
                                submit_btn(),
                                clear_btn()
                            ],
                            width=3
                        ),
                        dbc.Col(mainContent(), width=9)
                    ]
                )
            ],
            fluid=True,
            className="bg-dark",
            style={"minHeight": "100vh"}
        )

    def time_series_page():
        return dbc.Container(
            [
                dbc.Row(  # This row contains the header and the button
                    [
                        dbc.Col(  # Column for the header
                            header('Time Series Analysis of Player Metrics'),
                            width={"size": 10, "order": 1}  # Adjust size as necessary
                        ),
                        dbc.Col(  # Column for the button
                            dbc.Button(
                                "Back to Dashboard",
                                href="/",
                                className="mr-1 mt-1"
                            ),
                            width={"size": 2, "order": 2},  # Adjust size as necessary
                            className="d-flex justify-content-end align-items-center"
                        )
                    ],
                    className="mb-3"  # Margin at the bottom for spacing
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                player_input_plot(),
                                html.Div(id='feedback-div-plot', children='',
                                         style={'color': 'red', 'margin': '10px 0'}),
                                submit_btn_plot(),
                                clear_btn_plot()
                            ],
                            width=3
                        ),
                        dbc.Col(mainContentplot(), width=9)
                    ]
                )
            ],
            fluid=True,
            className="bg-dark",
            style={"minHeight": "100vh"}
        )

    @app.callback(Output('page-content', 'children'),
                  [Input('url', 'pathname')])
    def display_page(pathname):
        if pathname == '/timeseries':
            return time_series_page()
        else:
            return main_dashboard()

    @app.callback(
        Output('main-content', 'children'),
        [Input('player-name-input', 'value'),
         Input('season-dropdown', 'value'),
         Input('submit-button', 'n_clicks')]
    )
    def click_submit(player_name, selected_seasons, n_clicks):
        # print(f"Callback triggered with player name: {player_name}")

        if n_clicks is None:
            return dash.no_update

        try:
            career_data = data_fetcher.get_career_stats_by_full_name(player_name)
            player_obj = Player(career_data)
            stats_df = player_obj.season_average_stats(selected_seasons)

            return mainContent(stats_df).children
        except Exception as e:
            return html.Div(f"An error occurred: {str(e)}", style={"color": "red"})

    @app.callback(
        [Output("season-dropdown", "options"),
         Output('feedback-div', 'children')],
        [Input("player-name-input", "value")]
    )
    def update_seasons_for_name_input(player_name):
        if not player_name:
            return [], ''

        career_data = data_fetcher.get_career_stats_by_full_name(player_name)
        if career_data.empty:
            return [], 'No player found with this name'
        options = [{'label': 'All Seasons', 'value': 'all'}]
        available_seasons = career_data["SEASON_ID"].unique().tolist()
        options.extend([{'label': season, 'value': season} for season in available_seasons])
        return options, ''

    @app.callback(
        Output('feedback-div-plot', 'children'),
        [Input("player-name-input-plot", "value")]
    )
    def fetch_player_feedback(player_name):
        if not player_name:
            return ''

        career_data = data_fetcher.get_career_stats_by_full_name(player_name)
        if career_data.empty:
            return 'No player found with this name'
        return ''

    @app.callback(
        [Output("player-name-input", "value"),
         Output("season-dropdown", "value")],
        [Input("clear-button", "n_clicks")]
    )
    def clear_inputs(n):
        if n is None:
            raise PreventUpdate

        return "", []


    @app.callback(
        Output('main-content-plot', 'children'),
        [Input("player-name-input-plot", "value"),
         Input("submit-button_plot", "n_clicks")]
    )
    def update_plot(player_name, n_clicks):
        if n_clicks is None:
            return dash.no_update
        if not player_name:
            return mainContentplot(None)
        career_data = data_fetcher.get_career_stats_by_full_name(player_name)
        player_obj = Player(career_data)
        return mainContentplot(player_obj.career_data_updated[['SEASON', 'PPG', 'RPG', 'APG']]).children



    @app.callback(
        Output("player-name-input-plot", "value"),
        [Input("clear-button_plot", "n_clicks")]
    )
    def clear_inputs(n):
        if n is None:
            raise PreventUpdate

        return ""

    app.run_server(debug=True, host='0.0.0.0')


if __name__ == '__main__':
    main()
