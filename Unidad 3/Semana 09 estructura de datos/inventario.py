# inventario.py
from producto import Producto  # Importar la clase Producto


class Inventario:
    def __init__(self):
        """
        Constructor de la clase Inventario.
        Inicializa una lista vacía para almacenar los productos.
        """
        self.productos = []

    def añadir_producto(self, producto):
        """
        Añade un nuevo producto al inventario.
        Verifica que el ID del producto sea único antes de añadirlo.
        :param producto: Objeto de la clase Producto.
        """
        # Verificar si el ID ya existe en la lista de productos
        if any(p.get_id() == producto.get_id() for p in self.productos):
            print("Error: El ID del producto ya existe.")
        else:
            self.productos.append(producto)  # Añadir el producto a la lista
            print("Producto añadido correctamente.")

    def eliminar_producto(self, id):
        """
        Elimina un producto del inventario por su ID.
        :param id: ID del producto a eliminar.
        """
        # Buscar el producto por su ID y eliminarlo
        for producto in self.productos:
            if producto.get_id() == id:
                self.productos.remove(producto)
                print("Producto eliminado correctamente.")
                return
        # Si no se encuentra el producto, mostrar un mensaje de error
        print("Error: No se encontró un producto con ese ID.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        """
        Actualiza la cantidad o el precio de un producto por su ID.
        :param id: ID del producto a actualizar.
        :param cantidad: Nueva cantidad (opcional).
        :param precio: Nuevo precio (opcional).
        """
        # Buscar el producto por su ID
        for producto in self.productos:
            if producto.get_id() == id:
                # Actualizar la cantidad si se proporciona un valor
                if cantidad is not None:
                    producto.set_cantidad(cantidad)
                # Actualizar el precio si se proporciona un valor
                if precio is not None:
                    producto.set_precio(precio)
                print("Producto actualizado correctamente.")
                return
        # Si no se encuentra el producto, mostrar un mensaje de error
        print("Error: No se encontró un producto con ese ID.")

    def buscar_por_nombre(self, nombre):
        """
        Busca productos en el inventario por nombre o parte del nombre.
        :param nombre: Nombre o parte del nombre a buscar.
        :return: Lista de productos que coinciden con el nombre.
        """
        # Filtrar productos que contienen el nombre buscado (ignorando mayúsculas/minúsculas)
        resultados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        return resultados

    def mostrar_inventario(self):
        """
        Muestra todos los productos en el inventario.
        Si el inventario está vacío, muestra un mensaje indicándolo.
        """
        if not self.productos:
            print("El inventario está vacío.")
        else:
            # Recorrer y mostrar cada producto en la lista
            for producto in self.productos:
                print(producto)