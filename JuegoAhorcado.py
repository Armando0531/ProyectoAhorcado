'''
Created on 2 nov. 2021

@author: arman
'''
import os

class ManipulacionArchivo:
    def verificar(self):
        if not os.path.isfile("palabras.txt"): 
            print("No existe el archivo")
            archivo = open("palabras.txt","w+")
            archivo.close()
            if os.path.isfile("palabras.txt"):
                print("El archivo fue creado exitosamente")
                
        if not os.path.getsize("palabras.txt") > 0:
            print("El archivo esta vacio")
            return True
        
        else:
            with open("palabras.txt", "r+") as f:
                lineas = 0
                for l in f:
                    
                    if l != "\n":
                        lineas+=1
                print("Cantidad de palabras: "+str(lineas))
            return False
    
    def borrar(self):
        if os.path.isfile("palabras.txt"):
            os.remove("palabras.txt")
            
        with open("palabras.txt", "w+") as f:
            pass
        print("El archivo fue borrado exitosamente")
        
class JuegoAhorcado:

    def cargarPalabras(self,listaPalabras):
        palabras={""}
        return palabras
    def elegirPalabra(self):
        return "palabra elegida + idioma"
    def inicioAhorcado(self,palabraSecreta,idioma):
        ganador=False
        palabraIdioma=palabraSecreta.split("-")
        palabraSecret=palabraIdioma[0]
        idioma=palabraIdioma[1]
        pass
    def seAdivinoPalabra(self,palabra,letrasIngresadas):
        return True
    def obtenerPalabraAdivinada(self,palabra,letrasIngresadas):
        carac="!#$%&/()=?�'<>-_.:,;}{~+*"
        palabraCodificada=""
        for i in range(i,len(palabra)):
            palabraCodificada=palabraCodificada+carac[i]
    def obtenerLetrasDisponibles(self,letrasIngresadas):
        return "Letras disponibles"



#------------------------------------------------------Pruebas
op=""
while(op!="5"):
    print("Elige la opcion que deseas")
    print("1) Verificar Archivo")
    print("2) Llenar Archivo con palabras")
    print("3) Borrar archivo")
    print("4) Jugar")
    print("5) Salir")
    op=input()
    if(op=="1"):
        print("1")
    elif(op=="2"):
        print("op 2")
    elif(op=="3"):
        print("op 3")
    elif(op=="4"):
        print("op 4")
    elif(op=="5"):
        print("Saliendo.....")
    else:
        print("La opcion que seleccionaste no existe prueba otra opcion")