'''
Created on 2 nov. 2021

@author: arman
'''
import os
import random

class Validacion:
    
    def validacionLetra(self):
        c = ''
        while True:
            c = str(input()).lower()
            if len(c)==1:
                b=ord(c[0])
                if 93<b and b<123:
                    break
                else:
                    print("Caracter no valido, intente de nuevo:")
            else:
                print("Entrada no valida, intente de nuevo:")
        return c
    
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
        
    def ordenamientoMezclaDirecta(self,array):
        
        mitad=len(array)//2
        
        if len(array)>=2:
            arregloIz=array[mitad:]
           
            arregloDer=array[:mitad]
            

            array.clear()
            
            self.ordenamientoMezclaDirecta(self,arregloIz)
            
            self.ordenamientoMezclaDirecta(self,arregloDer)
            
            #Hasta aqui es la divicion de todos los elemntos hasta que llege a ser igual a 1
            while(len(arregloDer)>0 and len(arregloIz)>0):
                if(arregloIz[0]< arregloDer[0]):# si la pocicion de la izquierda es menor a la derecha
                    array.append(arregloIz.pop(0))
                else:
                    array.append(arregloDer.pop(0))
            #Hace que siempre se este actualizando ya que se elimina la pocicion
            
            #Ahora esto es por si llegan a quedar elementos sobrantes
            while len(arregloIz)>0:
                array.append(arregloIz.pop(0))
            
            while len(arregloDer)>0:
                array.append(arregloDer.pop(0))
        
        return array    
    
    def ordenar(self):
        palabras=""
        with open("palabras.txt", "r") as f:
            for l in f:
                tmp = l.split()
                for i in tmp:
                    palabras=palabras+i+"/"
                    
        vector=palabras.split("/")
        vector2= self.ordenamientoMezclaDirecta(self,array=palabras.split("/"))
        with open("palabras.txt", "w") as f:
            for i in vector2:
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
        
    def mostrarLetrasDisponibles(self):
        print("Letras disponibles: ",end="")
        letras=self.getLetrasDisponibles()
        for i in letras:
            print(i, end=" ")  
        print()

    def encontrarLetra(self, letra):
        letras=self.getLetrasDisponibles()
        x = 0
        for i in range (len(letras)):
            if letra == letras[i]:
                letras[i]='_'
                x=1
                break
        self.setLetrasDisponibles(letras)
        return x==1
    
class JuegoAhorcado:
    def __init__(self):
        self.oportunidades=Oportunidades()
    def cargarPalabras(self):
        return ManipulacionArchivo.cargar(ManipulacionArchivo)
    def elegirPalabra(self, palabras):
        x = random.randint(0,(len(palabras)-1))
        return palabras[x]
    def inicioAhorcado(self, palabraSecreta):
        print("Bienvenido al juego del ahorcado \nEstoy pensando en una palabra de "+str(len(palabraSecreta))+" letras \n========\n")
        letrasDisponibles = LetrasDisponibles()
        letrasIngresadas = Pila()
        while (self.oportunidades.getOportunidades()>0) and (not self.seAdivinoLaPalabra(palabraSecreta, letrasIngresadas)):
            self.oportunidades.mostrarOportunidades()
            letrasDisponibles.mostrarLetrasDisponibles()
            print("Por favor ingresa una letra: ",end="")
            letra = Validacion.validacionLetra(Validacion)
            if letrasDisponibles.encontrarLetra(letra):
                letrasIngresadas.anadir(letra)
                if letra in palabraSecreta.lower():
                    print("Bien hecho: ",end="")
                else:
                    self.oportunidades.decrementar()
            else:
                print("Ya ingresaste esa letra")
            letrasIngresadas.obtenerPalabraAdivinada(palabraSecreta.lower())
            
        if self.seAdivinoLaPalabra(palabraSecreta, letrasIngresadas):
            print("Felicidades, has GANADO")
        else:
            print("NO has adivinado la palabra. La palabra secreta era: "+palabraSecreta) 
    def seAdivinoLaPalabra(self, palabraSecreta, letrasIngresadas):
        x=1
        palabraSecreta=palabraSecreta.lower()
        lts = []
        for i in palabraSecreta:
            y=0
            while not letrasIngresadas.getLetras() == []:
                lt = letrasIngresadas.extraer()
                lts.append(lt)
                if lt==i:
                    y=1
                    break
            while not lts == []:
                letrasIngresadas.anadir(lts.pop(0))
            x*=y
        return x==1



class PruebaJuegoAhorcado:
    def menuOpciones(self):
        while True:  
            print("Elige la opcion que deseas")
            print("1) Verificar Archivo")
            print("2) Llenar Archivo con palabras")
            print("3) Borrar Archivo")
            print("4) Jugar")
            print("5) Salir")  
            opc = Validacion.validacionNatural(Validacion)
            if(opc==1):
                ManipulacionArchivo.verificar(ManipulacionArchivo)
                ManipulacionArchivo.ordenar(ManipulacionArchivo)
            elif(opc==2):
                ManipulacionArchivo.guardar(ManipulacionArchivo)
            elif(opc==3):
                ManipulacionArchivo.borrar(ManipulacionArchivo)
            elif(opc==4):
                if ManipulacionArchivo.verificar(ManipulacionArchivo):
                    ManipulacionArchivo.guardar(ManipulacionArchivo)
                ja = JuegoAhorcado()
                palabras = ja.cargarPalabras()
                palabraSecreta = ja.elegirPalabra(palabras)

                ja.inicioAhorcado(palabraSecreta)
            elif(opc==5):
                print("Gracias por jugar")
                break
            else:
                print("Opcion no valida")

pja = PruebaJuegoAhorcado()
pja.menuOpciones()