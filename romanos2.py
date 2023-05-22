simbolos = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
entero_lista = []

def entero_romano(n_int):
    n_mil = n_int // 1000 * 1000
    n_cen = (n_int % 1000) // 100 * 100
    n_dec = (n_int % 100) // 10 * 10
    n_uni = n_int % 10 * 10
    entero_lista = [n_mil, n_cen, n_dec, n_uni]
    return entero_lista

def presente(lista_num):
    numero_romano = ""
    for numero in lista_num:
        if numero in simbolos.values():
            numero_romano += [letra for letra, valor in simbolos.items() if valor == numero][0]
    return numero_romano

entero = int(input("Dame un número: "))
entero_lista = entero_romano(entero)
numero_romano = presente(entero_lista)
entero_lista.append(numero_romano)
print(numero_romano)