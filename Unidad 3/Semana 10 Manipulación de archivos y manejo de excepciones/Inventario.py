class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        """
        Constructor de la clase Producto.
        Inicializa un producto con un ID único, nombre, cantidad y precio.
        """
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Getters
    def get_id(self):
        """Devuelve el ID del producto."""
        return self.id

    def get_nombre(self):
        """Devuelve el nombre del producto."""
        return self.nombre

    def get_cantidad(self):
        """Devuelve la cantidad disponible del producto."""
        return self.cantidad

    def get_precio(self):
        """Devuelve el precio del producto."""
        return self.precio

    # Setters
    def set_nombre(self, nombre):
        """Actualiza el nombre del producto."""
        self.nombre = nombre

    def set_cantidad(self, cantidad):
        """Actualiza la cantidad disponible del producto."""
        self.cantidad = cantidad

    def set_precio(self, precio):
        """Actualiza el precio del producto."""
        self.precio = precio

    def __str__(self):
        """
        Representación en cadena del producto.
        Devuelve una cadena formateada con los detalles del producto.
        """
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"