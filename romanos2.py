simbolos = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
l_entero= []
letras = []
puntero= 0
l_resultado =[]

def romano_entero(letras):
  
    if len (letras) == 1:
        if letra in simbolos:
                print(simbolos[letra])
    elif len(letras) != 1:
        for letra in letras:
            if letra in simbolos:
                entero = simbolos[letra]
                l_entero.append(entero)

    while l_entero != []:
        
        if l_entero[puntero] < l_entero[puntero+1]:
                num_1=l_entero[puntero]
                num_2=l_entero[puntero+1]
                resultado =num_2 - num_1
                l_resultado.append(resultado)
                l_entero.remove(l_entero[0])
                l_entero.remove(l_entero[0])   
        elif l_entero[puntero] > l_entero[puntero+1]:
                num_1=l_entero[puntero]
                num_2=l_entero[puntero+1]
                resultado =num_1 + num_2
                l_resultado.append(resultado)
                l_entero.remove(l_entero[0])
                l_entero.remove(l_entero[0])
        elif l_entero[puntero] == l_entero[puntero+1] == l_entero[puntero+2]:
                num_1=l_entero[puntero]
                num_2=l_entero[puntero+1]
                num_3=l_entero[puntero+2]
                resultado = num_1 + num_2 + num_3
                l_resultado.append(resultado)
                l_entero.remove(l_entero[0])
                l_entero.remove(l_entero[0])
                l_entero.remove(l_entero[0])
                
    solucion = sum(l_resultado)           
    print(solucion)


 if __name__=="__main__":