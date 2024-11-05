# config.py
import pyodbc

def obtener_conexion():
    conexion = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=DESKTOP-P09OFMG\\SQLEXPRESS;'
        'DATABASE=gestion_datos;'
        'UID=sa;'
        'PWD=123456'
    )
    return conexion