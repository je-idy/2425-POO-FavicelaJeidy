# Sistema de Reservas utilizando POO

# Clase Cliente: Representa a los clientes que harán reservas
class Cliente:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

    def __str__(self):
        return f"Cliente: {self.nombre}, Teléfono: {self.telefono}"

# Clase Mesa: Representa las mesas disponibles para reservar
class Mesa:
    def __init__(self, id_mesa, capacidad):
        self.id_mesa = id_mesa
        self.capacidad = capacidad
        self.esta_reservada = False

    def __str__(self):
        estado = "Reservada" if self.esta_reservada else "Disponible"
        return f"Mesa {self.id_mesa} (Capacidad: {self.capacidad}) - {estado}"

# Clase Reserva: Gestiona los detalles de una reserva
class Reserva:
    def __init__(self, cliente, mesa, fecha_hora):
        self.cliente = cliente
        self.mesa = mesa
        self.fecha_hora = fecha_hora

    def __str__(self):
        return f"Reserva de {self.cliente.nombre} para la Mesa {self.mesa.id_mesa} el {self.fecha_hora}"

# Clase SistemaReservas: Coordina el sistema de reservas
class SistemaReservas:
    def __init__(self):
        self.mesas = []
        self.reservas = []

    def agregar_mesa(self, mesa):
        self.mesas.append(mesa)

    def listar_mesas_disponibles(self):
        disponibles = [mesa for mesa in self.mesas if not mesa.esta_reservada]
        return disponibles

    def realizar_reserva(self, cliente, id_mesa, fecha_hora):
        # Buscar la mesa por ID
        for mesa in self.mesas:
            if mesa.id_mesa == id_mesa:
                if not mesa.esta_reservada:
                    mesa.esta_reservada = True
                    reserva = Reserva(cliente, mesa, fecha_hora)
                    self.reservas.append(reserva)
                    return reserva
                else:
                    raise Exception("La mesa ya está reservada.")
        raise Exception("Mesa no encontrada.")

    def listar_reservas(self):
        return self.reservas

# Ejemplo de uso del sistema de reservas
if __name__ == "__main__":
    # Crear el sistema de reservas
    sistema = SistemaReservas()

    # Agregar mesas al sistema
    sistema.agregar_mesa(Mesa(1, 4))
    sistema.agregar_mesa(Mesa(2, 2))
    sistema.agregar_mesa(Mesa(3, 6))

    # Crear clientes
    cliente1 = Cliente("Jeidy Faviclea", "0987654321")
    cliente2 = Cliente("Carlos Pérez", "0976543210")

    # Listar mesas disponibles
    print("Mesas disponibles:")
    for mesa in sistema.listar_mesas_disponibles():
        print(mesa)

    # Realizar una reserva
    print("\nRealizando una reserva:")
    reserva1 = sistema.realizar_reserva(cliente1, 1, "2025-01-12 19:00")
    print(reserva1)

    # Listar mesas disponibles tras la reserva
    print("\nMesas disponibles tras la reserva:")
    for mesa in sistema.listar_mesas_disponibles():
        print(mesa)

    # Realizar otra reserva
    reserva2 = sistema.realizar_reserva(cliente2, 2, "2025-01-12 20:00")
    print(reserva2)

    # Listar todas las reservas
    print("\nReservas realizadas:")
    for reserva in sistema.listar_reservas():
        print(reserva)