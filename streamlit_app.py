
import streamlit as st

#? --- PAGE SETUP ---#
st.set_page_config(layout="wide")

registros_page = st.Page(
    page="views/registros.py",
    title="Registros",
    icon="📋",
    default=True
)
consultar_page = st.Page(
    page="views/consultar.py",
    title="Consultar",
    icon="🔎",
)

#? --- NAVEGATION SETUP [WITH SECTIONS] ---#
pg = st.navigation(
    {
        "Información de personal": [registros_page, consultar_page],
    }
)

#? --- SHARE ON ALL PAGES ---#
st.logo("assets/cisp.png")
st.sidebar.text("Made with ❤️ by Joz")

#? --- RUN NAVEGATION ---#
pg.run()