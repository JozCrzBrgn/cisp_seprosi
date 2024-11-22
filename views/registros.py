import streamlit as st

col1, col2 = st.columns([1, 2])
with col1:
    st.image("assets/cisp.png")
with col2:
    st.title("Registro de elementos")

st.write("Aquí se mostrarán los elementos registrados en la base de datos.")
st.button("Registrar nuevo elemento")