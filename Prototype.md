# Prototipo - Prototype
Este patron permite la creacion de nuevos objetos que ya antes se habian ideado,
es decir, este patron es de un diseño crecional que permite copiar a objetos ya
existentes sin que el codigo tenga que depender de sus clases.

import copy
class Prototype:
     pass

def main():
    prototype = Prototype()
    prototype_copy = copy.deepcopy(prototype)

if __name__ == "__main__":
    main()
