
#? Librerias por defecto
import json
#? Librerias de terceros
import streamlit as st
import streamlit_authenticator as stauth


def crear_credenciales(names:list, usernames:list, passwords:list):
    def guardar_sin_comentarios_espacios(contenido):
        lineas = contenido.split('\n')  # Dividir el contenido en líneas
        # Filtrar las líneas que no son comentarios ni espacios en blanco
        lineas_filtradas = [linea for linea in lineas if not linea.strip().startswith("#") and linea.strip()]
        # Unir las líneas filtradas de nuevo en un solo texto
        contenido_sin_comentarios_espacios = '\n'.join(lineas_filtradas)
        return contenido_sin_comentarios_espacios
    # Crear un objeto Hasher
    hashed_passwords = stauth.Hasher(passwords).generate()
    # Construir el contenido usando un diccionario y un bucle for
    user_data = {
        "usernames": {
            username: {
                "failed_login_attempts": 0,
                "logged_in": "False",
                "name": name,
                "password": hashed_password
            }
            for username, name, hashed_password in zip(usernames, names, hashed_passwords)
        }
    }
    # Convertir a string JSON
    contenido = json.dumps(user_data, indent=4)
    # Eliminar comentarios y espacios en blanco   
    contenido_sin_comentarios_espacios = guardar_sin_comentarios_espacios(contenido)
    # Escribir el contenido en el archivo
    with open(st.secrets["FILE_PATH_CREDENTIALS"], "w", encoding="utf-8") as archivo:
        archivo.write(contenido_sin_comentarios_espacios)

if __name__ == "__main__":
    crear_credenciales(st.secrets["NAMES"], st.secrets["USERNAMES"], st.secrets["PASSWORDS"])