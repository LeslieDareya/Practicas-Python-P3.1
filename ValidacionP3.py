class Validar:
    def __init__(self):
        # Contador para validaciones (por si se necesita en el futuro)
        # Counter for validations (reserved for future use)
        self.con = 0

    def ValidarNumeros(self, num):
        #  Verifica que todos los caracteres sean números
        #  Checks that all characters are numbers
        if num == "":
            return False  # Si está vacío / If empty, return False
        for c in num:
            # Comprueba si el código ASCII está entre 48 ('0') y 57 ('9')
            # Checks if ASCII code is between 48 ('0') and 57 ('9')
            if not (ord(c) >= 48 and ord(c) <= 57):
                return False
        return True  # Si todos son números / If all are digits

    def ValidarLetras(self, texto):
        #  Verifica que todos los caracteres sean letras o espacios
        #  Checks that all characters are letters or spaces
        if texto == "":
            return False  # Si está vacío / If empty, return False
        for c in texto:
            # Comprueba si es una letra mayúscula, minúscula o espacio
            # Checks if uppercase, lowercase, or space
            if not ((ord(c) >= 65 and ord(c) <= 90) or 
                    (ord(c) >= 97 and ord(c) <= 122) or 
                    c == " "):
                return False
        return True  # Si todos los caracteres son válidos / If all characters valid

    def ValidarDomicilio(self, texto):
        #  Verifica que el domicilio contenga letras, números o espacios
        #  Checks that address contains letters, numbers, or spaces
        if texto == "":
            return False  # No se permite vacío / Empty not allowed
        for c in texto:
            # Comprueba si es letra, número o espacio
            # Checks if character is letter, number, or space
            if not ((ord(c) >= 65 and ord(c) <= 90) or 
                    (ord(c) >= 97 and ord(c) <= 122) or 
                    (ord(c) >= 48 and ord(c) <= 57) or 
                    c == " "):
                return False
        return True  # Si el domicilio es válido / If address is valid


