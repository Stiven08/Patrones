# COMMAND
A diferencia de los anteriores patrones, este es un diseño de comportamiento
esto lleva a decir que convierte una solicitud a un objeto independiente 
y que este lleva la informacion completa sobre la solicitud. Esto permite a que 
se parametrice los metodos con varios y diferentes solicitudes, poner o retrasar 
la ejecucion de una solicitud y soportar alguna de las operaciones que no se puedan
ejecutar.

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
