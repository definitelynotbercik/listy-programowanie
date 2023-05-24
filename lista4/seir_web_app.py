import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import numpy as np
from scipy.integrate import odeint
import plotly.graph_objects as go


def seir(S0, E0, I0, R0, beta, sigma, gamma):
    N = S0 + E0 + I0 + R0

    def dydt(y, t):
        S, E, I, R = y
        return [-beta*S*I/N,
                beta*S*I/N - sigma*E,
                sigma*E - gamma*I,
                gamma*I]

    t = np.linspace(0, 100, 1000)
    
    y0 = (S0, E0, I0, R0)
    
    sol = odeint(dydt, y0=y0, t=t)
    
    (S, E, I, R) = sol.T

    return t, S, E, I, R


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.VAPOR])


# layout of the app
app.layout = html.Div(
    children=[
        html.H1(children="SEIR Model", style={'textAlign' : 'center'}),
        dcc.Graph(id="seir-plot"),
        html.Div(
            children=[
                html.Label("Initial number of susceptible people (S0)"),
                dcc.Slider(0, 2000, 50, id="susceptible-input", value=999),
            ]
        ),
        html.Div(
            children=[
                html.Label("Initial number of exposed people (E0)"),
                dcc.Slider(0, 2000, 50, id="exposed-input", value=1),
            ]
        ),
        html.Div(
            children=[
                html.Label("Initial number of infective people (I0)"),
                dcc.Slider(0, 2000, 50, id="infective-input", value=0),
            ]
        ),
        html.Div(
            children=[
                html.Label("Initial number of recovered people (R0)"),
                dcc.Slider(0, 2000, 50, id="recovered-input", value=0),
            ]
        ),
        html.Div(
            children=[
                html.Label("Infectious rate (beta)"),
                dcc.Slider(0, 5, 0.1, id="beta-input", value=1.34),
            ]
        ),
        html.Div(
            children=[
                html.Label("Incubation rate (sigma)"),
                dcc.Slider(0, 5, 0.1, id="sigma-input", value=0.19),
            ]
        ),
        html.Div(
            children=[
                html.Label("Recovery rate (gamma)"),
                dcc.Slider(0, 5, 0.1, id="gamma-input", value=0.34),
            ]
        )
    ]
)

# callback function updating the plot
@app.callback(
    Output("seir-plot", "figure"),
    [
        Input("susceptible-input", "value"),
        Input("exposed-input", "value"),
        Input("infective-input", "value"),
        Input("recovered-input", "value"),
        Input("beta-input", "value"),
        Input("sigma-input", "value"),
        Input("gamma-input", "value"),
    ],
)
def update_seir_plot(S0, E0, I0, R0, beta, sigma, gamma):
    t, S, E, I, R = seir(S0, E0, I0, R0, beta, sigma, gamma)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=t, y=S, mode="lines", name="Susceptible"))
    fig.add_trace(go.Scatter(x=t, y=E, mode="lines", name="Exposed"))
    fig.add_trace(go.Scatter(x=t, y=I, mode="lines", name="Infective"))
    fig.add_trace(go.Scatter(x=t, y=R, mode="lines", name="Recovered"))

    fig.update_layout(
        xaxis_title="Time (days)",
        yaxis_title="People",
        title=f"S0={S0}, E0={E0}, I0={I0}, R0={R0}, beta={beta}, sigma={sigma}, gamma={gamma}",
    )

    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
    