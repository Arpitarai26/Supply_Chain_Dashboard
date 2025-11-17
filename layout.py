# -----------------------------------------------------
# layout.py - defines dashboard layout & theme toggle
# -----------------------------------------------------
from dash import html, dcc

def create_layout(df):
    return html.Div([
        html.H1("📊 Business Performance Dashboard", style={'textAlign': 'center'}),

        html.Div([
            html.Label("Toggle Theme:", style={'marginRight': '10px'}),
            dcc.RadioItems(
                id='theme-toggle',
                options=[
                    {'label': '🌙 Dark', 'value': 'dark'},
                    {'label': '☀️ Light', 'value': 'light'}
                ],
                value='dark',
                labelStyle={'display': 'inline-block', 'marginRight': '15px'}
            )
        ], style={'textAlign': 'center', 'marginBottom': '20px'}),

        html.Div([
            html.Div([
                html.Label("Select Customer"),
                dcc.Dropdown(
                    id='customer-dropdown',
                    options=[{'label': c, 'value': c} for c in sorted(df["Customer"].unique())],
                    multi=True, placeholder="Choose customers"
                )
            ], style={'width': '30%', 'display': 'inline-block', 'padding': '10px'}),

            html.Div([
                html.Label("Select Location"),
                dcc.Dropdown(
                    id='location-dropdown',
                    options=[{'label': l, 'value': l} for l in sorted(df["Location"].unique())],
                    multi=True, placeholder="Choose locations"
                )
            ], style={'width': '30%', 'display': 'inline-block', 'padding': '10px'}),

            html.Div([
                html.Label("Select Business Type"),
                dcc.Dropdown(
                    id='business-dropdown',
                    options=[{'label': b, 'value': b} for b in sorted(df["BusinessType"].unique())],
                    multi=True, placeholder="Choose business types"
                )
            ], style={'width': '30%', 'display': 'inline-block', 'padding': '10px'})
        ]),

        html.Br(),
        html.Div(id='kpi-cards', style={'display': 'flex', 'justifyContent': 'space-around', 'flexWrap': 'wrap'}),
        html.Br(),

        html.Div([
            dcc.Graph(id='revenue-bar'),
            dcc.Graph(id='order-trend'),
            dcc.Graph(id='business-type-bar'),
            dcc.Graph(id='us-map')
        ], style={'padding': '20px'})
    ])
