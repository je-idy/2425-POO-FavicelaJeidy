def ingresar_temperaturas():
    """
    Solicita al usuario ingresar las temperaturas diarias durante una semana.
    Retorna una lista de temperaturas (floats).
    """
    print("Ingrese las temperaturas diarias de la semana:")
    temperaturas = []
    for dia in ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]:
        while True:
            try:
                temp = float(input(f"{dia}: "))
                temperaturas.append(temp)
                break
            except ValueError:
                print("Por favor, ingrese un número válido.")
    return temperaturas

def calcular_promedio(temperaturas):
    """
    Calcula el promedio de una lista de temperaturas.
    """
    return sum(temperaturas) / len(temperaturas)

def mostrar_resultados(temperaturas, promedio):
    """
    Muestra las temperaturas ingresadas y el promedio semanal.
    """
    print("\n--- Resultados ---")
    print("Temperaturas ingresadas:", temperaturas)
    print(f"Promedio semanal: {promedio:.2f}°C")

def main():
    """
    Función principal que organiza la ejecución del programa.
    """
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    mostrar_resultados(temperaturas, promedio)

if __name__ == "__main__":
    main()
