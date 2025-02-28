import json


# Importamos la librería json para guardar y cargar el inventario en un archivo
import json

# Clase Producto: Representa un producto en el inventario
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        """
        Constructor de la clase Producto.
        :param id_producto: Identificador único del producto.
        :param nombre: Nombre del producto.
        :param cantidad: Cantidad disponible en el inventario.
        :param precio: Precio unitario del producto.
        """
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        """
        Representación en cadena del producto.
        :return: Cadena formateada con los detalles del producto.
        """
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"


# Clase Inventario: Gestiona la colección de productos
class Inventario:
    def __init__(self):
        """
        Constructor de la clase Inventario.
        Inicializa un diccionario vacío para almacenar los productos.
        """
        self.productos = {}  # Diccionario donde la clave es el ID del producto

    def agregar_producto(self, producto):
        """
        Agrega un nuevo producto al inventario.
        :param producto: Objeto de la clase Producto.
        """
        if producto.id_producto in self.productos:
            print("Error: Ya existe un producto con este ID.")
        else:
            self.productos[producto.id_producto] = producto
            print(f"Producto '{producto.nombre}' agregado correctamente.")

    def eliminar_producto(self, id_producto):
        """
        Elimina un producto del inventario por su ID.
        :param id_producto: ID del producto a eliminar.
        """
        if id_producto in self.productos:
            producto_eliminado = self.productos.pop(id_producto)
            print(f"Producto '{producto_eliminado.nombre}' eliminado correctamente.")
        else:
            print("Error: No se encontró un producto con este ID.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        """
        Actualiza la cantidad o el precio de un producto.
        :param id_producto: ID del producto a actualizar.
        :param cantidad: Nueva cantidad (opcional).
        :param precio: Nuevo precio (opcional).
        """
        if id_producto in self.productos:
            producto = self.productos[id_producto]
            if cantidad is not None:
                producto.cantidad = cantidad
            if precio is not None:
                producto.precio = precio
            print(f"Producto '{producto.nombre}' actualizado correctamente.")
        else:
            print("Error: No se encontró un producto con este ID.")

    def buscar_por_nombre(self, nombre):
        """
        Busca productos por nombre.
        :param nombre: Nombre o parte del nombre del producto a buscar.
        """
        resultados = [producto for producto in self.productos.values() if nombre.lower() in producto.nombre.lower()]
        if resultados:
            print("Resultados de la búsqueda:")
            for producto in resultados:
                print(producto)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_inventario(self):
        """
        Muestra todos los productos en el inventario.
        """
        if self.productos:
            print("Inventario actual:")
            for producto in self.productos.values():
                print(producto)
        else:
            print("El inventario está vacío.")

    def guardar_inventario(self, archivo):
        """
        Guarda el inventario en un archivo JSON.
        :param archivo: Nombre del archivo donde se guardará el inventario.
        """
        inventario_serializable = {id_producto: {"nombre": producto.nombre, "cantidad": producto.cantidad, "precio": producto.precio}
                                  for id_producto, producto in self.productos.items()}
        with open(archivo, 'w') as f:
            json.dump(inventario_serializable, f)
        print(f"Inventario guardado en '{archivo}'.")

    def cargar_inventario(self, archivo):
        """
        Carga el inventario desde un archivo JSON.
        :param archivo: Nombre del archivo desde donde se cargará el inventario.
        """
        try:
            with open(archivo, 'r') as f:
                inventario_serializable = json.load(f)
            self.productos = {id_producto: Producto(id_producto, datos["nombre"], datos["cantidad"], datos["precio"])
                               for id_producto, datos in inventario_serializable.items()}
            print(f"Inventario cargado desde '{archivo}'.")
        except FileNotFoundError:
            print("Error: El archivo no existe.")


# Función para mostrar el menú de opciones
def mostrar_menu():
    """
    Muestra el menú de opciones para el usuario.
    """
    print("\n--- Menú de Gestión de Inventario ---")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Mostrar inventario")
    print("6. Guardar inventario")
    print("7. Cargar inventario")
    print("8. Salir")


# Función principal
def main():
    """
    Función principal que ejecuta el programa.
    """
    inventario = Inventario()  # Crea una instancia del inventario
    archivo_inventario = "inventario.json"  # Nombre del archivo para guardar y cargar datos

    while True:
        mostrar_menu()  # Muestra el menú
        opcion = input("Seleccione una opción: ")  # Solicita la opción al usuario

        if opcion == "1":  # Agregar producto
            id_producto = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == "2":  # Eliminar producto
            id_producto = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":  # Actualizar producto
            id_producto = input("Ingrese el ID del producto a actualizar: ")
            cantidad = input("Ingrese la nueva cantidad (deje vacío para no cambiar): ")
            precio = input("Ingrese el nuevo precio (deje vacío para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)

        elif opcion == "4":  # Buscar producto por nombre
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_por_nombre(nombre)

        elif opcion == "5":  # Mostrar inventario
            inventario.mostrar_inventario()

        elif opcion == "6":  # Guardar inventario
            inventario.guardar_inventario(archivo_inventario)

        elif opcion == "7":  # Cargar inventario
            inventario.cargar_inventario(archivo_inventario)

        elif opcion == "8":  # Salir
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")


# Punto de entrada del programa
if __name__ == "__main__":
    main()