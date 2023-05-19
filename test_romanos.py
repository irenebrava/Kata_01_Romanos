from romanos import entero_a_romano

def test_uno_es_palito():
    assert entero_a_romano(1) == "I"

def test_dos_es_palito_palito():
    assert entero_a_romano(2) == "II"

def test_tres_es_palito_palito():
    assert entero_a_romano(3) == "III"

def test_cuatro_es_palito_palito():
    assert entero_a_romano(4) == "IV"

def test_cinco_es_palito_palito():
    assert entero_a_romano(5) == "V"

def test_seis_es_palito_palito():
    assert entero_a_romano(6) == "VI"