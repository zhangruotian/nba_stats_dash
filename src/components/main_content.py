import dash_html_components as html
from dash import dcc

from .table import alpine_table
import plotly.graph_objs as go


def mainContent(dataframe=None) -> html.Div:
    children = [html.H5("Player Overview", className="text-center text-light mb-4")]
    if dataframe is not None and not dataframe.empty:
        children.append(alpine_table(dataframe))

    return html.Div(
        id="main-content",
        children=children,
        className="bg-dark"
    )


def create_time_series_plot(data):
    trace_ppg = go.Scatter(
        x=data['SEASON'],
        y=data['PPG'],
        mode='lines+markers',
        name='PPG',
        line=dict(color='cyan'),
        marker=dict(color='cyan', symbol='circle')
    )

    trace_rpg = go.Scatter(
        x=data['SEASON'],
        y=data['RPG'],
        mode='lines+markers',
        name='RPG',
        line=dict(color='magenta'),
        marker=dict(color='magenta', symbol='circle')
    )

    trace_apg = go.Scatter(
        x=data['SEASON'],
        y=data['APG'],
        mode='lines+markers',
        name='APG',
        line=dict(color='yellow'),
        marker=dict(color='yellow', symbol='circle')
    )

    layout = go.Layout(
        title='Player Performance Over Seasons',
        plot_bgcolor='#2F2F2F',  # Background color adjusted to better fit SLATE theme
        paper_bgcolor='#2F2F2F',  # Paper color adjusted to better fit SLATE theme
        font=dict(color='white'),  # Font color
        xaxis=dict(
            title='Season',
            gridcolor='gray',
            type='category',
            color='white',  # Color of x-axis labels
            titlefont=dict(color='white')
        ),
        yaxis=dict(
            title='Metrics',
            gridcolor='gray',
            color='white',  # Color of y-axis labels
            titlefont=dict(color='white')
        ),
        legend=dict(font=dict(color='white'))
    )

    return dcc.Graph(figure={'data': [trace_ppg, trace_rpg, trace_apg], 'layout': layout})




def mainContentplot(dataframe=None) -> html.Div:
    children = [html.H5("Career plots", className="text-center text-light mb-4")]

    if dataframe is not None and not dataframe.empty:
        graph = create_time_series_plot(dataframe)
        children.append(graph)

    return html.Div(
        id="main-content-plot",
        children=children,
        className="bg-dark"
    )
