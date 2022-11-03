# MVC Modelo Vista Controlador (Model View Controller)
Este patron es utilziado para realizar interfaces de usuario en el cual
divide en partes la logica del programa, se elabora esto para poder asi
mismo separar las representaciones internas de los datos en formas que se 
presentan y son aceptadas por el usuario. Este patron es comunmente utilizado
para el desarrollo de aplicaciones web ya que esto facilita la implementacion
en el patron que se elaboro.


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
