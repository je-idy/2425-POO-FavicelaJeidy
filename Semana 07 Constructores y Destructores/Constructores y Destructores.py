# Clase "Libro" que representa un libro con atributos como título, autor y año de publicación
class Libro:
    # El constructor __init__ se utiliza para inicializar el objeto con los valores proporcionados
    def __init__(self, titulo, autor, anio_publicacion):
        self.titulo = titulo  # Inicializa el atributo 'titulo' con el valor proporcionado
        self.autor = autor  # Inicializa el atributo 'autor' con el valor proporcionado
        self.anio_publicacion = anio_publicacion  # Inicializa el atributo 'anio_publicacion' con el valor proporcionado
        print(f"Constructor llamado: El libro '{self.titulo}' ha sido creado.")

    # El destructor __del__ se ejecuta automáticamente cuando el objeto es destruido (eliminado)
    # En este caso, el destructor imprime un mensaje indicando que el libro está siendo destruido.
    def __del__(self):
        print(f"Destructor llamado: El libro '{self.titulo}' ha sido destruido.")

    # Método para mostrar la información del libro
    def mostrar_informacion(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año de publicación: {self.anio_publicacion}")


# Función principal para probar la clase Libro
def main():
    # Creación de un objeto 'mi_libro' de la clase Libro, el constructor se llama automáticamente
    mi_libro = Libro("Cien años de soledad", "Gabriel García Márquez", 1967)

    # Mostramos la información del libro usando el método mostrar_informacion
    mi_libro.mostrar_informacion()

    # Aquí no es necesario llamar explícitamente al destructor, ya que Python lo maneja automáticamente
    # cuando el objeto sale de ámbito al final de la función main.


# Ejecutamos el programa
if __name__ == "__main__":
    main()
