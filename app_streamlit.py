import plotly.express as px
import streamlit as st

# Création d'un DataFrame simple
df = px.data.stocks(indexed=True).stack().reset_index()
df.rename(columns={0:"valeur de l'action"},inplace=True)
# widget pour ajouter un titre
st.title('Cours des actions par entreprise')

# Widget pour sélectionner une entreprise
company = st.selectbox('Choisissez une entreprise :', df["company"].unique())

# Filtrage des données basé sur la sélection
filtered_data = df[df['company'] == company]

# Mise à jour du graphique
fig = px.line(filtered_data, x="date", y="valeur de l'action")
st.plotly_chart(fig)