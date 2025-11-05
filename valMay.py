class Validar:
    def __init__(self):
        pass

    def solo_letras(self, texto):
        """
        Verifica que el texto contenga únicamente letras (mayúsculas o minúsculas).
        Retorna True si es válido, False en caso contrario.
        """
        return texto.isalpha()
