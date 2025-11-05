class Validar:
    def ValidarNombre(self, nombre):
        """Solo letras y espacios"""
        return nombre.replace(" ", "").isalpha() and len(nombre.strip()) > 0

    def ValidarPrecio(self, precio):
        """Número flotante positivo"""
        try:
            precio = float(precio)
            return precio > 0
        except ValueError:
            return False

    def ValidarCantidad(self, cantidad):
        """Entero positivo"""
        try:
            cantidad = int(cantidad)
            return cantidad > 0
        except ValueError:
            return False
