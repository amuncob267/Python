# 1: Primero pido los datos
precio = float(input("Precio: "))
unidades = int(input("Unidades: "))
porcentaje = float(input("Porcentaje de descuento: "))

# 2: Aquí dejo los cálculos
subtotal = precio * unidades
descuento = subtotal * (porcentaje / 100)
iva = (subtotal - descuento) * 0.21
total = (subtotal - descuento) + iva

# 3: Muestro los resultados
print(f"Subtotal: {subtotal:.2f} €")
print(f"Descuento: {descuento:.2f} €")
print(f"IVA: {iva:.2f} €")
print(f"Total: {total:.2f} €")

# 4. Compruebo si el envío es gratuito
if total >= 50:  # Por ejemplo 50€
    print("Envío gratuito incluido.")
else:
    print("No supera el mínimo para envío gratuito.")