import os
def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)
    opciones = {
        '1': 'semana 02 ejemplos de tecnica de programacion/ejemplos tecnicas de programacion.py',
        '2': 'semana 02 ejemplos de tecnica de programacion/sistemas de reservas.py',
        '3': 'semana 03  Ejemplo Programacion tradicional frente a POO/programacion orientada a objetos.py',
        '4': 'semana 03  Ejemplo Programacion tradicional frente a POO/programacion tradicional.py',
        '5': 'semana 044 Semana 04 EjemplosMundoReal_POO/tienda.py',
        '6': 'semana 05 Semana 05 Tipos de datos, Identificadores/ipos de datos, Identificadores.py',
        '7': 'semana 06 Semana 06. Clases, objetos, herencia, encapsulamiento y polimorfismo/Clases, objetos, herencia, encapsulamiento y polimorfismo.py',
        '8': 'semana 07 semana 07 Constructores y Destructores/Constructores y Destructores.py'
    }
    while True:
        print("\nMenu Principal - Dashboard")
        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")
        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            # Asegura que el path sea absoluto
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")
# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()