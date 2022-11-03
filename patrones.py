#PATRONES DE DISEÑO#

#SINGLETON#

#En singleton principalemten solo puede existir una sola instancia, 
# esto para asegurar que este patron tengo un punto de acceso global 
# en esa misma instancia, donde solo sea tenga acceso a él.


class Singleton(type):

    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance

class MyClass(metaclass=Singleton):
    
    pass
def main():
    m1 = MyClass()
    m2 = MyClass()
    assert m1 is m2

if __name__ == "__main__":
    main()


#FABRICA - (FACTORY)#
#Este patron se utiliza para la creacion de objetos sin la necesidad de 
#especificar la clase exacta, por lo que el objeto que se esta creando 
#puede ser intercambiado facilmente. Lo que factory quiere hacer es 
#resolver los problemas de la creacion de un objeto concreto de una clase
#en la programacion orientado a objetos.

import abc

class Creator(metaclass=abc.ABCMeta):
    def __init__(self):
        self.product = self._factory_method()

    @abc.abstractmethod
    def _factory_method(self):
        pass

    def some_operation(self):
        self.product.interface()

class ConcreteCreator1(Creator):
    def _factory_method(self):
        return ConcreteProduct1()

class ConcreteCreator2(Creator):
    def _factory_method(self):
        return ConcreteProduct2()

class Product(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def interface(self):
        pass

class ConcreteProduct1(Product):
    def interface(self):
        pass

class ConcreteProduct2(Product):
    def interface(self):
        pass

def main():
    concrete_creator = ConcreteCreator1()
    concrete_creator.product.interface()
    concrete_creator.some_operation()

if __name__ == "__main__":
    main()
    

#FABRICA ABSTRACTA - (ABSTRACT FACTORY)#
#Fabrica abstracta es el tipo de patron creacional 
#que permite la creacion en familias o grupos los objetos 
#que se relacionan sin laespecificacion de sus clases.

import abc
class AbstractFactory(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create_product_a(self):
        pass

    @abc.abstractmethod
    def create_product_b(self):
        pass

class ConcreteFactory1(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA1()

    def create_product_b(self):
        return ConcreteProductB1()

class ConcreteFactory2(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA2()

    def create_product_b(self):
        return ConcreteProductB2()
    
class AbstractProductA(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def interface_a(self):
        pass

class ConcreteProductA1(AbstractProductA):
    def interface_a(self):
        pass

class ConcreteProductA2(AbstractProductA):
    def interface_a(self):
        pass

class AbstractProductB(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def interface_b(self):
        pass

class ConcreteProductB1(AbstractProductB):
    def interface_b(self):
        pass

class ConcreteProductB2(AbstractProductB):
    def interface_b(self):
        pass

def main():
    for factory in (ConcreteFactory1(), ConcreteFactory2()):
        product_a = factory.create_product_a()
        product_b = factory.create_product_b()
        product_a.interface_a()
        product_b.interface_b()

if __name__ == "__main__":
    main()


#PROTOTIPO - (PROTOTYPE)#
#Este patron permite la creacion de nuevos objetos que ya antes se habian ideado,
#es decir, este patron es de un diseño crecional que permite copiar a objetos ya
#existentes sin que el codigo tenga que depender de sus clases.

import copy
class Prototype:
     pass

def main():
    prototype = Prototype()
    prototype_copy = copy.deepcopy(prototype)

if __name__ == "__main__":
    main()
    
#FACHADA - (FACADE)#
#Este patron es de un diseño estructural ya que este permite una interfaz 
#esquematizado a un framework, biblioteca o tambien a otros tipos de clases.

class Facade:
    def __init__(self):
        self._subsystem_1 = Subsystem1()
        self._subsystem_2 = Subsystem2()
    
    def operation(self):
        self._subsystem_1.operation1()
        self._subsystem_1.operation2()
        self._subsystem_2.operation1()
        self._subsystem_2.operation2()
    
class Subsystem1:
    def operation1(self):
        pass

    def operation2(self):
        pass
    
class Subsystem2:
    def operation1(self):
        pass

    def operation2(self):
        pass
    
def main():
    facade = Facade()
    facade.operation()

if __name__ == "__main__":
    main()


#DECORADOR - (DECORATOR)#
#Este patron tambine es de diseño estructural, ya que ingresar funciones 
#a los objetos, posicionando estos objetos dentro de otros objetos
#especiales que contienen las funcionalidades.

import abc
class Component(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def operation(self):
        pass

class Decorator(Component, metaclass=abc.ABCMeta):
    def __init__(self, component):
        self._component = component

    @abc.abstractmethod
    def operation(self):
        pass

class ConcreteDecoratorA(Decorator):
    def operation(self):
    #...
        self._component.operation()
    #...
    
class ConcreteDecoratorB(Decorator):
    def operation(self):
        # ...
        self._component.operation()
        # ...

class ConcreteComponent(Component):
    def operation(self):
        pass

def main():
    concrete_component = ConcreteComponent()
    concrete_decorator_a = ConcreteDecoratorA(concrete_component)
    concrete_decorator_b = ConcreteDecoratorB(concrete_decorator_a)
    concrete_decorator_b.operation()

if __name__ == "__main__":
    main()


#PROXY#
#Tiene el permiso de la sustitucion de un objeto o tambien para cambiar
#su posicion, proxy tiene al margen el acceso del objeto original 
#para que asi poder hacer algo antes o despues de que llegue una 
#solicitud al objeto original. Proxy se camufla como un onjeto
#de la base de datos, y esto ayuda a que por ejemplo se vuelva
#rapida y no se congestione varias consultas en la base de datos. 

import abc
class Subject(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def request(self):
        pass

class Proxy(Subject):
    def __init__(self, real_subject):
        self._real_subject = real_subject

    def request(self):
        # ...
        self._real_subject.request()
        # ...

class RealSubject(Subject):
    def request(self):
        pass

def main():
    real_subject = RealSubject()
    proxy = Proxy(real_subject)
    proxy.request()

if __name__ == "__main__":
    main()
    

#COMMAND#
#A diferencia de los anteriores patrones, este es un diseño de comportamiento
#esto lleva a decir que convierte una solicitud a un objeto independiente 
#y que este lleva la informacion completa sobre la solicitud. Esto permite a que 
#se parametrice los metodos con varios y diferentes solicitudes, poner o retrasar 
#la ejecucion de una solicitud y soportar alguna de las operaciones que no se puedan
#ejecutar.

import abc
class Invoker:
    def __init__(self):
        self._commands = []

    def store_command(self, command):
        self._commands.append(command)

    def execute_commands(self):
        for command in self._commands:
            command.execute()

class Command(metaclass=abc.ABCMeta):
    def __init__(self, receiver):
        self._receiver = receiver

    @abc.abstractmethod
    def execute(self):
        pass

class ConcreteCommand(Command):
    def execute(self):
        self._receiver.action()

class Receiver:
    def action(self):
        pass

def main():
    receiver = Receiver()
    concrete_command = ConcreteCommand(receiver)
    invoker = Invoker()
    invoker.store_command(concrete_command)
    invoker.execute_commands()

if __name__ == "__main__":
    main()
    

#MEMENTO#
#Memento es un patron que permite la restauracion y permite guardar el 
#estado de un objeto sin mostrar los detalles de la implementacion de este.

import pickle
class Originator:
    def __init__(self):
        self._state = None

    def set_memento(self, memento):
        previous_state = pickle.loads(memento)
        vars(self).clear()
        vars(self).update(previous_state)

    def create_memento(self):
        return pickle.dumps(vars(self))
    
def main():
    originator = Originator()
    memento = originator.create_memento()
    originator._state = True
    originator.set_memento(memento)

if __name__ == "__main__":
    main()
    

#OBSERVADOR - (OBSERVER)#
#Patron de diseño de comportamiento, permite la definicion de un mecanismo 
#de suscripcion que notifica a uno o varios objetos sobre alguna acontecimiento
#que se este visualizando.

import abc
class Subject:
    def __init__(self):
        self._observers = set()
        self._subject_state = None
    
    def attach(self, observer):
        observer._subject = self
        self._observers.add(observer)

    def detach(self, observer):
        observer._subject = None
        self._observers.discard(observer)

    def _notify(self):
        for observer in self._observers:
            observer.update(self._subject_state)

    @property
    def subject_state(self):
        return self._subject_state
    
    @subject_state.setter
    def subject_state(self, arg):
        self._subject_state = arg
        self._notify()
        
class Observer(metaclass=abc.ABCMeta):
    def __init__(self):
        self._subject = None
        self._observer_state = None

    @abc.abstractmethod
    def update(self, arg):
        pass
    
class ConcreteObserver(Observer):
    def update(self, arg):
        self._observer_state = arg
        # ...

def main():
    subject = Subject()
    concrete_observer = ConcreteObserver()
    subject.attach(concrete_observer)
    subject.subject_state = 123

if __name__ == "__main__":
    main()
    

#ESTRATEGIA - (STRATEGY)#
#Patron de diseño de comportamiento, que define y organiza grupos de algoritmos que
#asigna a cada uno de ellos por clases separadas y hace sus objetos intercambiables.

import abc
class Context:
    def __init__(self, strategy):
        self._strategy = strategy

    def context_interface(self):
        self._strategy.algorithm_interface()
    
class Strategy(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def algorithm_interface(self):
        pass

class ConcreteStrategyA(Strategy):
    def algorithm_interface(self):
        pass

class ConcreteStrategyB(Strategy):
    def algorithm_interface(self):
        pass
    
def main():
    concrete_strategy_a = ConcreteStrategyA()
    context = Context(concrete_strategy_a)
    context.context_interface()
    
if __name__ == "__main__":
    main()


#DAO (Data Access Object)#
#DAO o "Objeto de Acceso a Datos" en español, es la relacion que tiene 
#una aplicacion hacia uno mucho dispositivos tecnologicos que lleven
#a cabo el almacenamiento de datos, esto se puede describir como 
#una base de datos o simplemente como un archivo. 
#Esto tiene una gran ventaja al utilizar DAO y es que la aplicacion 
#donde se este trabajando puede ser modificada o actualizada sin cambiar
#partes de la aplicacion.


public void createUser(NewUserRequestDTO dto) {  

    UserDAO userDAO = new UserDAOImpl();  
        
    if(userDAO.findByUsername(dto.getUsername()) != null) {  
        throw new RuntimeException("Username already exists");  
    }  
        
    UserConverter usrConverter = new UserConverter();  
    User user = surConverter.fromDto(dto);  
    
    usrDAO.save(user);  
}

#Inyección de dependencias (Dependency injection)#
#Es el patron de diseño en el que las funciones o los objetos que se 
#se encuentran aqui tambien dependen de otros objetos y funciones, 
#este patron utiliza mucho mas a menudo marcos especializados
#que se llaman "contenedores" para tener mayor flexibilidad y facilidad
#en la composicion de un programa. Es el proceso de proporcionar un recurso 
#que se requiere en una pieza de codigo.

import os

class ApiClient:

    def __init__(self, api_key: str, timeout: int) -> None:
        self.api_key = api_key  # <-- dependency is injected
        self.timeout = timeout  # <-- dependency is injected

class Service:

    def __init__(self, api_client: ApiClient) -> None:
        self.api_client = api_client  # <-- dependency is injected

def main(service: Service) -> None:  # <-- dependency is injected
    ...

if __name__ == "__main__":
    main(
        service=Service(
            api_client=ApiClient(
                api_key=os.getenv("API_KEY"),
                timeout=int(os.getenv("TIMEOUT")),
            ),
        ),
    )



#MVC Modelo Vista Controlador (Model View Controller)#
#Este patron es utilziado para realizar interfaces de usuario en el cual
#divide en partes la logica del programa, se elabora esto para poder asi
#mismo separar las representaciones internas de los datos en formas que se 
#presentan y son aceptadas por el usuario. Este patron es comunmente utilizado
#para el desarrollo de aplicaciones web ya que esto facilita la implementacion
#en el patron que se elaboro.


def main():

    my_items = [
        {'name': 'bread', 'price': 0.5, 'quantity': 20},
        {'name': 'milk', 'price': 1.0, 'quantity': 10},
        {'name': 'wine', 'price': 10.0, 'quantity': 5},
    ]

    create_items(my_items)
    create_item('beer', price=3.0, quantity=15)

   
    print('READ items')
    print(read_items())
    print(read_item('bread'))

    # UPDATE
    print('UPDATE bread')
    update_item('bread', price=2.0, quantity=30)
    print(read_item('bread'))

    # DELETE
    print('DELETE beer')
    delete_item('beer')

    print('READ items')
    print(read_items())

if __name__ == '__main__':
    main()

