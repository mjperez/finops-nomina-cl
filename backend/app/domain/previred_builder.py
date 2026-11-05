from app.domain.chilean_rules import validar_rut


def construir_linea_previred(
    rut_num: int,
    rut_dv: str,
    apellido_paterno: str,
    apellido_materno: str,
    nombres: str,
    dias_trabajados: int,
    imponible_clp: int,
    cotizacion_afp_clp: int,
    cotizacion_salud_clp: int,
    codigo_movimiento: int = 0,
    tipo_linea: str = "00",
) -> str:
    if not (tipo_linea == "00" or tipo_linea == "01"):
        raise ValueError("Tipo de línea debe ser 00 o 01")

    if not validar_rut(rut_num, rut_dv):
        raise ValueError("Rut inválido")

    campos = ["0"] * 105

    campos[0] = str(rut_num)
    campos[1] = rut_dv.upper()
    campos[2] = apellido_paterno
    campos[3] = apellido_materno
    campos[4] = nombres
    campos[13] = tipo_linea
    campos[14] = str(codigo_movimiento)

    if tipo_linea == "00":
        campos[10] = str(dias_trabajados)
        campos[28] = str(imponible_clp)
        campos[29] = str(cotizacion_afp_clp)
        campos[63] = str(imponible_clp)
        campos[64] = str(cotizacion_salud_clp)

    return ";".join(campos)


def validar_linea_previred(linea: str) -> bool:
    partes = linea.split(";")

    if not partes[0].isdigit():
        return False

    return (
        len(partes) == 105
        and validar_rut(int(partes[0]), partes[1])
        and partes[13] in ("00", "01")
    )


def exportar_nomina_previred(lineas: list[str]) -> str:
    if not lineas:
        raise ValueError("Error de nómina vacía")

    for linea in lineas:
        if not validar_linea_previred(linea) or not linea:
            raise ValueError(f"Error de línea en nómina: {linea}")

    return "\n".join(lineas)
