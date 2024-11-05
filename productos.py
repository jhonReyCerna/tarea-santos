
import streamlit as st
import pandas as pd
from config import obtener_conexion

def crear_producto(nombre, precio, stock):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)", (nombre, precio, stock))
    conexion.commit()
    conexion.close()

def leer_productos():
    conexion = obtener_conexion()
    df = pd.read_sql("SELECT * FROM productos", conexion)
    conexion.close()
    return df

def actualizar_producto(id, nombre, precio, stock):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("UPDATE productos SET nombre=?, precio=?, stock=? WHERE id=?", (nombre, precio, stock, id))
    conexion.commit()
    conexion.close()

def eliminar_producto(id):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM productos WHERE id=?", (id,))
    conexion.commit()
    conexion.close()

# Interfaz de Streamlit
st.title("Mantenedor de Productos")

opcion = st.selectbox("Selecciona una opción", ["Crear", "Leer", "Actualizar", "Eliminar"])

if opcion == "Crear":
    nombre = st.text_input("Nombre del producto")
    precio = st.number_input("Precio", min_value=0.0, format="%.2f")
    stock = st.number_input("Stock", min_value=0)
    if st.button("Crear producto"):
        crear_producto(nombre, precio, stock)
        st.success("Producto creado correctamente")

elif opcion == "Leer":
    st.subheader("Lista de Productos")
    productos = leer_productos()
    st.write(productos)

elif opcion == "Actualizar":
    id = st.number_input("ID del producto", min_value=1)
    nombre = st.text_input("Nuevo nombre del producto")
    precio = st.number_input("Nuevo precio", min_value=0.0, format="%.2f")
    stock = st.number_input("Nuevo stock", min_value=0)
    if st.button("Actualizar producto"):
        actualizar_producto(id, nombre, precio, stock)
        st.success("Producto actualizado correctamente")

elif opcion == "Eliminar":
    id = st.number_input("ID del producto a eliminar", min_value=1)
    if st.button("Eliminar producto"):
        eliminar_producto(id)
        st.success("Producto eliminado correctamente")
