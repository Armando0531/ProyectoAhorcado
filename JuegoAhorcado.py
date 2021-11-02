'''
Created on 2 nov. 2021

@author: arman
'''
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