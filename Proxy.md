# PROXY
Tiene el permiso de la sustitucion de un objeto o tambien para cambiar
su posicion, proxy tiene al margen el acceso del objeto original 
para que asi poder hacer algo antes o despues de que llegue una 
solicitud al objeto original. Proxy se camufla como un onjeto
de la base de datos, y esto ayuda a que por ejemplo se vuelva
rapida y no se congestione varias consultas en la base de datos. 

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
