# Inyección de dependencias (Dependency injection)
Es el patron de diseño en el que las funciones o los objetos que se 
se encuentran aqui tambien dependen de otros objetos y funciones, 
este patron utiliza mucho mas a menudo marcos especializados
que se llaman "contenedores" para tener mayor flexibilidad y facilidad
en la composicion de un programa. Es el proceso de proporcionar un recurso 
que se requiere en una pieza de codigo.

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
