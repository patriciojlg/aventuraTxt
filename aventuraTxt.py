# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 13:11:04 2013

@author: joaquino

BITACORA

03/09/13
irA() ya logra cambiar la hubicacion del personaje.
04/09/13
irA() a traves de movimientosValidos()
Logra mover al persona de hubicacion, describe la nueva hubicacion
05/09/13
Se depura el procesamiento de las frases entrades a través de la creación de 
función que limpia la entrada de hilativos dejando solo verbo + sustantivo.
ir al bano ---> ir bano | mirar la piedra --> mirar piedra

 


TAREAS PENDIENTES:
    
    - Descripción especial al: Entrar a una hubicación.
    - Mostrar salidas disponibles: al describir 1°vez la hubicación 
      y al recibir verbo.ir 
    -
    
   
   VerbObjetoHub(queverbo,queobjeto):
           obj = queobjeto
        if queverbo in verbos and queobjeto in hubicacion.objetos:
            return true
        else:
            return false
    
Como usar:
    if verboObjetoHub("coger","manzana") == True:
        print "Coges la manzana y la guardas en tu mochila"
        hubicacion.objetos.remove(obj)
        inventario.extend(obj)
   

#SIN HILATIVOS!

Ahora usar hilativos.sinHilativos 
Para un mejor manejo de las ordenes entrates!     
"""

## Esta clase es constructora y crea el objeto lugar

class lugar(object):
    def __init__(self):
        #Intterruptor de eventos
        self.interruptor = False
        #Descripción tomada por el método setDescripcion()
        self.descripcion = ""
        self.descriocionEnt = ""
        #En los objetos lo ideal sería usar un sucedaneo de Switch-Case 
        #Con descripcion, y reaccion para cada verbo y convinatoria con el inventario()
        self.objetos = {}
        self.salidas = {}
   #SETTERS!    
    def setDescripcion(self,descripcion):
        self.descripcion = descripcion
    def setObjetos(self,Nobjeto):
        self.objetos = self.lugar.extend(Nobjeto)
    def setSalidas(self,cordenada,Dsalida):
        self.salidas[cordenada] = Dsalida 
        
    #GETTERS
    def getDescripcion(self):
        print self.descripcion
    def getSalidas(self):
        print self.salidas


#Lugares
cuarto = lugar()
bano = lugar()
bano.descripcionEnt = "Entras en el bano fétido..."
bano.descripcion = "Este lugar apesta... estás en un bano que tiene un olor que se mete en tu nariz y como ácido recorre tu sistema respiratorio. A demás, el lugar tiene unas paredes cubiertas de algo esponjoso que parece estar vivo. La tasa está casi rebalsando de un liquido rojo; la cadena de este al parecer no se ha tirado en siglos."
#Salidas
cuarto.salidas = ["bano"]
bano.salidas = ["cuarto"]
#Defino hubicacion inicial
hubicacion = cuarto

cuarto.objetos["luz"] = "Tras la puerta de entrada a esta habitación se siente un interruptor"
cuarto.descripcion = "No veo nada está todo oscuro..."

#Sin Hilativos

sinHilativos = []

#Definir verbos

verbo = []
mirar = ["mirar","examinar","explorar"]
verbo.extend(mirar)
comer = ['comer','tragar','ingerir','deborar','engullir']
verbo.extend(comer)
ir = ["ir","moverse","dirigirse","salir","trasladarse","irse","entrar"]
verbo.extend(ir)
activar = ["encender","activar","prender"]
verbo.extend(activar)
#articulos
articulos = ['el','la','los','las']
preposiciones = ["a","hacia","al"]

conectores = []
conectores.extend(articulos)
conectores.extend(preposiciones)

#Objetos

#Funcion de errores en la entrada

def entradaDesconocida(entrada):
    if entrada[0] not in verbo:
        print "No conozco el verbo %s. Prueba con otro por favor" % entrada[0]
    elif len(entrada) > 1:    
        #Ojo cuarto debe ser una clase intanciada
        if entrada[0] not in ir and entrada[0] in verbo and entrada[1] not in hubicacion.objetos:
            print "No veo aquello que quieres %s" % entrada[0]


#Metodo ir a; ir a el, ir hacia el, etc  etc
def movimientosValidos(entrada):
    if len(entrada) < 3:
        if entrada[0] in ir and entrada[1] in hubicacion.salidas:
            return True
  #  elif len(entrada) < 4:
   #     if entrada[0] in ir and entrada[1] in preposiciones and entrada[2] in hubicacion.salidas:
    #        return True
   # elif len(entrada) < 5:
    #    if entrada[0] in ir and entrada[1] in preposiciones and entrada[2] in articulos and entrada[3] in hubicacion.salidas:
     #       return True
    else:
        return False

#Recibe el verbo ir y cambia la hubicacion; a través de las salidas de cada hubicacion. 
def irA(entrada):
    global hubicacion
    if entrada[0] in ir:
        #Solo un verbo ir[]
        if len(entrada) < 2:
            print "Sí, pero %s a dónde?" % entrada[0]
            #Sin artículo            
        elif movimientosValidos(entrada) == True:
                hubicacion = eval(entrada[len(entrada)-1])
                print hubicacion.descripcionEnt
        else:
            print "No te entiendo hacia donde quieres ir"

#Imprime descripciones de los lugares y los objetos            
def descriptor(entrada):
    global hubicacion
    orden = entrada
    ##Muestra la descripción de la hubicacion examinada
    if len(orden) == 1:
        if orden[0] in mirar:
            print hubicacion.descripcion
            
    ##Muestra la descripcion del objeto examinado
    elif len(orden) > 1:
        if orden[0] in mirar and orden[1] in hubicacion.objetos:
            print hubicacion.objetos[orden[1]]


#MEJORA DEL CODIGO A TRAVES DE UN ELIMINADOR DE HILATIVOS!
def hilativos(entrada):
    global sinHilativos
    sinHilativos = []
    #Toma la entrada (como lista) y le saca los hilativos
    for i in entrada:
        if conectores.count(i) > 0:
            entrada.remove(i)
        
    #Le da una repasada por si quedó un hilativo sin eliminar    
    for e in entrada:
        if conectores.count(e) > 0:
            entrada.remove(e)
    sinHilativos = entrada
    
## -- HASTA ACA OBJETALES --
    
    ##Eventos para "Cuarto"
def eCuarto(entrada):
    if hubicacion == cuarto:
        ##Todos los eventos de esta habitación
        
        #Enciende la luz y agrega nuevos objetos a la habitacion
        if orden[0] in activar and orden[1] == "luz":
            cuarto.descripcion = "Estás en una habitación muy amplia, vacía por completo, no obstante, la pared del fondo tiene algunos GRABADOS"
            cuarto.objetos["grabados"] = "Son unos extraños grabados tipo indígenas que forman un árbol, y como fruto de éste hay incrustada en la pared una PIEDRA que brilla"                         
            print "Prendes la luz de la habitación, ahora todo se puede ver mucho mejor\nDas un vistaso y te das cuenta que "
            cuarto.getDescripcion()
            
        #No se puede apagar la luz
        elif orden == "apagar la luz":
            print "No deseo apagarla, la verdad es que siento un poco de miedo por la oscuridad"
         
        #Es probable que los métodos intanciables deban estar dentro de la
        #clase constructura.
        
        ##Evetos para bano       
    elif hubicacion == bano:
        pass
        
while True:
    orden = raw_input("Que hace: ")
    orden = orden.lower()
    orden = orden.split(" ")
    hilativos(orden)
    orden = sinHilativos
    entradaDesconocida(orden)
    eCuarto(orden)
    descriptor(orden)
    irA(orden)