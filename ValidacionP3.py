class Validar:
    def __init__(self):
        self.con = 0

    def ValidarNumeros(self, num):
        # Verifica que todos los caracteres sean números
        if num == "":
            return False
        for c in num:
            if not (ord(c) >= 48 and ord(c) <= 57):
                return False
        return True

    def ValidarLetras(self, texto):
        # Verifica que todos los caracteres sean letras o espacios
        if texto == "":
            return False
        for c in texto:
            if not ((ord(c) >= 65 and ord(c) <= 90) or 
                    (ord(c) >= 97 and ord(c) <= 122) or 
                    c == " "):
                return False
        return True

    def ValidarDomicilio(self, texto):
        # Verifica que el domicilio contenga letras, números o espacios
        if texto == "":
            return False
        for c in texto:
            if not ((ord(c) >= 65 and ord(c) <= 90) or 
                    (ord(c) >= 97 and ord(c) <= 122) or 
                    (ord(c) >= 48 and ord(c) <= 57) or 
                    c == " "):
                return False
        return True

