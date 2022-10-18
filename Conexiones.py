import sqlite3

class Conexiones:
    
    def abrirConexion(self):
        self.miConexion = sqlite3.connect("Concesionaria")
        self.miCursor = self.miConexion.cursor()
    
    def cerrarConexion(self):
        self.miConexion.close()   
