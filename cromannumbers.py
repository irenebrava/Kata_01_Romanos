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

"""
metodos mágicos para logica
"""
def __eq__(self, other):
     other = self.__to_roman(other)
     return self.numero == other.numero

def __req__(self, other):
     return self.__eq__(other)

def __lt__(self, other):
     other = self.__to_roman(other)
     return self.numero < other.numero

def __le__(self, other):
     other = self.__to_roman(other)
     return self.numero <= other.numero

def __gt__(self, other):
     other = self.__to_roman(other)
     return self.numero > other.numero

def __ge__(self, other):
     other = self.__to_roman(other)
     return self.numero >= other.numero

def __ne__(self, other):
     other = self.__to_roman(other)
     return self.numero != other.numero

"""
metodos mágicos para logica
"""
def __eq__(self, other):
     other = self.__to_roman(other)
     return self.numero == other.numero

def __req__(self, other):
     return self.__eq__(other)

def __lt__(self, other):
     other = self.__to_roman(other)
     return self.numero < other.numero

def __le__(self, other):
     other = self.__to_roman(other)
     return self.numero <= other.numero

def __gt__(self, other):
     other = self.__to_roman(other)
     return self.numero > other.numero

def __ge__(self, other):
     other = self.__to_roman(other)
     return self.numero >= other.numero

def __ne__(self, other):
     other = self.__to_roman(other)
     return self.numero != other.numero


"""
metodos mágicos para aritmética
"""

def __to_roman(self, otro):
     if not isinstance(otro, RomanNumber):
          otro = RomanNumber(otro)
     return otro

def __mul__(self, otro):
     if not isinstance(otro, RomanNumber):
          otro = RomanNumber(otro)

     resultado = self.numero * otro.numero
     
     return RomanNumber(resultado)

def __rmul__(self, otro):
     return self.__mul__(otro)


def __add__(self, otro):
     if not isinstance(otro, RomanNumber):
          otro = RomanNumber(otro)
     resultado = self.numero + otro.numero
     return RomanNumber(resultado)

def __radd__(self, otro):
     return self.__add__(otro)

def __floordiv__(self, otro):
     if not isinstance(otro, RomanNumber):
          otro = RomanNumber(otro)
     resultado = self.numero // otro.numero
     return RomanNumber(resultado)

def __rfloordiv__(self, otro):
     otro = RomanNumber(otro)
     return otro.__floordiv__(self)

def __sub__(self, otro):
     if not isinstance(otro, RomanNumber):
          otro = RomanNumber(otro)

     return RomanNumber(self.numero - otro.numero)

def __rsub__(self, otro):
     otro = self.__to_roman(otro)

     return otro.__sub__(self)

def __pow__(self, otro):
     otro = self.__to_roman(otro)
     return RomanNumber(self.numero ** otro.numero)

def __rpow__(self, otro):
     otro = self.__to_roman(otro)
     return otro.__pow__(self)


"""""
metodos magicos representacion
"""""
def __repr__(self):
     return f"{self.numero}-{self.simbolo}"

def __str__(self):
     return self.__repr__()


if __name__ == "__main__":
 romano2 = RomanNumber(5)
 suma ="X" + romano2
 print(suma)
 suma = romano2 + 10
 print(suma)
 resta = "X"- romano2
 print(resta)
 resta2 = 10 - romano2
 print(resta2)
