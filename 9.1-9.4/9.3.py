# Caso 1: No cumple los requisitos
matriculada = True
autorizacion_especial = False
edad = 17

puede_acceder = (matriculada and edad >= 18) or autorizacion_especial
print(f"Caso 1 - Puede acceder?: {puede_acceder}")  # False

# Caso 2: Cumple 18
matriculada = True
autorizacion_especial = False
edad = 18

puede_acceder = (matriculada and edad >= 18) or autorizacion_especial
print(f"Caso 2 - ¿Puede acceder?: {puede_acceder}")  # True