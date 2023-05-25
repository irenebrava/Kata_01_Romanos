
from cromannumbers import RomanNumber



def test_instaciar_num_romano():
    romano = RomanNumber(23)
    assert romano.numero == 23
    assert romano.simbolo =="XXIII"

def test_instaciar_num_romano():
    romano = RomanNumber(13)
    assert romano.numero == 13
    assert romano.simbolo =="XIII"

def test_instaciar_num_romano():
    romano = RomanNumber("XI")
    assert romano.numero == 11
    assert romano.simbolo =="XI"

def test_instaciar_num_romano():
    romano = RomanNumber(1)
    assert romano.numero == 1
    assert romano.simbolo =="I"

    romano.numero = 2
    assert romano.numero == 2
    assert romano.simbolo =="II"