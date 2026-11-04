def validar_rut(rut_num: int, rut_dv: str) -> bool:
    if rut_num <= 0 or rut_dv == "":
        return False

    factores = [2, 3, 4, 5, 6, 7]
    total = 0

    for i in range(9): # range(9) sirve para RUTs entre 1 y 999 millones
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