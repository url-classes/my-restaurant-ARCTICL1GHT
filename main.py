from menu import Menu
from lunar import Lunar
from venus import Venus
from mercurio import Mercurio
from pluton import Pluton


pedido: Menu = Lunar()
pedido.pedido()
print(f"Precio: {pedido.precio()}")
print(f"Tiempo: {pedido.tiempo()}")
