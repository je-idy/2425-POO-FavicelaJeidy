# Programa: Sistema de una tienda
# Descripción: Este programa simula un sistema de una tienda utilizando los principios de POO.

# Clase Producto: representa un producto que la tienda tiene disponible para la venta.
class Producto:
    def __init__(self, nombre, precio, stock):
        """
        Constructor de la clase Producto.
        :param nombre: Nombre del producto (str)
        :param precio: Precio del producto (float)
        :param stock: Cantidad disponible en inventario (int)
        """
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __str__(self):
        """Devuelve una representación legible del producto."""
        return f"Producto: {self.nombre}, Precio: ${self.precio:.2f}, Stock: {self.stock} unidades"

    def actualizar_stock(self, cantidad):
        """
        Actualiza el stock del producto.
        :param cantidad: Cantidad a restar del stock (int)
        """
        if cantidad > self.stock:
            raise ValueError("No hay suficiente stock disponible.")
        self.stock -= cantidad

# Clase Tienda: representa la tienda con una lista de productos y métodos para la gestión de ventas.
class Tienda:
    def __init__(self, nombre):
        """
        Constructor de la clase Tienda.
        :param nombre: Nombre de la tienda (str)
        """
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, producto):
        """
        Agrega un producto al inventario de la tienda.
        :param producto: Objeto Producto a agregar
        """
        self.productos.append(producto)

    def mostrar_productos(self):
        """
        Muestra la lista de productos disponibles en la tienda.
        """
        if not self.productos:
            print("No hay productos disponibles en la tienda.")
        else:
            for producto in self.productos:
                print(producto)

    def vender_producto(self, nombre_producto, cantidad):
        """
        Realiza la venta de un producto, actualizando el stock disponible.
        :param nombre_producto: Nombre del producto a vender (str)
        :param cantidad: Cantidad a vender (int)
        """
        for producto in self.productos:
            if producto.nombre == nombre_producto:
                if producto.stock >= cantidad:
                    producto.actualizar_stock(cantidad)
                    total = producto.precio * cantidad
                    print(f"Venta realizada: {cantidad} x {producto.nombre} por un total de ${total:.2f}")
                else:
                    print("Stock insuficiente para realizar la venta.")
                return
        print("Producto no encontrado.")

# Ejemplo de uso
if __name__ == "__main__":
    # Crear una instancia de la tienda
    mi_tienda = Tienda("Tienda Tech")

    # Crear productos
    producto1 = Producto("Laptop", 800.00, 10)
    producto2 = Producto("Mouse", 25.50, 50)
    producto3 = Producto("Teclado", 45.00, 30)

    # Agregar productos a la tienda
    mi_tienda.agregar_producto(producto1)
    mi_tienda.agregar_producto(producto2)
    mi_tienda.agregar_producto(producto3)

    # Mostrar productos disponibles
    print("Productos disponibles en la tienda:")
    mi_tienda.mostrar_productos()

    print("\nIntentando realizar una venta:")
    # Realizar una venta
    mi_tienda.vender_producto("Laptop", 2)

    print("\nProductos disponibles tras la venta:")
    # Mostrar productos disponibles tras la venta
    mi_tienda.mostrar_productos()
