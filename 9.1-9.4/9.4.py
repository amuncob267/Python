# 1: Plazas iniciales
plazas = 12

# 2: Actualización con asignación aumentada
plazas -= 3  # Reserva 3 plazas 
plazas += 1  # Cancela 1 reserva

# 3: Mostrar número final
print(f"Plazas disponibles: {plazas}")

estado = "Hay plazas" if plazas > 0 else "Completo"
print(estado)