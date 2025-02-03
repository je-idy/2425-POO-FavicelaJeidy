# Clase base que representa a un Animal
class Animal:
    def __init__(self, nombre, edad):
        # Atributos encapsulados con un guion bajo (_)
        self._nombre = nombre
        self._edad = edad

    # Método para describir al animal
    def describir(self):
        return f"Soy un animal llamado {self._nombre}, y tengo {self._edad} años."

    # Métodos getter y setter para acceder y modificar atributos encapsulados
    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_edad(self):
        return self._edad

    def set_edad(self, edad):
        self._edad = edad


# Clase derivada que representa a un Perro
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        # Heredamos atributos de la clase base
        super().__init__(nombre, edad)
        self.raza = raza  # Nuevo atributo específico para perros

    # Sobrescribimos el método describir para aplicar polimorfismo
    def describir(self):
        return f"Soy un perro llamado {self._nombre}, de raza {self.raza}, y tengo {self._edad} años."

    # Método exclusivo de la clase Perro
    def ladrar(self):
        return f"{self._nombre} está ladrando: ¡Guau guau!"


# Código principal para demostrar la funcionalidad
def main():
    # Creamos un objeto de la clase base
    animal = Animal("Tomby", 5)
    print(animal.describir())

    # Creamos un objeto de la clase derivada
    perro = Perro("Bobby", 3, "Golden Retriever")
    print(perro.describir())  # Polimorfismo: Llama al método sobrescrito
    print(perro.ladrar())  # Método exclusivo de la clase derivada

    # Usamos métodos getter y setter (encapsulación)
    perro.set_nombre("Rocky")
    print(f"Nuevo nombre del perro: {perro.get_nombre()}")


# Llamamos a la función principal
if __name__ == "__main__":
    main()
