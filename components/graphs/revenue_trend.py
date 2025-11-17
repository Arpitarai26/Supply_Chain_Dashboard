import plotly.express as px

def revenue_over_time(df, PALETTE):
    if df is None or df.empty:
        return {}

    bg = str(PALETTE.get('background', '#121212')).lower()
    dark_mode = bg in ('#121212', '#181818', '#000000', 'black')

    trend_data = df.groupby('WorkDate', as_index=False)['TotalRevenue'].sum()
    fig = px.line(trend_data, x='WorkDate', y='TotalRevenue', title="Revenue Over Time", markers=True)
    fig.update_traces(
        line=dict(color=PALETTE.get('primary', '#00BCD4'), width=3),
        marker=dict(color=PALETTE.get('secondary', '#FFC107'), size=5),
        fill='tozeroy', fillcolor='rgba(0,188,212,0.2)'
    )
    fig.update_layout(
        template='plotly_dark' if dark_mode else 'plotly_white',
        plot_bgcolor=PALETTE.get('plot_bg', '#181818'),
        paper_bgcolor=PALETTE.get('plot_bg', '#181818'),
        font_color=PALETTE.get('text', '#E0E0E0'),
        title_x=0.5
    )
    return fig
