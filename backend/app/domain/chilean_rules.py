from decimal import ROUND_HALF_UP, Decimal
from typing import TypedDict


def validar_rut(rut_num: int, rut_dv: str) -> bool:
    if rut_num <= 0 or rut_dv == "":
        return False

    factores = [2, 3, 4, 5, 6, 7]
    total = 0

    for i in range(9):  # range(9) sirve para RUTs entre 1 y 999 millones
        if rut_num == 0:
            break
        total += (rut_num % 10) * factores[i % 6]
        rut_num //= 10

    res = 11 - (total % 11)

    if res == 11:
        res = "0"
    elif res == 10:
        res = "K"
    return str(res) == rut_dv.upper()


def uf_a_clp(monto_uf: Decimal, valor_uf: Decimal) -> int:
    if monto_uf < 0 or valor_uf <= 0:
        raise ValueError(
            "El valor de la uf o el monto en uf no pueden ser menores a 0."
        )
    uf_total = monto_uf * valor_uf
    return int(uf_total.quantize(Decimal(1), rounding=ROUND_HALF_UP))


def calcular_imponible_topado(
    sueldo_imponible_clp: int, valor_uf: Decimal, tope_uf: Decimal = Decimal("89.9")
) -> int:
    tope_pesos = uf_a_clp(tope_uf, valor_uf)
    if sueldo_imponible_clp < 0:
        raise ValueError("El sueldo imponible no puede ser menor a 0.")
    return min(sueldo_imponible_clp, tope_pesos)


class ResultadoLiquidacion(TypedDict):
    sueldo_bruto_clp: int
    imponible_topado_clp: int
    descuento_afp_clp: int
    descuento_salud_clp: int
    sueldo_liquido_clp: int


def calcular_liquidacion(
    sueldo_base_clp: int,
    valor_uf: Decimal,
    tasa_afp: Decimal,
    tasa_salud: Decimal = Decimal("0.07"),
    tope_uf: Decimal = Decimal("89.9"),
) -> ResultadoLiquidacion:
    """Retorna sueldo_bruto_clp, imponible_topado_clp,descuento_afp_clp, descuento_salud_clp y sueldo_liquido_clp."""
     
    imponible_topado = calcular_imponible_topado(sueldo_base_clp, valor_uf, tope_uf)
    descuento_afp = int(
        (tasa_afp * Decimal(imponible_topado)).quantize(
            Decimal(1), rounding=ROUND_HALF_UP
        )
    )
    descuento_salud = int(
        (tasa_salud * Decimal(imponible_topado)).quantize(
            Decimal(1), rounding=ROUND_HALF_UP
        )
    )

    sueldo_liquido_clp = int(sueldo_base_clp - descuento_afp - descuento_salud)

    return {
        "sueldo_bruto_clp": sueldo_base_clp,
        "imponible_topado_clp": imponible_topado,
        "descuento_afp_clp": descuento_afp,
        "descuento_salud_clp": descuento_salud,
        "sueldo_liquido_clp": sueldo_liquido_clp,
    }