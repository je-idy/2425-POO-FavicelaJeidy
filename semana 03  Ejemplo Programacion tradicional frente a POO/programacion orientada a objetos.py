class ClimaSemanal:
    """
    Clase que representa la información diaria del clima y calcula el promedio semanal.
    """
    def __init__(self):
        # Lista para almacenar las temperaturas diarias
        self.__temperaturas = []

    def ingresar_temperaturas(self):
        """
        Método para ingresar las temperaturas diarias de la semana.
        """
        print("Ingrese las temperaturas diarias de la semana:")
        for dia in ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]:
            while True:
                try:
                    temp = float(input(f"{dia}: "))
                    self.__temperaturas.append(temp)
                    break
                except ValueError:
                    print("Por favor, ingrese un número válido.")

    def calcular_promedio(self):
        """
        Método para calcular el promedio semanal de temperaturas.
        """
        if not self.__temperaturas:
            print("No se han ingresado temperaturas.")
            return None
        return sum(self.__temperaturas) / len(self.__temperaturas)

    def mostrar_resultados(self):
        """
        Método para mostrar las temperaturas ingresadas y el promedio semanal.
        """
        print("\n--- Resultados ---")
        print("Temperaturas ingresadas:", self.__temperaturas)
        promedio = self.calcular_promedio()
        if promedio is not None:
            print(f"Promedio semanal: {promedio:.2f}°C")

# Clase hija (opcional) para extender funcionalidad
class ClimaExtendido(ClimaSemanal):
    """
    Clase extendida que permite agregar más funcionalidades (opcional).
    """
    def mostrar_dias_calidos(self, umbral):
        """
        Muestra los días con temperaturas superiores a un umbral.
        """
        dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        dias_calidos = [dia for dia, temp in zip(dias, self._ClimaSemanal__temperaturas) if temp > umbral]
        print(f"Días con temperatura superior a {umbral}°C: {', '.join(dias_calidos) if dias_calidos else 'Ninguno'}")

def main():
    """
    Función principal para ejecutar el programa.
    """
    clima = ClimaSemanal()
    clima.ingresar_temperaturas()
    clima.mostrar_resultados()

    # Extender funcionalidad (opcional)
    clima_extendido = ClimaExtendido()
    clima_extendido.ingresar_temperaturas()
    clima_extendido.mostrar_resultados()
    clima_extendido.mostrar_dias_calidos(umbral=25)

if __name__ == "__main__":
    main()