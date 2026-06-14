import requests
import streamlit as st

API_URL = "http://api:8000"

st.title("Mon Application")

tab_login, tab_register = st.tabs(["Se connecter", "Créer un compte"])

with tab_register:
    st.subheader("Créer un compte")
    reg_username = st.text_input("Nom d'utilisateur", key="reg_user")
    reg_password = st.text_input("Mot de passe", type="password", key="reg_pass")
    if st.button("Créer mon compte"):
        try:
            resp = requests.post(
                f"{API_URL}/register",
                json={"username": reg_username, "password": reg_password},
            )
            if resp.status_code == 200:
                st.success("Compte créé avec succès !")
            else:
                st.error("Ce nom d'utilisateur existe déjà.")
        except Exception:
            st.error("Impossible de contacter le serveur.")

with tab_login:
    st.subheader("Se connecter")
    login_username = st.text_input("Nom d'utilisateur", key="login_user")
    login_password = st.text_input("Mot de passe", type="password", key="login_pass")
    if st.button("Se connecter"):
        try:
            resp = requests.post(
                f"{API_URL}/login",
                json={"username": login_username, "password": login_password},
            )
            data = resp.json()
            if data.get("success"):
                st.markdown(
                    f"<h2 style='text-align:center'>✅ Bienvenue, {login_username} ! Vous êtes connecté.</h2>",
                    unsafe_allow_html=True,
                )
            else:
                st.error("Nom d'utilisateur ou mot de passe incorrect.")
        except Exception:
            st.error("Impossible de contacter le serveur.")
