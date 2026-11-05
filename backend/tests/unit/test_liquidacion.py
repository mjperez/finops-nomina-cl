from decimal import Decimal

import pytest

from app.domain.chilean_rules import (
    calcular_imponible_topado,
    calcular_liquidacion,
    uf_a_clp,
)


def test_uf_a_clp():
    assert uf_a_clp(monto_uf=Decimal("89.9"), valor_uf=Decimal("38000.55")) == 3_416_249
    assert uf_a_clp(monto_uf=Decimal(1), valor_uf=Decimal("100.5")) == 101


def test_calcular_imponible_topado():
    assert (
        calcular_imponible_topado(
            sueldo_imponible_clp=1_000_000,
            valor_uf=Decimal(38000),
            tope_uf=Decimal("89.9"),
        )
        == 1_000_000
    )

    assert (
        calcular_imponible_topado(
            sueldo_imponible_clp=5_000_000, valor_uf=Decimal(38000)
        )
        == 3_416_200
    )


def test_calcular_liquidacion():
    res = calcular_liquidacion(
        sueldo_base_clp=5_000_000, valor_uf=Decimal(38000), tasa_afp=Decimal("0.1127")
    )

    assert res["descuento_afp_clp"] == 385006
    assert res["sueldo_liquido_clp"] == 4375860


def test_casos_borde_negativos():
    monto_uf=Decimal("-89.9")
    valor_uf=Decimal(38000)
    with pytest.raises(ValueError):
        uf_a_clp(monto_uf, valor_uf)

    monto_uf=Decimal("89.9")
    valor_uf=Decimal(0)               
    with pytest.raises(ValueError):
        uf_a_clp(monto_uf, valor_uf)
    
    sueldo_imponible_clp=-5_000_000
    valor_uf=Decimal(38000)
    with pytest.raises(ValueError):
        calcular_imponible_topado(
            sueldo_imponible_clp, valor_uf
        )
