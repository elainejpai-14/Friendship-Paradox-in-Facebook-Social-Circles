import pandas as pd
import dash
from dash import dcc, html, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px

# Load data
df = pd.read_csv("paradox_analysis.csv")
df["ParadoxHolds"] = df["Paradox_Strength"] > 1

# Dash app setup
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server  # For Render

app.title = "Friendship Paradox Dashboard"
app.layout = dbc.Container([
    html.H2("📊 Friendship Paradox Dashboard", className="text-center mt-4"),
    dbc.Row([
        dbc.Col([
            dcc.Dropdown(id='paradox-filter',
                         options=[
                             {"label": "All Nodes", "value": "all"},
                             {"label": "Only Paradox Nodes", "value": "paradox"},
                             {"label": "Only Non-Paradox Nodes", "value": "non-paradox"}],
                         value="all", clearable=False)
        ], width=4),
    ], className="mb-3"),
    dbc.Row([
        dbc.Col(dcc.Graph(id="degree-histogram"), width=6),
        dbc.Col(dcc.Graph(id="strength-histogram"), width=6),
    ]),
    dbc.Row([dbc.Col(dcc.Graph(id="scatter-plot"))])
], fluid=True)

@app.callback(
    Output("degree-histogram", "figure"),
    Output("strength-histogram", "figure"),
    Output("scatter-plot", "figure"),
    Input("paradox-filter", "value"))
def update_charts(paradox_filter):
    dff = df.copy()
    if paradox_filter == "paradox":
        dff = dff[dff["ParadoxHolds"] == True]
    elif paradox_filter == "non-paradox":
        dff = dff[dff["ParadoxHolds"] == False]

    fig1 = px.histogram(dff, x="Degree", nbins=30, title="Degree Distribution")
    fig2 = px.histogram(dff, x="Paradox_Strength", nbins=30, title="Paradox Strength Distribution")
    fig3 = px.scatter(dff, x="Degree", y="Paradox_Strength", color=dff["ParadoxHolds"].astype(str),
                      title="Paradox Strength vs Degree", color_discrete_map={"True": "green", "False": "purple"})
    return fig1, fig2, fig3

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8050)
