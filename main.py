import streamlit as st


# --- #: Presentación Lobby :# --- #

def cambiar_fondo(): st.markdown( """ <style> .stApp { background-image: url("images\fondo.png"); background-attachment: fixed; background-size: cover; background-repeat: no-repeat; background-position: center; } </style> """, unsafe_allow_html=True )
cambiar_fondo()

st.title(
    body=":red[*World Robot Boxing*]",
    anchor=False,
    text_alignment="center"
)
st.subheader(
    body=":blue[|Planificador de Combates|]",
    anchor=False,
    text_alignment="center")
st.divider()



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

st.logo("images/logo.png", size="large", link="https://gigantes-de-acero.fandom.com/es/wiki/World_Robot_Boxing#:~:text=World%20Robot%20Boxing%20es%20una,los%20que%20participan%20los%20robots.")

navegacion.run()

