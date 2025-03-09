# Clase Libro: Representa un libro con atributos como título, autor, categoría y ISBN.
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Usamos una tupla para almacenar el autor y el título, ya que estos no cambiarán una vez creados.
        self.titulo_autor = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"Título: {self.titulo_autor[0]}, Autor: {self.titulo_autor[1]}, Categoría: {self.categoria}, ISBN: {self.isbn}"


# Clase Usuario: Representa a un usuario de la biblioteca.
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        # Lista para almacenar los libros actualmente prestados al usuario.
        self.libros_prestados = []

    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.id_usuario}, Libros Prestados: {len(self.libros_prestados)}"


# Clase Biblioteca: Gestiona las colecciones de libros, usuarios y préstamos.
class Biblioteca:
    def __init__(self):
        # Diccionario para almacenar los libros disponibles, con el ISBN como clave y el objeto Libro como valor.
        self.libros_disponibles = {}
        # Conjunto para manejar los IDs de usuarios únicos.
        self.usuarios_registrados = set()
        # Diccionario para almacenar los usuarios registrados, con el ID de usuario como clave y el objeto Usuario como valor.
        self.usuarios = {}

    # Método para añadir un libro a la biblioteca.
    def añadir_libro(self, libro):
        if libro.isbn in self.libros_disponibles:
            print(f"El libro con ISBN {libro.isbn} ya existe en la biblioteca.")
        else:
            self.libros_disponibles[libro.isbn] = libro
            print(f"Libro '{libro.titulo_autor[0]}' añadido correctamente.")

    # Método para quitar un libro de la biblioteca.
    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            del self.libros_disponibles[isbn]
            print(f"Libro con ISBN {isbn} eliminado correctamente.")
        else:
            print(f"El libro con ISBN {isbn} no existe en la biblioteca.")

    # Método para registrar un nuevo usuario.
    def registrar_usuario(self, usuario):
        if usuario.id_usuario in self.usuarios_registrados:
            print(f"El usuario con ID {usuario.id_usuario} ya está registrado.")
        else:
            self.usuarios_registrados.add(usuario.id_usuario)
            self.usuarios[usuario.id_usuario] = usuario
            print(f"Usuario '{usuario.nombre}' registrado correctamente.")

    # Método para dar de baja a un usuario.
    def dar_de_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios_registrados:
            self.usuarios_registrados.remove(id_usuario)
            del self.usuarios[id_usuario]
            print(f"Usuario con ID {id_usuario} dado de baja correctamente.")
        else:
            print(f"El usuario con ID {id_usuario} no está registrado.")

    # Método para prestar un libro a un usuario.
    def prestar_libro(self, isbn, id_usuario):
        if isbn not in self.libros_disponibles:
            print(f"El libro con ISBN {isbn} no está disponible.")
            return
        if id_usuario not in self.usuarios_registrados:
            print(f"El usuario con ID {id_usuario} no está registrado.")
            return

        libro = self.libros_disponibles[isbn]
        usuario = self.usuarios[id_usuario]

        usuario.libros_prestados.append(libro)
        del self.libros_disponibles[isbn]
        print(f"Libro '{libro.titulo_autor[0]}' prestado a '{usuario.nombre}'.")

    # Método para devolver un libro a la biblioteca.
    def devolver_libro(self, isbn, id_usuario):
        if id_usuario not in self.usuarios_registrados:
            print(f"El usuario con ID {id_usuario} no está registrado.")
            return

        usuario = self.usuarios[id_usuario]
        libro_a_devolver = None

        for libro in usuario.libros_prestados:
            if libro.isbn == isbn:
                libro_a_devolver = libro
                break

        if libro_a_devolver:
            usuario.libros_prestados.remove(libro_a_devolver)
            self.libros_disponibles[isbn] = libro_a_devolver
            print(f"Libro '{libro_a_devolver.titulo_autor[0]}' devuelto por '{usuario.nombre}'.")
        else:
            print(f"El libro con ISBN {isbn} no fue prestado a este usuario.")

    # Método para buscar libros por título, autor o categoría.
    def buscar_libros(self, criterio, valor):
        resultados = []
        for libro in self.libros_disponibles.values():
            if criterio == "titulo" and valor.lower() in libro.titulo_autor[0].lower():
                resultados.append(libro)
            elif criterio == "autor" and valor.lower() in libro.titulo_autor[1].lower():
                resultados.append(libro)
            elif criterio == "categoria" and valor.lower() in libro.categoria.lower():
                resultados.append(libro)

        if resultados:
            print(f"Resultados de la búsqueda por {criterio} '{valor}':")
            for libro in resultados:
                print(libro)
        else:
            print(f"No se encontraron libros con {criterio} '{valor}'.")

    # Método para listar los libros prestados a un usuario.
    def listar_libros_prestados(self, id_usuario):
        if id_usuario not in self.usuarios_registrados:
            print(f"El usuario con ID {id_usuario} no está registrado.")
            return

        usuario = self.usuarios[id_usuario]
        if usuario.libros_prestados:
            print(f"Libros prestados a '{usuario.nombre}':")
            for libro in usuario.libros_prestados:
                print(libro)
        else:
            print(f"'{usuario.nombre}' no tiene libros prestados.")


# Función para mostrar el menú y manejar las opciones del usuario.
def mostrar_menu():
    print("\n--- Sistema de Gestión de Biblioteca Digital ---")
    print("1. Añadir libro")
    print("2. Quitar libro")
    print("3. Registrar usuario")
    print("4. Dar de baja usuario")
    print("5. Prestar libro")
    print("6. Devolver libro")
    print("7. Buscar libros")
    print("8. Listar libros prestados")
    print("9. Salir")


# Función principal del programa.
def main():
    biblioteca = Biblioteca()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":  # Añadir libro
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            categoria = input("Ingrese la categoría del libro: ")
            isbn = input("Ingrese el ISBN del libro: ")
            libro = Libro(titulo, autor, categoria, isbn)
            biblioteca.añadir_libro(libro)

        elif opcion == "2":  # Quitar libro
            isbn = input("Ingrese el ISBN del libro a quitar: ")
            biblioteca.quitar_libro(isbn)

        elif opcion == "3":  # Registrar usuario
            nombre = input("Ingrese el nombre del usuario: ")
            id_usuario = input("Ingrese el ID del usuario: ")
            usuario = Usuario(nombre, id_usuario)
            biblioteca.registrar_usuario(usuario)

        elif opcion == "4":  # Dar de baja usuario
            id_usuario = input("Ingrese el ID del usuario a dar de baja: ")
            biblioteca.dar_de_baja_usuario(id_usuario)

        elif opcion == "5":  # Prestar libro
            isbn = input("Ingrese el ISBN del libro a prestar: ")
            id_usuario = input("Ingrese el ID del usuario: ")
            biblioteca.prestar_libro(isbn, id_usuario)

        elif opcion == "6":  # Devolver libro
            isbn = input("Ingrese el ISBN del libro a devolver: ")
            id_usuario = input("Ingrese el ID del usuario: ")
            biblioteca.devolver_libro(isbn, id_usuario)

        elif opcion == "7":  # Buscar libros
            criterio = input("Buscar por (titulo/autor/categoria): ").lower()
            valor = input(f"Ingrese el {criterio} a buscar: ")
            biblioteca.buscar_libros(criterio, valor)

        elif opcion == "8":  # Listar libros prestados
            id_usuario = input("Ingrese el ID del usuario: ")
            biblioteca.listar_libros_prestados(id_usuario)

        elif opcion == "9":  # Salir
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()