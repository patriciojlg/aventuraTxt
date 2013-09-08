# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 13:11:04 2013

@author: joaquino

Hasta el momento una vez ejecutado este archivo (el juego) es posible:

pedir la descricion del cuarto --> mirar
como todo está oscuro uno puede --> encender luz | si enciendes la luz cambia la descripcion del cuarto (pues puedes ver)
mirar el gabado extraño que hay en la pared --> mirar grabado
también, se puede ir al bano --> ir al bano
en el bano, se puede pedir una descripcion --> mirar

BITACORA (logros a nivel de desarrollo)

03/09/13
irA() ya logra cambiar la ubicacion del personaje.
04/09/13
irA() a traves de movimientosValidos()
Logra mover al persona de ubicacion, describe la nueva ubicacion
05/09/13
Se depura el procesamiento de las frases entrades a través de la creación de 
función que limpia la entrada de hilativos dejando solo verbo + sustantivo.
ejemplo: ir al bano ---> ["ir", "bano"] | mirar la piedra --> ["mirar"."piedra"]


TAREAS PENDIENTES:
    
    - La descripción de cada hubicación (escena), a través de un título, descripción del lugar, objetos y salidas.
    
    Ejemplo:
    
    BAÑO
    
    Estás en el baño de la casa, es un lugar repuganante, las paredes están cubiertas de algo rugoso color rojo oscuro 
    que parece estár vivo, el olor es pestilente. La tasa del WC está llena a tope de agua-feca y al parecer la cadena
    no se ha tirado por mucho tiempo...  Al Norte vuelves al living de la casa. 
    
   - Crear métodos que manipulen objetos: 
   
   VerbObjetoHub(queverbo,queobjeto):
           obj = queobjeto
        if queverbo in verbos and queobjeto in ubicacion.objetos:
            return true
        else:
            return false
     OTRO EJEMPLO 
     
    if verboObjetoHub("coger","manzana") == True:
        print "Coges la manzana y la guardas en tu mochila"
        ubicacion.objetos.remove(obj)
        inventario.extend(obj)
   
------------------------------ ------------ ---------------------- -----------------------------------

#SIN HILATIVOS!

Ahora usar hilativos.sinHilativos 
Para un mejor manejo de las ordenes entrates! 
Ya no es necesario procesar cada una de las preposiciones y artículos, el método sinHilativos toma la entrada
y le borra todo tipo de articulo, preposicion, etc. Dejando sólo el verbo y el sustantivo:

Ejemplo 

entrada = "ir al bano" 
sinHilativos(entrada) --> ["ir", "bano"]
lo cual permite pasar estos dos elementos de la lista, y procesarlos más cómodamente. 
"""


#INICIO DEL PROGRAMA

## Esta clase es constructora y crea el objeto lugar (hubicaciónes en las que le será posible estar al personaje)

class lugar(object):
    def __init__(self):
        self.titulo = ""
        #Intterruptor de eventos
        self.interruptor = False
        #Descripción tomada por el método setDescripcion()
        self.descripcion = ""
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



#Solo con el afán de ir probando el código, Acá he ido instanciando la clase lugar() en objetos 
# y asignando nuevas propiedades.

#Este método muestra el mensaje de bienvenida al juego -- o descripción 
#de la narración introductoria. 

def inicio():
    print "Este programa es un motor para la creación de Video-Juegos, de tipo \
    \n aventuras de texto o aventuras conversacionales. El cual como objetivo \
    \n principal pretende narrar situaciones en las cuales el usuario (jugador) \
    \n pueda realizar acciones y/o tomar decisiones, escribiendolas como texto \
    \n -- Por el momento puedes hacer algunas pruebas, escribiendo: mirar, ir a, \
    \n encender luz (en tu dormitorio), mirar grabados, ir a bano, etc \n \
    Ejemplo:\n \
    Estás en tu cuarto, has despertado y no recuerdas nada... \n"
    print escena()
        
    

cuarto = lugar()
cuarto.titulo = "Tu dormitorio"
cuarto.salidas = ["bano"]
cuarto.objetos["luz"] = "Tras la puerta de entrada a esta habitación se siente un interruptor"
cuarto.descripcion = "No ves nada está todo oscuro..."


bano = lugar()
bano.titulo = "El bano en suite de tu dormitorio"
bano.salidas = ["cuarto"]
bano.descripcion = "Este lugar apesta... estás en un bano que tiene un olor que se mete en tu nariz y como ácido recorre tu sistema respiratorio. A demás, el lugar tiene unas paredes cubiertas de algo esponjoso que parece estar vivo. La tasa está casi rebalsando de un liquido rojo; la cadena de este al parecer no se ha tirado en siglos. Al sur está tu dormitorio"
#Salidas

#Defino ubicacion inicial
ubicacion = cuarto


#Sin Hilativos

sinHilativos = []

#Estas son las listas de verbos que el programa hasta el momento admite. 

verbo = []
mirar = ["mirar","examinar","explorar"]
verbo.extend(mirar)
comer = ['comer','tragar','ingerir','deborar','engullir']
verbo.extend(comer)
ir = ["ir","moverse","dirigirse","salir","trasladarse","irse","entrar"]
verbo.extend(ir)
activar = ["encender","activar","prender"]
verbo.extend(activar)

#Estos son los artículos y conectores que el porgrama -hasta el día de hoy- admite como válidos. 
articulos = ['el','la','los','las']
preposiciones = ["a","hacia","al"]
#Luego los meto todos en una sola lista llamada conectores, para poder reconocerlos y borrarlos de la entrada.
conectores = []
conectores.extend(articulos)
conectores.extend(preposiciones)

#Objetos

#Funcion de errores en la entrada

def escena():
    TITULO = ubicacion.titulo.upper()
    return "\n"+"Estás en: "+chr(27)+"[0;46m"+TITULO+chr(27)+"[0m"+"\n\n"+ubicacion.descripcion+"\n"



def entradaDesconocida(entrada):
    if entrada[0] not in verbo:
        print "No conozco el verbo %s. Prueba con otro por favor" % entrada[0]
    elif len(entrada) > 1:    
        #Ojo cuarto debe ser una clase intanciada
        if entrada[0] not in ir and entrada[0] in verbo and entrada[1] not in ubicacion.objetos:
            print "No veo aquello que quieres %s" % entrada[0]


#Metodo ir a; ir a el, ir hacia el, etc  etc
def movimientosValidos(entrada):
    if len(entrada) < 3:
        if entrada[0] in ir and entrada[1] in ubicacion.salidas:
            return True
    else:
        return False

#Recibe el verbo ir y cambia la ubicacion; a través de las salidas de cada ubicacion. 
def irA(entrada):
    global ubicacion
    if entrada[0] in ir:
        #Solo un verbo ir[]
        if len(entrada) < 2:
            print "Sí, pero %s a dónde?" % entrada[0]
            #Sin artículo            
        elif movimientosValidos(entrada) == True:
                ubicacion = eval(entrada[len(entrada)-1])
                print escena()
        else:
            print "No te entiendo hacia donde quieres ir"

#Imprime descripciones de los lugares y los objetos            
def descriptor(entrada):
    global ubicacion
    orden = entrada
    ##Muestra la descripción de la ubicacion examinada
    if len(orden) == 1:
        if orden[0] in mirar:
            print escena()
            
    ##Muestra la descripcion del objeto examinado
    elif len(orden) > 1:
        if orden[0] in mirar and orden[1] in ubicacion.objetos:
            print ubicacion.objetos[orden[1]]


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
    if ubicacion == cuarto:
        ##Todos los eventos de esta habitación
        
        #Enciende la luz y agrega nuevos objetos a la habitacion
        if orden[0] in activar and orden[1] == "luz":
            cuarto.descripcion = "\
Es una habitación muy amplia -esto anteriormente había sido tu Dormitorio-\
pero ahora está vacío por completo, y lo más shockiante es que en la pared del \
fondo, en vez de estar la puerta para salir al resto de tu departamento, \
hay unos GRABADOS... A tu espalda sigue estando el bano de tu dormitorio."
            cuarto.objetos["grabados"] = "Son unos extraños grabados tipo indígenas que forman un árbol, y como fruto de éste hay incrustada en la pared una PIEDRA que brilla"                         
            print "Prendes la luz de la habitación, ahora todo se puede ver mucho mejor\nDas un vistaso y te das cuenta que "
            cuarto.getDescripcion()
            
        #No se puede apagar la luz
        elif orden == "apagar la luz":
            print "No deseo apagarla, la verdad es que siento un poco de miedo por la oscuridad"
         
        #Es probable que los métodos intanciables deban estar dentro de la
        #clase constructura.
        
        ##Evetos para bano       
    elif ubicacion == bano:
        pass

inicio()
while True:
    orden = raw_input("Qué haces > ")
    orden = orden.lower()
    orden = orden.split(" ")
    hilativos(orden)
    orden = sinHilativos
    entradaDesconocida(orden)
    eCuarto(orden)
    descriptor(orden)
    irA(orden)
