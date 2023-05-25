def test_instaciar_num_romano():
    romano = RomanNumber(23)
    assert romano.valor == 23
    assert romano.simbolo =="XXIII"

class Alumna:
    def __init__(self,n, a):
        self.nombre = n
        self.apellido = a




def test_irene_existe():
    irene =Alumna("Irene", "Bravo")
    assert irene.nombre == "Irene"
    assert irene.apellido =="Bravo" 
/*////////////////////////////////////////////////*/