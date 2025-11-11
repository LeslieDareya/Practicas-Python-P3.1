class Validar:
    def __init__(self):
        # Constructor vacío / Empty constructor
        pass

    def ValidarLetras(self, texto):
        # Verifica que el texto contenga solo letras o espacios
        # Checks that the text contains only letters or spaces
        if texto == "":
            return False
        for c in texto:
            if not ((ord(c) >= 65 and ord(c) <= 90) or (ord(c) >= 97 and ord(c) <= 122) or c == " "):
                return False
        return True

    def ValidarNumero(self, texto):
        # Verifica que el texto contenga solo números
        # Checks that the text contains only numbers
        if texto == "":
            return False
        for c in texto:
            if not (ord(c) >= 48 and ord(c) <= 57):
                return False
        return True

    def ValidarFecha(self, dia, mes, anio):
        # Verifica que los campos de fecha sean válidos
        # Checks that the date fields are valid
        if not (self.ValidarNumero(dia) and self.ValidarNumero(mes) and self.ValidarNumero(anio)):
            return False
        d, m, a = int(dia), int(mes), int(anio)
        # Valida los rangos de día, mes y año / Validates the ranges of day, month, and year
        if d < 1 or d > 31 or m < 1 or m > 12 or a < 1900 or a > 2025:
            return False
        return True
