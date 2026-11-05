import pytest

from app.domain.previred_builder import (
    construir_linea_previred,
    exportar_nomina_previred,
    validar_linea_previred,
)


def test_construir_linea_00():
    linea = construir_linea_previred(rut_num=11111111,rut_dv="1", apellido_paterno="Pérez",apellido_materno="Soto",nombres="Juan",dias_trabajados=30,imponible_clp=3_416_200,cotizacion_afp_clp=385_006,cotizacion_salud_clp=239_134,codigo_movimiento=0,tipo_linea="00")
    assert len(linea.split(';')) == 105


def test_construir_linea_01():
    linea = construir_linea_previred(rut_num=11111111,rut_dv="1", apellido_paterno="Pérez",apellido_materno="Soto",nombres="Juan",dias_trabajados=30,imponible_clp=3_416_200,cotizacion_afp_clp=385_006,cotizacion_salud_clp=239_134,codigo_movimiento=0,tipo_linea="01")
    assert len(linea.split(';')) == 105
    assert linea.split(";")[13] == "01"
    assert linea.split(";")[28] == "0"
    
def test_validar_linea():
    assert validar_linea_previred("11111111;1;Perez;Soto;Juan") is False


def test_validar_linea_vacia():
    assert validar_linea_previred("") is False
    
def test_exportar_nomina_error():
    with pytest.raises(ValueError):
        exportar_nomina_previred([])
        
def test_exportar_nomina_exito():
    linea_00 = construir_linea_previred(
        rut_num=11111111,
        rut_dv="1",
        apellido_paterno="Pérez",
        apellido_materno="Soto",
        nombres="Juan",
        dias_trabajados=30,
        imponible_clp=3_416_200,
        cotizacion_afp_clp=385_006,
        cotizacion_salud_clp=239_134,
        codigo_movimiento=0,
        tipo_linea="00",
    )
    linea_01 = construir_linea_previred(
        rut_num=11111111,
        rut_dv="1",
        apellido_paterno="Pérez",
        apellido_materno="Soto",
        nombres="Juan",
        dias_trabajados=30,
        imponible_clp=3_416_200,
        cotizacion_afp_clp=385_006,
        cotizacion_salud_clp=239_134,
        codigo_movimiento=3,
        tipo_linea="01",
    )
    txt = exportar_nomina_previred([linea_00, linea_01])
    assert len(txt.splitlines()) == 2