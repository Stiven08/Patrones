#FABRICA - (FACTORY)
Este patron se utiliza para la creacion de objetos sin la necesidad de 
especificar la clase exacta, por lo que el objeto que se esta creando 
puede ser intercambiado facilmente. Lo que factory quiere hacer es 
resolver los problemas de la creacion de un objeto concreto de una clase
en la programacion orientado a objetos.

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
