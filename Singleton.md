# SINGLETON
En singleton principalemten solo puede existir una sola instancia, 
esto para asegurar que este patron tengo un punto de acceso global 
en esa misma instancia, donde solo sea tenga acceso a él.

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
