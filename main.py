import time
from menu import Menu
from lunar import Lunar
from venus import Venus
from mercurio import Mercurio
from pluton import Pluton

bandera: bool = True
total: float = 0
tiempo: float = 0

while bandera:
    print("Menu")
    print("1. Lunar")
    print("2. Venus")
    print("3. Pluton")
    print("4. Mercurio")
    print("0. Finalizar pedido")
    op = int(input("Ingrese opcion \n"))
    if op == 1:
        pedido: Menu = Lunar()
        print(f"Menu: {pedido.__class__.__name__}")
        print("Contenido:")
        print("Hamburguesa: Hamburguesa con queso")
        print("Bebida: Coca-Cola")
        print("Complemento: Papas")
        print("Postre: Helado")
        pedido.pedido()
        print(f"Precio: {pedido.precio()}")
        print(f"Tiempo: {pedido.tiempo()} \n")
        total += pedido.precio()
        tiempo += pedido.tiempo()

    elif op == 2:
        pedido: Menu = Venus()
        print(f"Menu: {pedido.__class__.__name__}")
        print("Contenido:")
        print("Hamburguesa: Hamburguesa con tocino")
        print("Bebida: Coca-Cola")
        print("Complemento: Ensalada")
        print("Postre: Gelatina")
        pedido.pedido()
        print(f"Precio: {pedido.precio()}")
        print(f"Tiempo: {pedido.tiempo()}")
        total += pedido.precio()
        tiempo += pedido.tiempo()

    elif op == 3:
        pedido: Menu = Pluton()
        print(f"Menu: {pedido.__class__.__name__}")
        print("Contenido:")
        print("Hamburguesa: Hamburguesa con queso y tocino")
        print("Bebida: Te")
        print("Complemento: Ensalada")
        print("Postre: Galleta")
        pedido.pedido()
        print(f"Precio: {pedido.precio()}")
        print(f"Tiempo: {pedido.tiempo()}")
        total += pedido.precio()
        tiempo += pedido.tiempo()

    elif op == 4:
        pedido: Menu = Mercurio()
        print(f"Menu: {pedido.__class__.__name__}")
        print("Contenido:")
        print("Hamburguesa: Hamburguesa con queso doble")
        print("Bebida: Cafe")
        print("Complemento: Aderezo")
        print("Postre: Gelatina")
        pedido.pedido()
        print(f"Precio: {pedido.precio()}")
        print(f"Tiempo: {pedido.tiempo()}")
        total += pedido.precio()
        tiempo += pedido.tiempo()

    elif op == 0:
        print(f"Se esta preparando su pedido")
        print(f"Total: Q{total}")
        print(f"Demorara: {tiempo} segundos")
        time.sleep(tiempo)
        bandera = False

    else:
        print("Valor incorrecto")


