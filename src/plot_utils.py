import plotly.graph_objects as go
from statsmodels.distributions.empirical_distribution import ECDF

colors = {
    "red": "#ee443a",
    "blue": "#42bbf1",
    "dark_blue": "#1a4fec",
    "green": "#50be61",
    "grey": "#b7b7b7",
    "orange": "#f28222",
    "purple": "#6e18ee",
    "brown": "#a65628",
}


def get_plotly_layout(width, height):
    layout = go.Layout(
        template="simple_white",
        font=dict(size=18, family="Clear Sans"),
        margin=go.layout.Margin(
            l=10,  # left margin
            r=10,  # right margin
            b=10,  # bottom margin
            t=10,  # top margin
        ),
        width=width,
        height=height,
        xaxis=dict(
            minor_ticks="inside", showgrid=True, griddash="dash", minor_griddash="dot"
        ),
        yaxis=dict(
            minor_ticks="inside", showgrid=True, griddash="dash", minor_griddash="dot"
        ),
    )
    return layout


def plot_cdf(data, width=800, height=450, xlog=False, xaxis_title='', color=colors['blue'], filename=False):
    fig = go.Figure(layout=get_plotly_layout(width=width, height=height))
    ecdf = ECDF(data)
    fig.add_trace(go.Scatter(x=ecdf.x, y=ecdf.y,
                             line=dict(color=color, width=5, dash=None)))
    if xlog:
        fig.update_xaxes(type='log')
    fig.update_yaxes(range=[0, 1], tickformat=',.0%')
    fig.update_layout(
        xaxis_title=xaxis_title,
        yaxis_title='CDF')
    if filename:
        fig.savefig(filename, bbox_inches='tight')
    return fig
