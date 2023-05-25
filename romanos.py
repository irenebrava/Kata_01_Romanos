unidades = {
    1: "I",
    5: "V",
    10: "X"
}

decenas = {
    1: "X",
    5: "L",
    10: "C"
}

centenas = {
    1: "C",
    5: "D",
    10: "M"
}

millares = {
    1: "M"
}


numeros_romanos = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

class RomanNumberError(Exception):
    pass

def listar_numero(num):
    n_mil = num // 1000 * 1000
    n_cen = (num % 1000) // 100 * 100
    n_dec = (num % 100) // 10 * 10
    n_uni = (num % 10) 

    return n_mil, n_cen, n_dec, n_uni

def sacar_clave(num):
    if num >= 1000:
        clave = millares
        num = num // 1000
    elif num >= 100:
        clave = centenas
        num //= 100
    elif num >= 10:
        clave = decenas
        num = num // 10
    else:
        clave = unidades
    return clave, num

def logica_aplastante(digito, clau):
    res = ""
    if digito < 4:
        res += digito * clau[1]
    elif digito == 4:
        res += clau[1] + clau[5]
    elif digito < 9:
        num_palitos = digito - 5
        res += clau[5] + num_palitos * clau[1]
    else:
        res += clau[1] + clau[10]

    return res 

def entero_a_romano(n_int):
    if n_int >= 10000 and n_int < 100000:
       l_int = [int(digito) for digito in str(n_int)]
       n_p = int(l_int[0]+l_int[1])
       parentesis_digito = logica_aplastante(n_p,decenas)
       numero_mil= ("(({}))".format(parentesis_digito))
       n_rest = n_int-(n_p*10000)
       numero_final_2 = entero_a_romano(n_rest)
       return numero_mil + numero_final_2
    
    if n_int > 3999 and n_int < 10000:
       l_int = [int(digito) for digito in str(n_int)]
       n_p = int(l_int[0])
       parentesis_digito = logica_aplastante(n_p,unidades)
       numero_mil= ("({})".format(parentesis_digito))
       n_rest = n_int-(n_p*1000)
       numero_final_2 = entero_a_romano(n_rest)
       return numero_mil + numero_final_2
       
    
    digitos = listar_numero(n_int)

    resultado = ""
    for digito in digitos:
        if digito == 0:
            continue        

        clave, digito = sacar_clave(digito)

        resultado += logica_aplastante(digito, clave)
        
    return resultado


def comprueba_excepciones(romano):
    for simbolo in numeros_romanos:
        if simbolo * 4 in romano:
            raise RomanNumberError("No se admites mas de tres simbolos iguales")
        elif simbolo in ("V","L","D") and simbolo *2 in romano:
            raise RomanNumberError("No se pueden repetir estos simbolos")
    
def romano_a_entero(letras):

    valor_total = 0
    ultimo_valor = 0 
    final_valor= 0

    comprueba_excepciones(letras)

    for numeral in reversed(letras):
        valor_actual = numeros_romanos[numeral]

        if valor_actual <= 5 and ultimo_valor >= 50:
            raise RomanNumberError("Resta no permitida") 
        elif valor_actual <= 50 and ultimo_valor >= 500:
            raise RomanNumberError("Resta no permitida")
        
        elif valor_actual< final_valor:
            raise RomanNumberError("No esta ordenado")
        elif final_valor == valor_actual and ultimo_valor> valor_actual:
            raise RomanNumberError("resta no")
        

        if valor_actual >= ultimo_valor:
            valor_total += valor_actual
        elif numeral not in "VLD":
            valor_total -= valor_actual
        final_valor = ultimo_valor 
        ultimo_valor = valor_actual
        

    return valor_total

if __name__ == "__main__":
    print(entero_a_romano(45327))