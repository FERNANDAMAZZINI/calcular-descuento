#crear un programa que calcule el descuento en compras en funcion del monto total de la compra y mostrar el monto final
def calcular_descuento(precio_original, porcentaje_descuento):
    """Calcula el precio final después de aplicar un descuento."""
    descuento = precio_original * (porcentaje_descuento / 100)
    precio_final = precio_original - descuento
    return precio_final

# Ejemplo de uso
precio = float(input("Ingrese el precio original: "))
descuento_porcentaje = float(input("Ingrese el porcentaje de descuento: "))

precio_final = calcular_descuento(precio, descuento_porcentaje)

print(f"El precio final después del descuento es: {precio_final:.2f}")