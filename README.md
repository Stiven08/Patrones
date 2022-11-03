# Patrones


## Singleton
En singleton principalemten solo puede existir una sola instancia, 
esto para asegurar que este patron tengo un punto de acceso global 
en esa misma instancia, donde solo sea tenga acceso a él.


## Fabrica - (Factory)
Este patron se utiliza para la creacion de objetos sin la necesidad de 
especificar la clase exacta, por lo que el objeto que se esta creando 
puede ser intercambiado facilmente. Lo que factory quiere hacer es 
resolver los problemas de la creacion de un objeto concreto de una clase
en la programacion orientado a objetos.


## Fabrica abstracta - (Abstract Factory)
Fabrica abstracta es el tipo de patron creacional 
que permite la creacion en familias o grupos los objetos 
que se relacionan sin laespecificacion de sus clases.


## Prototipo - (Protoype)
Este patron permite la creacion de nuevos objetos que ya antes se habian ideado,
es decir, este patron es de un diseño crecional que permite copiar a objetos ya
existentes sin que el codigo tenga que depender de sus clases.


## Fachada - (Facade)
Este patron es de un diseño estructural ya que este permite una interfaz 
esquematizado a un framework, biblioteca o tambien a otros tipos de clases.


## Decorador - (Decorator)#
Este patron tambine es de diseño estructural, ya que ingresar funciones 
a los objetos, posicionando estos objetos dentro de otros objetos
especiales que contienen las funcionalidades.


## Proxy
Tiene el permiso de la sustitucion de un objeto o tambien para cambiar
su posicion, proxy tiene al margen el acceso del objeto original 
para que asi poder hacer algo antes o despues de que llegue una 
solicitud al objeto original. Proxy se camufla como un onjeto
de la base de datos, y esto ayuda a que por ejemplo se vuelva
rapida y no se congestione varias consultas en la base de datos. 


## Command
A diferencia de los anteriores patrones, este es un diseño de comportamiento
esto lleva a decir que convierte una solicitud a un objeto independiente 
y que este lleva la informacion completa sobre la solicitud. Esto permite a que 
se parametrice los metodos con varios y diferentes solicitudes, poner o retrasar 
la ejecucion de una solicitud y soportar alguna de las operaciones que no se puedan
ejecutar.


## Memento
Memento es un patron que permite la restauracion y permite guardar el 
estado de un objeto sin mostrar los detalles de la implementacion de este.


## Observador - (Observer)
Patron de diseño de comportamiento, permite la definicion de un mecanismo 
de suscripcion que notifica a uno o varios objetos sobre alguna acontecimiento
que se este visualizando.


## Estrategia - (strategy)
Patron de diseño de comportamiento, que define y organiza grupos de algoritmos que
asigna a cada uno de ellos por clases separadas y hace sus objetos intercambiables.


## DAO - (Data Access Object)
DAO o "Objeto de Acceso a Datos" en español, es la relacion que tiene 
una aplicacion hacia uno mucho dispositivos tecnologicos que lleven
a cabo el almacenamiento de datos, esto se puede describir como 
una base de datos o simplemente como un archivo. 
Esto tiene una gran ventaja al utilizar DAO y es que la aplicacion 
donde se este trabajando puede ser modificada o actualizada sin cambiar
partes de la aplicacion.


## Inyección de dependencias - (Dependency injection)
Es el patron de diseño en el que las funciones o los objetos que se 
se encuentran aqui tambien dependen de otros objetos y funciones, 
este patron utiliza mucho mas a menudo marcos especializados
que se llaman "contenedores" para tener mayor flexibilidad y facilidad
en la composicion de un programa. Es el proceso de proporcionar un recurso 
que se requiere en una pieza de codigo.


## #MVC Modelo Vista Controlador - (Model View Controller)
Este patron es utilziado para realizar interfaces de usuario en el cual
divide en partes la logica del programa, se elabora esto para poder asi
mismo separar las representaciones internas de los datos en formas que se 
presentan y son aceptadas por el usuario. Este patron es comunmente utilizado
para el desarrollo de aplicaciones web ya que esto facilita la implementacion
en el patron que se elaboró.
