import dash_bootstrap_components as dbc


def submit_btn() -> dbc.Button:
    return dbc.Button('Submit', id='submit-button', color='primary', className='mt-3',
                      style={'width': '30%', 'height': '50px', 'marginLeft': '25px'})

def clear_btn() -> dbc.Button:
    return dbc.Button('Clear', id='clear-button', color='primary', className='mt-3', style={'width': '30%', 'height': '50px', 'marginLeft': '25px'})

def submit_btn_plot() -> dbc.Button:
    return dbc.Button('Submit', id='submit-button_plot', color='primary', className='mt-3',
                      style={'width': '30%', 'height': '50px', 'marginLeft': '25px'})

def clear_btn_plot() -> dbc.Button:
    return dbc.Button('Clear', id='clear-button_plot', color='primary', className='mt-3', style={'width': '30%', 'height': '50px', 'marginLeft': '25px'})