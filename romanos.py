unidades= {1:"I", 5:"V", 10:"X"}
decenas={1:"X", 5:"L", 10:"C"}
centenas={1:"C", 5:"D", 10:"M"}
millares ={1:"M"}

def listar_numero(num):
   n_mil = num // 1000 * 1000
   n_cen = (num % 1000) // 100 * 100
   n_dec = (num % 100) // 10 * 10
   n_uni = (num % 10)
   return n_mil, n_cen, n_dec, n_uni

def sacar_clave(n):
   if n >= 1000:
      clave = millares
      n = n//1000
   
   elif n>= 100:
      clave = centenas
      n = n//100 

   elif n>=10:
      clave = decenas
      n = n//10  
   else: 
      clave = unidades
   return clave, n

def logica(digito,clave):
   resultado = ""
   if digito < 4:
         resultado += digito * clave[1]
   elif digito == 4:
      resultado += clave[1] + clave[5]
   elif digito<9:
      num_palitos = digito -5
      resultado += clave[5] + num_palitos * clave[1]
   else:
      resultado += clave[1] + clave[10] 
   return resultado


def entero_romano(n_int):
   if n_int > 3999:
       raise ValueError("RomanNumber must be less of 4000")

   digitos=listar_numero(n_int)
   
   resultado = ""
   for digito in digitos:
      if digito == 0:
         continue
      
      clave, digito = sacar_clave(digito)
      resultado += logica(digito,clave)
       
   return resultado

if __name__=="__main__":
   print(entero_romano)