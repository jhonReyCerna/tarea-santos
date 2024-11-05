# usuarios.py
import streamlit as st
import pandas as pd
from config import obtener_conexion

def crear_usuario(nombre, email, telefono):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO usuarios (nombre, email, telefono) VALUES (?, ?, ?)", (nombre, email, telefono))
    conexion.commit()
    conexion.close()

def leer_usuarios():
    conexion = obtener_conexion()
    df = pd.read_sql("SELECT * FROM usuarios", conexion)
    conexion.close()
    return df

def actualizar_usuario(id, nombre, email, telefono):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("UPDATE usuarios SET nombre=?, email=?, telefono=? WHERE id=?", (nombre, email, telefono, id))
    conexion.commit()
    conexion.close()

def eliminar_usuario(id):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM usuarios WHERE id=?", (id,))
    conexion.commit()
    conexion.close()

# Interfaz de Streamlit
st.title("Mantenedor de Usuarios")

opcion = st.selectbox("Selecciona una opción", ["Crear", "Leer", "Actualizar", "Eliminar"])

if opcion == "Crear":
    nombre = st.text_input("Nombre")
    email = st.text_input("Email")
    telefono = st.text_input("Teléfono")
    if st.button("Crear usuario"):
        crear_usuario(nombre, email, telefono)
        st.success("Usuario creado correctamente")

elif opcion == "Leer":
    st.subheader("Lista de Usuarios")
    usuarios = leer_usuarios()
    st.write(usuarios)

elif opcion == "Actualizar":
    id = st.number_input("ID del usuario", min_value=1)
    nombre = st.text_input("Nuevo nombre")
    email = st.text_input("Nuevo email")
    telefono = st.text_input("Nuevo teléfono")
    if st.button("Actualizar usuario"):
        actualizar_usuario(id, nombre, email, telefono)
        st.success("Usuario actualizado correctamente")

elif opcion == "Eliminar":
    id = st.number_input("ID del usuario a eliminar", min_value=1)
    if st.button("Eliminar usuario"):
        eliminar_usuario(id)
        st.success("Usuario eliminado correctamente")
