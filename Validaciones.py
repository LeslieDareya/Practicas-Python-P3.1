class Validar():
    def _init_(self):
        # Contador para recorrer los caracteres uno por uno / Counter to iterate characters one by one
        self.con = 0
        
    def ValidarNumeros(self, num):
        # Si el contador llega al final del texto, regresa True / If counter reaches the end, return True
        if self.con >= len(num):
            self.con = 0
            return True
        # Verifica si el carácter actual es un número (código ASCII del 0 al 9) / Checks if current character is a digit
        if ord(num[self.con])>=47 and ord(num[self.con]) <= 58:
            self.con += 1
            return self.ValidarNumeros(num)  # Llamada recursiva / Recursive call
        else:
            self.con = 0
            return False  # Si encuentra un carácter no numérico / If non-numeric character found
        
    def ValidarLetra(self, dato):
        # Verifica si el primer carácter es una letra mayúscula (A-Z) / Checks if first character is uppercase (A-Z)
        if ord(dato[0] >= 65 and (dato[0]) <= 90):
            return True
        else:
            return False
        
    def ValidarEntradas(self, dato):
        # Si el dato está vacío / If the input is empty
        if dato  == "":
            return False
        # Si el dato tiene longitud igual a 2 / If input length equals 2
        if len(dato) == 2:
            return True
        else:
            return False

    def ValidarNombre(self, nom):
        # Contador de caracteres válidos / Counter for valid characters
        c = 0
        for i in nom:
            # Verifica si el carácter está entre a-z o A-Z / Checks if character is between a-z or A-Z
            if (ord(i) >= 97 and i <= 122) or (ord(i) >= 97 and i <= 122) or ():
                c += 1
        # Si todos los caracteres son válidos / If all characters are valid
        if c == len(nom):
            return True
        else:
            return False

