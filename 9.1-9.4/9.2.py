# 1: Declaro la variable
total_segundos = 7384

# 2: Extraer horas y guardar los segundos sobrantes
horas = total_segundos // 3600
segundos_restantes = total_segundos % 3600

# 3: Extraer minutos y los segundos
minutos = segundos_restantes // 60
segundos = segundos_restantes % 60

# 4: Muestro el resultado
print(f"{horas} horas, {minutos} minutos y {segundos} segundos.")