from pytest import approx
from calc import calcular_igv, aplicar_descuento


def test_calcular_igv():
    assert calcular_igv(100) == approx(20)


def test_aplicar_descuento():
    assert aplicar_descuento(100, 10) == approx(90)

def test_aplicar_recargo():
    from calc import aplicar_recargo
    assert aplicar_recargo(100, 10) == approx(110)

def test_calcular_envio():
    from calc import calcular_envio
    assert calcular_envio(250, "Lima") == 0
    assert calcular_envio(100, "Lima") == 10
    assert calcular_envio(100, "Callao") == 12
    assert calcular_envio(100, "Arequipa") == 20