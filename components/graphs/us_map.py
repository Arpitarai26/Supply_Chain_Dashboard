import plotly.express as px
import plotly.graph_objects as go

def revenue_us_map(df, PALETTE):
    if df is None or df.empty or 'State' not in df.columns:
        fig = go.Figure()
        fig.update_layout(
            title="No data available for U.S. map",
            paper_bgcolor=PALETTE.get("plot_bg", "#181818"),
            plot_bgcolor=PALETTE.get("plot_bg", "#181818"),
            font_color=PALETTE.get("text", "#E0E0E0"),
            title_x=0.5
        )
        return fig

    state_data = df.groupby('State', as_index=False)['TotalRevenue'].sum().sort_values('TotalRevenue', ascending=False)
    fig = px.choropleth(
        state_data,
        locations='State', locationmode='USA-states', color='TotalRevenue',
        color_continuous_scale=['#004d73', PALETTE.get('primary', '#00BCD4'), '#80deea'],
        scope='usa', title='Revenue Distribution Across U.S. States',
        labels={'TotalRevenue': 'Total Revenue ($)'}
    )
    fig.update_layout(
        geo_bgcolor=PALETTE.get('plot_bg', '#181818'),
        plot_bgcolor=PALETTE.get('plot_bg', '#181818'),
        paper_bgcolor=PALETTE.get('plot_bg', '#181818'),
        font_color=PALETTE.get('text', '#E0E0E0'),
        geo=dict(showframe=False, showcoastlines=False, landcolor=PALETTE.get('plot_bg', '#181818')),
        title_x=0.5
    )
    if not state_data.empty:
        top_state = state_data.iloc[0]
        fig.add_annotation(
            text=f"🏆 Top State: {top_state['State']} (${top_state['TotalRevenue']:,.0f})",
            xref="paper", yref="paper", x=0.5, y=-0.15,
            showarrow=False, font=dict(size=12, color=PALETTE.get('text', '#E0E0E0'))
        )
    return fig
