# -----------------------------------------------------
# components/kpis.py - KPI card creation logic
# -----------------------------------------------------
from dash import html

def generate_kpis(df):
    """Generate KPI cards for dashboard metrics with styled numeric values."""
    # ---- Compute Metrics ----
    total_orders = df['OrderCount'].sum()
    total_pieces = df['NumberOfPieces'].sum()
    total_revenue = df['TotalRevenue'].sum()
    avg_revenue_per_order = total_revenue / total_orders if total_orders else 0
    unique_customers = df['Customer'].nunique()

    # ---- Base Style ----
    base_style = {
        'color': '#FFFFFF',  # White text for dark background
        'padding': '25px',
        'borderRadius': '15px',
        'width': '18%',
        'textAlign': 'center',
        'boxShadow': '0px 4px 10px rgba(0, 0, 0, 0.4)',
        'margin': '10px',
        'display': 'inline-block',
        'verticalAlign': 'top',
    }

    # ---- Helper to make each card ----
    def make_card(title, value, bg):
        return html.Div([
            html.H4(title, style={
                'marginBottom': '8px',
                'fontWeight': '600',
                'fontSize': '1.1rem'
            }),
            html.H2(value, style={
                'margin': '0',
                'fontWeight': 'bold',
                'fontSize': '2rem',
                'color': '#FFFFFF'
            })
        ], style={**base_style, 'backgroundColor': bg})

    # ---- Return ONLY 5 KPI Cards ----
    return [
        make_card("Total Orders", f"{total_orders:,}", "#0074D9"),
        make_card("Total Pieces", f"{total_pieces:,}", "#2ECC40"),
        make_card("Total Revenue", f"${total_revenue:,.2f}", "#FF851B"),
        make_card("Avg Revenue/Order", f"${avg_revenue_per_order:,.2f}", "#B10DC9"),
        make_card("Unique Customers", f"{unique_customers:,}", "#39CCCC")
    ]
