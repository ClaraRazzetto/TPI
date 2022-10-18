from Conexiones import Conexiones

class Automovil:
    def __init__(self, marca, modelo,precio=None,cantidadDisponibles=None):
        self.marca = marca
        self.modelo = modelo
        self.precio=precio
        self.cantidadDisponibles=cantidadDisponibles
        
    def cargar_automovil(self):
        try:
            self.validar()
        except:
            print("Error al cargar datos del automovil")
        else:
            conexion = Conexiones()
            conexion.abrirConexion()
            try:
                conexion.miCursor.execute("INSERT INTO AUTOMOVILES(marca,modelo,precio,cantidadDisponibles) VALUES('{}', '{}','{}','{}')".format(self.marca, self.modelo, self.precio, self.cantidadDisponibles))
                conexion.miConexion.commit()
                print("Automovil cargado exitosamente")
            except:
                print("Error al agregar un automovil")
            finally:
                conexion.cerrarConexion()
        
    
    def modificar_automoviles(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("UPDATE AUTOMOVILES SET precio='{}' where marca='{}' and modelo='{}' ".format(self.precio,self.marca,self.modelo))
            conexion.miConexion.commit()
            print("Automovil modificado correctamente")
        except:
            print('Error al actualizar un automovil')
        finally:
            conexion.cerrarConexion()  
            
            
    def cargar_disponibilidad(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            sql = "select * from AUTOMOVILES where marca = '"+ self.marca + "' and modelo = '" + self.modelo + "'"
            conexion.miCursor.execute(sql)
            rows = conexion.miCursor.fetchall()
            if  rows:
                sql = "update AUTOMOVILES SET cantidadDisponibles = cantidadDisponibles + 1 where marca = '" + self.marca + "' and modelo = '" + self.modelo + "'"
                conexion.miCursor.execute(sql) 
                conexion.miConexion.commit()
                print("Automovil cargado exitosamente")
    
            else:
                print ('no existen un automovil  marca ' + self.marca + ' -  modelo = ' + self.modelo )           
            
        except:
            print("Error al cargar automovil")
        finally:
            conexion.cerrarConexion()

    def borrar_automovil(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("DELETE FROM AUTOMOVILES where marca='{}' and modelo='{}'" .format(self.marca, self.modelo))
            conexion.miConexion.commit()
            print("Automovil borrado exitosamente")
        except:
            print("Error al borrar un automovil")
        finally:
            conexion.cerrarConexion()

    def listado_automoviles(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        
        try:
            conexion.miCursor.execute("SELECT * FROM AUTOMOVILES")
            autos = conexion.miCursor.fetchall()        
            if(autos):
                for auto in autos:
                    print("ID:",auto[0]," Marca:",auto[1]," Modelo:",auto[2]," Precio:",auto[3]," Cantidad disponible:", auto[4])            
            else:
                print("No se han encontrado registros de automoviles")
        except:
            print("Error al listar automoviles")
        finally: 
            conexion.cerrarConexion
        

    def validar(self):
        if(len(self.marca)>=30 or len(self.modelo)>=30 or self.precio <= 0 or self.cantidadDisponibles <=0):
            raise Exception
        elif(not type(self.marca) is str or not type(self.modelo) is str or not type(self.precio) is float or not type(self.cantidadDisponibles) is int):
            raise TypeError