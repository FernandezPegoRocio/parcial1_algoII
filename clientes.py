import sqlite3
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Clientes:
    def abrir(self):
        conexion = sqlite3.connect("bdcliente.db")
        return conexion
    
    def crear_tabla(self):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = """CREATE TABLE IF NOT EXISTS clientes (
            codigo TEXT PRIMARY KEY,
            nombre TEXT,
            contacto TEXT)"""
        cursor.execute(sql)
        cone.commit()
        cone.close()

    def alta(self, datos):
        cone = self.abrir()
        cursor = cone.cursor()  
        sql = "INSERT INTO clientes (codigo, nombre, contacto) VALUES (?, ?, ?)"
        cursor.execute(sql, datos)
        cone.commit()
        logging.info(f"Cliente {datos[0]} - {datos[1]} fue agregado con éxito")
        cone.close()

    def consulta(self, datos):
        try:
            cone = self.abrir()
            cursor = cone.cursor()  
            sql = "SELECT nombre, contacto FROM clientes WHERE codigo = ?"
            cursor.execute(sql, datos)
            return cursor.fetchall()
        finally:
            cone.close()

    def recuperar_todos(self):
        try:
            cone = self.abrir()
            cursor = cone.cursor()  
            sql = "SELECT codigo, nombre, contacto FROM clientes"
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            cone.close()

    def baja(self, datos):
        try:
            cone = self.abrir()
            cursor = cone.cursor()  
            sql = "DELETE FROM clientes WHERE codigo = ?"
            cursor.execute(sql, datos)
            cone.commit()
            logging.info(f"Cliente con código {datos[0]} eliminado")
            return cursor.rowcount
        finally:
            cone.close()

    def modificar(self, datos):
        try:
            cone = self.abrir()
            cursor = cone.cursor() 
            sql = "UPDATE clientes SET nombre = ?, contacto = ? WHERE codigo = ?"
            cursor.execute(sql, datos)
            cone.commit()
            logging.info(f"Cliente con código {datos[2]} se modificó correctamente")
            return cursor.rowcount
        finally:
            cone.close()

if __name__ == "__main__":
    cliente = Clientes()
    cliente.crear_tabla()