
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
    assert romano._simbolo =="I"

    romano.numero = 2
    assert romano.numero == 2
    assert romano._simbolo =="II"

    romano.simbolo ="III"
    assert romano.numero == 3
    assert romano.simbolo =="III"

def test_multiplicaciones():
    romano1 = RomanNumber("X")
    romano2= RomanNumber(5)
    assert romano1 * romano2 == RomanNumber("L")
    assert romano1 * 5 == RomanNumber(50)
    assert romano1 * "V" == RomanNumber(50)
    assert "X" * romano2 == RomanNumber("L")
    assert 10 * romano2 == RomanNumber("L")

def test_sumas():
    romano1 = RomanNumber("X")
    romano2= RomanNumber(5)
    assert "X" + romano2 == RomanNumber("XV")
    assert 10 + romano2 == RomanNumber(15)
    assert romano1 + romano2 == RomanNumber("XV")
    assert romano1 + 5 == RomanNumber(15)
    assert romano1 + "V" == RomanNumber(15)

def test_restas():
    romano1 = RomanNumber("X")
    romano2= RomanNumber(5)
    assert romano1 - romano2 == RomanNumber("V")
    assert romano1 - 5 == RomanNumber(5)
    assert romano1 - "V" == RomanNumber(5)
    
    assert "X" - romano2 == RomanNumber("V")
    assert 10 - romano2 == RomanNumber(5)