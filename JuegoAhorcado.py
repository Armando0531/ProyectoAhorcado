'''
Created on 2 nov. 2021

@author: arman
'''
import os
import random

class Validacion:
    
    def validacionNatural(self):
        while True:
            try:
                r = int(input())
            except:
                print("Solamente numeros: ")
            else:
                if r>0:
                    break
                else:
                    print("Solamente enteros positivos, intente de nuevo: ")
        return r
    
    def validacionPalabra(self):
        palabra = str()
        palabraValidada = str()
        l = ''
        while True:
            palabra = str(input().lower())
            if len(palabra)>0:
                for i in range(len(palabra)):
                    l = ord(palabra[i])
                    if 93<l and l<123:
                        palabraValidada+=palabra[i]
                if len(palabraValidada)==0:
                    print("Palabra no valida, intente de nuevo:")
                else:
                    break
            else:
                print("Entrada no valida, intente de nuevo:")
        return palabraValidada
    
class Oportunidades:
    def __init__(self):
        self.__oportunidades = 10
        
    def getOportunidades(self):
        return self.__oportunidades
    
    def setOportunidades(self, oportunidades):
        self.__oportunidades=oportunidades
        
    def decrementar(self):
        print("Lo siento, esa letra no esta en la palabra secreta:",end=" ")
        self.setOportunidades((self.getOportunidades()-1))
        
    def mostrarOportunidades(self):
        print("Te quedan "+str(self.getOportunidades())+" oportunidades para adivinar")
        
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
        
    def guardar(self):
        palabras = []
        print("Cantidad de palabras a ingresar:")
        cnt = Validacion.validacionNatural(Validacion)
        for i in range(cnt):
            print("Palabra "+str(i+1)+':')
            palabras.append(Validacion.validacionPalabra(Validacion))
            
        palabras.sort()
        with open("palabras.txt", "a+") as f:
            for i in palabras:
                f.write(i+"\n")
                
        print(str(cnt)+" palabras cargadas correctamente \n")
    def ordenar(self):
        palabras=[]
        with open("palabras.txt", "r") as f:
            for l in f:
                tmp = l.split()
                for i in tmp:
                    palabras.append(i)
                    
        palabras.sort()
        with open("palabras.txt", "w") as f:
            for i in palabras:
                f.write(i+"\n")
    def cargar(self):
        print("Cargando lista de palabras desde el archivo...")
        self.ordenar(ManipulacionArchivo)
        palabras=[]
        with open("palabras.txt", "r") as f:
            for l in f:
                tmp = l.split()
                for i in tmp:
                    palabras.append(str(i).upper())
                    
        print(str(len(palabras))+" palabras cargadas")
        return palabras
        
class Pila:
    def __init__(self):
        self.letras=[]
        
    def getLetras(self):
        return self.letras
    
    def setLetras(self, letras):
        self.letras=letras
    
    def extraer(self):
        if self.getLetras() == []:
            return ' '
        else:
            return self.letras.pop(0)

    def anadir(self, letra):
        lts=[]
        lts.append(letra)
        while not self.letras == []:
            lts.append(self.letras.pop())
            
        lts.sort()
        self.setLetras(lts)

    def obtenerPalabraAdivinada(self,palabraSecreta):
        lts = []
        for i in palabraSecreta:
            y=0
            while not self.letras == []:
                lt = self.extraer()
                lts.append(lt)
                if lt==i:
                    y=1
                    print(i,end=" ")
                    break
            while not lts == []:
                self.anadir(lts.pop(0))
            if y==0:
                print("_",end=" ")    
        print("\n\n")

class LetrasDisponibles:
    
    def __init__(self):
        self.__letrasDisponibles=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    def getLetrasDisponibles(self):
        return self.__letrasDisponibles
    
    def setLetrasDisponibles(self, letrasDisponibles):
        self.__letrasDisponibles=letrasDisponibles
        
class JuegoAhorcado:
    def __init__(self):
        self.oportunidades=Oportunidades()
    def cargarPalabras(self):
        return ManipulacionArchivo.cargar(ManipulacionArchivo)
    def elegirPalabra(self, palabras):
        x = random.randint(0,(len(palabras)-1))
        return palabras[x]
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