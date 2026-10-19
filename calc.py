def calcular_igv(monto):
    return monto * 0.18


def aplicar_descuento(monto, porcentaje):
    return monto * (1 - porcentaje / 100)


def aplicar_recargo(monto, porcentaje):
    return monto * (1 + porcentaje / 100)

def calcular_envio(monto, distrito):
    if monto >= 200:
        return 0
    if distrito == "Lima":
        return 10
    if distrito == "Callao":
        return 12
    return 20