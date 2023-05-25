from romannumbers import romano_a_entero, RomanNumberError
import pytest

def test_simbolos():
    assert romano_a_entero("I") == 1
    assert romano_a_entero("L") == 50

def test_resta_normal():
    assert romano_a_entero("IV") == 4
    assert romano_a_entero("IX") == 9
    assert romano_a_entero("XIX") == 19

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
def test_resta_repetida():
    with pytest.raises(RomanNumberError):
        romano_a_entero("IIX")
    with pytest.raises(RomanNumberError):
        romano_a_entero("MCIIX")
    with pytest.raises(RomanNumberError):
        romano_a_entero("XXCC")
    with pytest.raises(RomanNumberError):
        romano_a_entero("CCMLV")
def test_resta_repetida_2():
    with pytest.raises(RomanNumberError):
        romano_a_entero("IXIX")
    with pytest.raises(RomanNumberError):
        romano_a_entero("IXX")