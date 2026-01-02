import streamlit as st


# --- #: Declaración de Multipáginas :# --- #

acerca_de = st.Page(
    page="pages/acerca_de.py",
    title="Acerca de WRB",
    icon=":material/info:",
    default=True
)
organizar_combates = st.Page(
    page="pages/organizar_combate.py",
    title="Organizar combate",
    icon=":material/info:"
)
combates_programados = st.Page(
    page="pages/combates_programados.py",
    title="Combates programados",
    icon=":material/info:"
)
robots = st.Page(
    page="pages/robots.py",
    title="Robots",
    icon=":material/info:"
)
armas = st.Page(
    page="pages/armas.py",
    title="Armas",
    icon=":material/info:"
)

# --- #: Menú de Navegación :# --- #

navegacion = st.navigation({
    "Info": [acerca_de],
    "Combates":[organizar_combates, combates_programados],
    "Catálogo":[robots, armas]
    })

navegacion.run()

# --- #: Presentación Lobby :# --- #

st.title(
    body=":red[*World Robot Boxing*]",
    anchor=False,
    text_alignment="center"
)
st.subheader(
    body="Planificador de Combates",
    anchor=False,
    text_alignment="center")
st.divider()