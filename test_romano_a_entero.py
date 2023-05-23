from romannumbers import romano_a_entero, RomanNumberError
import pytest

def test_simbolos():
    assert romano_a_entero("I") == 1
    assert romano_a_entero("L") == 50

def test_resta_normal():
    assert romano_a_entero("IV") == 4
    assert romano_a_entero("IX") == 9

def test_sumando():
    assert romano_a_entero("CXXIII")==123

def test_composicion():
    assert romano_a_entero("MMCMXLIX")==2949

def test_no_mas_3():
    with pytest.raises(RomanNumberError):
        romano_a_entero("CCCC")

def test_no_repetir_VLD():
    with pytest.raises(RomanNumberError):
        romano_a_entero("VV")
    with pytest.raises(RomanNumberError):
        romano_a_entero("LL")
    with pytest.raises(RomanNumberError):
        romano_a_entero("DD")

def test_restas_no():
    with pytest.raises(RomanNumberError):
        romano_a_entero("IC")
    with pytest.raises(RomanNumberError):
        romano_a_entero("XM")
    with pytest.raises(RomanNumberError):
        romano_a_entero("IL")