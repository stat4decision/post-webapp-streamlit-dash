import dash
from dash import html, dcc
import plotly.express as px
from dash.dependencies import Input, Output
import plotly.express as px

# Données de démonstration
df = px.data.stocks(indexed=True).stack().reset_index()
df.rename(columns={0:"valeur de l'action"},inplace=True)

# Initialisation de l'application Dash
app = dash.Dash(__name__)

# Layout de l'application
app.layout = html.Div([
    # Titre de l'application
    html.H1('Cours des actions par entreprise'),
    # Texte descriptif
    html.P("Choisissez une entreprise:"),
    # Selectbox pour choisir une espèce
    dcc.Dropdown(
        id='company-selector',
        options=[{'label': i, 'value': i} for i in df['company'].unique()],
        value='GOOG'  # Valeur par défaut
    ),

    # Graphique qui se met à jour en fonction de la sélection
    dcc.Graph(id='graph-output')
])

# Callback pour mettre à jour le graphique
@app.callback(
    Output('graph-output', 'figure'),
    [Input('company-selector', 'value')]
)
def update_graph(company):
    filtered_df = df[df['company'] == company]
    fig = px.line(filtered_df, x="date", y="valeur de l'action")
    return fig

# Exécution de l'application
if __name__ == '__main__':
    app.run_server(debug=True)