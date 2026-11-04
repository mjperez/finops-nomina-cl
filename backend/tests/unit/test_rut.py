from app.domain.chilean_rules import validar_rut


def test_rut_validos():
    assert(validar_rut(11111111, "1")) is True
    assert(validar_rut(33333333,"3")) is True
    assert(validar_rut(76000000, "0")) is True
    assert(validar_rut(11111112, "K")) is True
    
def test_rut_invalidos():
    assert(validar_rut(11111111, "K")) is False
    assert(validar_rut(33333333,"1")) is False
    assert(validar_rut(76000000, "2")) is False
    assert(validar_rut(11111112, "0")) is False
    
def test_rut_casos_borde():
    assert(validar_rut(0,"0")) is False
    assert(validar_rut(-1111111,"1")) is False
    assert(validar_rut(1111111,"")) is False
