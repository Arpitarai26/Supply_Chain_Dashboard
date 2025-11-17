import plotly.express as px

def revenue_by_location(df, CUSTOMER_COLORS, PALETTE):
    if df is None or df.empty:
        return {}

    bg = str(PALETTE.get('background', '#121212')).lower()
    dark_mode = bg in ('#121212', '#181818', '#000000', 'black')

    fig = px.bar(
        df, x='Location', y='TotalRevenue',
        color='Customer', color_discrete_map=CUSTOMER_COLORS,
        barmode='group', title="Revenue by Location"
    )
    fig.update_layout(
        template='plotly_dark' if dark_mode else 'plotly_white',
        plot_bgcolor=PALETTE.get('plot_bg', '#181818'),
        paper_bgcolor=PALETTE.get('plot_bg', '#181818'),
        font_color=PALETTE.get('text', '#E0E0E0'),
        title_x=0.5,
        xaxis=dict(showgrid=True, gridcolor=PALETTE.get('grid', 'rgba(255,255,255,0.1)')),
        yaxis=dict(showgrid=True, gridcolor=PALETTE.get('grid', 'rgba(255,255,255,0.1)'))
    )
    return fig
