# -----------------------------------------------------
# callbacks.py - connects UI with graph & KPI logic + ML model + theme switching
# -----------------------------------------------------
import importlib
from dash import Input, Output, html
from components.kpis import generate_kpis
from components.graphs.revenue_bar import revenue_by_location
from components.graphs.revenue_trend import revenue_over_time
from components.graphs.revenue_business_type import revenue_by_business_type
from components.graphs.us_map import revenue_us_map


def register_callbacks(app, df):
    @app.callback(
        [
            Output('revenue-bar', 'figure'),
            Output('order-trend', 'figure'),
            Output('business-type-bar', 'figure'),
            Output('us-map', 'figure'),
            Output('kpi-cards', 'children'),
        ],
        [
            Input('customer-dropdown', 'value'),
            Input('location-dropdown', 'value'),
            Input('business-dropdown', 'value'),
            Input('theme-toggle', 'value'),
        ]
    )
    def update_dashboard(selected_customers, selected_locations, selected_business, theme):
        # ---- Safe theme loading ----
        try:
            theme_module = importlib.import_module(f"components.colors_{theme}")
        except Exception:
            theme_module = importlib.import_module("components.colors_dark")

        CUSTOMER_COLORS = getattr(theme_module, "CUSTOMER_COLORS", {})

        # Safe defaults
        _DEFAULT_PALETTE = {
            "primary": "#00BCD4",
            "secondary": "#FFC107",
            "background": "#121212",
            "plot_bg": "#181818",
            "text": "#E0E0E0",
            "grid": "rgba(255,255,255,0.1)"
        }
        PALETTE = {**_DEFAULT_PALETTE, **getattr(theme_module, "PALETTE", {})}

        # ---- Filter Data ----
        filtered_df = df.copy()
        if selected_customers:
            filtered_df = filtered_df[filtered_df['Customer'].isin(selected_customers)]
        if selected_locations:
            filtered_df = filtered_df[filtered_df['Location'].isin(selected_locations)]
        if selected_business:
            filtered_df = filtered_df[filtered_df['BusinessType'].isin(selected_business)]

        # ---- KPIs ----
        kpi_cards = generate_kpis(filtered_df)

       

        return (
            revenue_by_location(filtered_df, CUSTOMER_COLORS, PALETTE),
            revenue_over_time(filtered_df, PALETTE),
            revenue_by_business_type(filtered_df, PALETTE),
            revenue_us_map(filtered_df, PALETTE),
            kpi_cards
        )
