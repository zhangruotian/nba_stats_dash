import dash_table

def alpine_table(dataframe) -> dash_table.DataTable:
    return dash_table.DataTable(
        data=dataframe.to_dict('records'),
        columns=[{'name': i, 'id': i} for i in dataframe.columns],

        # Styling the table
        style_table={
            'overflowX': 'auto',
            'border': 'thin lightgrey solid'
        },
        style_header={
            'backgroundColor': 'rgb(50, 50, 50)',
            'fontWeight': 'bold',
            'color': 'white',
            'textAlign': 'center'  # Center text in header
        },
        style_cell={
            'backgroundColor': 'rgb(60, 60, 60)',
            'color': 'white',
            'border': '1px solid grey',
            'textAlign': 'center'  # Center text in cells
        },
        style_data_conditional=[
            {
                'if': {'row_index': 'odd'},
                'backgroundColor': 'rgb(50, 50, 50)'
            }
        ]
    )
