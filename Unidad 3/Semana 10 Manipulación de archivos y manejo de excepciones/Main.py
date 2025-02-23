import os

class Inventario:
    def __init__(self, archivo="inventario.txt"):
        """
        Constructor de la clase Inventario.
        Inicializa la lista de productos y carga los datos desde el archivo.
        """
        self.archivo = archivo
        self.productos = []
        self.cargar_inventario()

    def cargar_inventario(self):
        """
        Carga los productos desde el archivo de inventario.
        Si el archivo no existe, se crea uno nuevo.
        """
        try:
            with open(self.archivo, "r") as file:
                for linea in file:
                    id, nombre, cantidad, precio = linea.strip().split(",")
                    producto = Producto(int(id), nombre, int(cantidad), float(precio))
                    self.productos.append(producto)
            print("Inventario cargado exitosamente.")
        except FileNotFoundError:
            print("Archivo de inventario no encontrado. Se creará uno nuevo.")
            open(self.archivo, "w").close()  # Crear archivo si no existe.
        except Exception as e:
            print(f"Error al cargar el inventario: {e}")

    def guardar_inventario(self):
        """
        Guarda los productos en el archivo de inventario.
        """
        try:
            with open(self.archivo, "w") as file:
                for producto in self.productos:
                    file.write(f"{producto.get_id()},{producto.get_nombre()},{producto.get_cantidad()},{producto.get_precio()}\n")
            print("Inventario guardado exitosamente.")
        except PermissionError:
            print("Error: No tienes permisos para escribir en el archivo.")
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")

    def añadir_producto(self, producto):
        """
        Añade un nuevo producto al inventario y guarda los cambios en el archivo.
        """
        if any(p.get_id() == producto.get_id() for p in self.productos):
            print("Error: El ID del producto ya existe.")
        else:
            self.productos.append(producto)
            self.guardar_inventario()
            print("Producto añadido con éxito.")

    def eliminar_producto(self, id):
        """
        Elimina un producto del inventario por su ID y guarda los cambios en el archivo.
        """
        producto = self.buscar_producto_por_id(id)
        if producto:
            self.productos.remove(producto)
            self.guardar_inventario()
            print("Producto eliminado con éxito.")
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        """
        Actualiza la cantidad o el precio de un producto por su ID y guarda los cambios en el archivo.
        """
        producto = self.buscar_producto_por_id(id)
        if producto:
            if cantidad is not None:
                producto.set_cantidad(cantidad)
            if precio is not None:
                producto.set_precio(precio)
            self.guardar_inventario()
            print("Producto actualizado con éxito.")
        else:
            print("Error: Producto no encontrado.")

    def buscar_producto_por_id(self, id):
        """
        Busca un producto en el inventario por su ID.
        Devuelve el producto si se encuentra, o None si no existe.
        """
        for producto in self.productos:
            if producto.get_id() == id:
                return producto
        return None

    def buscar_productos_por_nombre(self, nombre):
        """
        Busca productos en el inventario por nombre.
        Devuelve una lista de productos cuyos nombres contienen la cadena proporcionada.
        """
        return [producto for producto in self.productos if nombre.lower() in producto.get_nombre().lower()]

    def mostrar_productos(self):
        """
        Muestra todos los productos en el inventario.
        Si el inventario está vacío, muestra un mensaje indicándolo.
        """
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos:
                print(producto)