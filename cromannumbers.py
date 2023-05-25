from romannumbers import *
class RomanNumber:
    def __init__(self, entrada):
        if type(entrada) == int:
            self._numero = entrada
            self._simbolo = entero_a_romano(entrada)
        elif isinstance (entrada, str):
            self._numero = romano_a_entero(entrada)
            self._simbolo = entrada
        else:
            raise RomanNumberError("Debes poner un entero o romano valido")
        

    @property
    def numero(self):
            return self._numero
    @property
    def simbolo(self):
            return self._simbolo
    
    @numero.setter
    def numero(self,entrada):
         self._numero = entrada
         self._simbolo = entero_a_romano(entrada)

    @simbolo.setter
    def simbolo(self,entrada):
         self._numero = romano_a_entero(entrada)
         self._simbolo = entrada

        
