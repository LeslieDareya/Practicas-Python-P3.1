class Validar:
    def ValidarSueldo(self, sueldo):
        """Valida que el sueldo sea un número positivo."""
        try:
            sueldo = float(sueldo)
            return sueldo > 0
        except ValueError:
            return False

    def ValidarDias(self, dias):
        """Valida que los días estén entre 1 y 31 y sean enteros."""
        try:
            dias = int(dias)
            return 1 <= dias <= 31
        except ValueError:
            return False
