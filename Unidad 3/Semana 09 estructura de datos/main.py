# main.py
from producto import Producto  # Importar la clase Producto
from inventario import Inventario  # Importar la clase Inventario

def mostrar_menu():
    """
    Muestra el menú de opciones disponibles para el usuario.
    """
    print("\n--- Menú de Inventario ---")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Mostrar inventario")
    print("6. Salir")

def main():
    """
    Función principal que maneja la interfaz de usuario.
    Permite al usuario interactuar con el inventario a través de un menú.
    """
    inventario = Inventario()  # Crear una instancia del inventario

    while True:
        mostrar_menu()  # Mostrar el menú
        opcion = input("Seleccione una opción: ")  # Leer la opción del usuario

        if opcion == "1":
            # Añadir un nuevo producto
            id = int(input("Ingrese el ID del producto: "))
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            producto = Producto(id, nombre, cantidad, precio)  # Crear el producto
            inventario.añadir_producto(producto)  # Añadir el producto al inventario

        elif opcion == "2":
            # Eliminar un producto por ID
            id = int(input("Ingrese el ID del producto a eliminar: "))
            inventario.eliminar_producto(id)

        elif opcion == "3":
            # Actualizar un producto por ID
            id = int(input("Ingrese el ID del producto a actualizar: "))
            cantidad = input("Ingrese la nueva cantidad (deje en blanco para no cambiar): ")
            precio = input("Ingrese el nuevo precio (deje en blanco para no cambiar): ")
            # Convertir los valores a entero o flotante si se proporcionan
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id, cantidad, precio)

        elif opcion == "4":
            # Buscar productos por nombre
            nombre = input("Ingrese el nombre o parte del nombre a buscar: ")
            resultados = inventario.buscar_por_nombre(nombre)
            if resultados:
                for producto in resultados:
                    print(producto)
            else:
                print("No se encontraron productos.")

        elif opcion == "5":
            # Mostrar todos los productos en el inventario
            inventario.mostrar_inventario()

        elif opcion == "6":
            # Salir del programa
            print("Saliendo del programa...")
            break

        else:
            # Opción no válida
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()  # Ejecutar la función principal