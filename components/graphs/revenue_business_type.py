import plotly.express as px

def revenue_by_business_type(df, PALETTE):
    if df is None or df.empty:
        return {}

    bg = str(PALETTE.get('background', '#121212')).lower()
    dark_mode = bg in ('#121212', '#181818', '#000000', 'black')

    grouped = df.groupby('BusinessType', as_index=False)['TotalRevenue'].sum()
    fig = px.bar(
        grouped, x='BusinessType', y='TotalRevenue',
        text_auto='.2s', title="Revenue by Business Type",
        color='TotalRevenue',
        color_continuous_scale=['#FFA000', '#FFC107', '#FFE082']
    )
    fig.update_layout(
        template='plotly_dark' if dark_mode else 'plotly_white',
        plot_bgcolor=PALETTE.get('plot_bg', '#181818'),
        paper_bgcolor=PALETTE.get('plot_bg', '#181818'),
        font_color=PALETTE.get('text', '#E0E0E0'),
        title_x=0.5
    )
    return fig
