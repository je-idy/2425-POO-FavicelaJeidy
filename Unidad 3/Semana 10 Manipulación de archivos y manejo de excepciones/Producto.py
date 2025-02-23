def mostrar_menu():
    """
    Muestra el menú de opciones en la consola.
    """
    print("\n--- Menú de Gestión de Inventario ---")
    print("1. Añadir Producto")
    print("2. Eliminar Producto")
    print("3. Actualizar Producto")
    print("4. Buscar Producto por Nombre")
    print("5. Mostrar Todos los Productos")
    print("6. Salir")

def main():
    """
    Función principal que maneja la interacción con el usuario.
    Permite al usuario realizar operaciones en el inventario a través de un menú.
    """
    inventario = Inventario()  # Crea una instancia del inventario.

    while True:
        mostrar_menu()  # Muestra el menú.
        opcion = input("Seleccione una opción: ")  # Solicita la opción al usuario.

        if opcion == "1":
            # Añadir un nuevo producto.
            try:
                id = int(input("Ingrese el ID del producto: "))
                nombre = input("Ingrese el nombre del producto: ")
                cantidad = int(input("Ingrese la cantidad del producto: "))
                precio = float(input("Ingrese el precio del producto: "))
                producto = Producto(id, nombre, cantidad, precio)
                inventario.añadir_producto(producto)
            except ValueError:
                print("Error: Ingrese valores válidos para ID, cantidad y precio.")

        elif opcion == "2":
            # Eliminar un producto por ID.
            try:
                id = int(input("Ingrese el ID del producto a eliminar: "))
                inventario.eliminar_producto(id)
            except ValueError:
                print("Error: Ingrese un ID válido.")

        elif opcion == "3":
            # Actualizar un producto por ID.
            try:
                id = int(input("Ingrese el ID del producto a actualizar: "))
                cantidad = input("Ingrese la nueva cantidad (deje en blanco para no cambiar): ")
                precio = input("Ingrese el nuevo precio (deje en blanco para no cambiar): ")
                cantidad = int(cantidad) if cantidad else None
                precio = float(precio) if precio else None
                inventario.actualizar_producto(id, cantidad, precio)
            except ValueError:
                print("Error: Ingrese valores válidos para cantidad y precio.")

        elif opcion == "4":
            # Buscar productos por nombre.
            nombre = input("Ingrese el nombre del producto a buscar: ")
            productos = inventario.buscar_productos_por_nombre(nombre)
            if productos:
                for producto in productos:
                    print(producto)
            else:
                print("No se encontraron productos con ese nombre.")

        elif opcion == "5":
            # Mostrar todos los productos en el inventario.
            inventario.mostrar_productos()

        elif opcion == "6":
            # Salir del programa.
            print("Saliendo del sistema...")
            break

        else:
            # Opción no válida.
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()  # Ejecuta la función principal.