# ADR-001: Precisión Monetaria en CLP y Conversión de UF

**Estado:** Aceptado

## Contexto

En el contexto de la gestión de nóminas en Chile, es fundamental garantizar la precisión en las operaciones monetarias, especialmente cuando se trabaja con la moneda nacional (CLP) y la unidad de fomento (UF). La conversión entre estas dos unidades requiere un manejo cuidadoso para evitar errores en los cálculos y asegurar la conformidad con las normativas locales. Los montos declarados en Previred van en Pesos Chilenos (INTEGER), sin centavos, mientras que los topes imponibles (89,9 UF) y tasas vienen con decimales. Usar float (IEEE 754) para dinero introduce errores de redondeo binario que provocan rechazos de nómina por diferencias de 1 peso.

## Decisión

Se ha decidido establecer una precisión monetaria específica para las operaciones en CLP y la conversión a UF. La precisión se definirá de la siguiente manera:

- Prohibición de uso de float para dinero.
- Usar Decimal con redondeo ROUND_HALF_UP al peso entero más cercano para todas las operaciones monetarias en CLP.

## Consecuencias

Cuadratura contable exacta frente a Previred, a cambio de convertir explicitamente como Decimal antes de persistir como entero.
