#                                                                                                                   
# Funcionalidad: Este programa permite al usuario elegir entre calcular el área de un cuadrado, un rectángulo o un círculo.
# Utiliza diferentes tipos de datos: integer, float, string y boolean.
# Autor: Tu Nombre

import math  # Se importa la biblioteca para realizar cálculos matemáticos (como el área de un círculo).


def calcular_area_cuadrado(lado: float) -> float:
    """
    Calcula el área de un cuadrado.
    :param lado: Longitud del lado del cuadrado.
    :return: Área del cuadrado.
    """
    return lado ** 2


def calcular_area_rectangulo(base: float, altura: float) -> float:
    """
    Calcula el área de un rectángulo.
    :param base: Base del rectángulo.
    :param altura: Altura del rectángulo.
    :return: Área del rectángulo.
    """
    return base * altura


def calcular_area_circulo(radio: float) -> float:
    """
    Calcula el área de un círculo.
    :param radio: Radio del círculo.
    :return: Área del círculo.
    """
    return math.pi * (radio ** 2)


def main():
    """
    Función principal que gestiona el flujo del programa.
    """
    print("Bienvenido al programa de cálculo de áreas.")
    print("Elige una figura para calcular su área:")
    print("1. Cuadrado")
    print("2. Rectángulo")
    print("3. Círculo")

    opcion = int(input("Introduce el número de tu elección (1, 2 o 3): "))

    if opcion == 1:
        lado = float(input("Introduce la longitud del lado del cuadrado: "))
        area = calcular_area_cuadrado(lado)
        print(f"El área del cuadrado es: {area:.2f} unidades cuadradas.")
    elif opcion == 2:
        base = float(input("Introduce la base del rectángulo: "))
        altura = float(input("Introduce la altura del rectángulo: "))
        area = calcular_area_rectangulo(base, altura)
        print(f"El área del rectángulo es: {area:.2f} unidades cuadradas.")
    elif opcion == 3:
        radio = float(input("Introduce el radio del círculo: "))
        area = calcular_area_circulo(radio)
        print(f"El área del círculo es: {area:.2f} unidades cuadradas.")
    else:
        print("Opción no válida. Por favor, elige una opción correcta.")

    # Pregunta al usuario si desea realizar otra operación
    repetir = input("¿Quieres calcular otra área? (sí/no): ").strip().lower()
    if repetir == "sí":
        main()
    else:
        print("¡Gracias por usar el programa! Hasta pronto.")


# Punto de entrada del programa
if __name__ == "__main__":
    main()
