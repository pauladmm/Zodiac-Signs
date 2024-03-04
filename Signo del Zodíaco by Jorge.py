def signo_zodiaco(dia, mes):
    if (mes == 12 and dia >= 22) or (mes == 1 and dia <= 20):
        return"Eres Capricornio"
    elif (mes == 1 and dia >= 21) or (mes == 2 and dia <= 19):
        return"Eres Acuario"
    elif (mes == 2 and dia >=20) or (mes == 3 and dia <=20):
        return"Eres Piscis"
    elif (mes == 3 and dia >= 21) or (mes == 4 and dia <= 20):
        return"Eres Aries"
    elif (mes == 4 and dia >= 21) or (mes == 5 and dia <= 20):
        return"Eres Tauro"
    elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 21):
        return"Eres Géminis"
    elif (mes == 6 and dia >= 22) or (mes == 7 and dia <= 23):
        return"Eres Cancer"
    elif (mes == 7 and dia >= 24) or (mes == 8 and dia <= 23):
        return"Eres Leo"
    elif (mes == 8 and dia >= 24) or (mes == 9 and dia <= 23):
        return"Eres Virgo"
    elif (mes == 9 and dia >= 24) or (mes == 10 and dia <= 22):
        return"Eres Libra"
    elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 22):
        return"Eres Escorpio"
    elif (mes == 11 and dia >= 23) or (mes == 12 and dia <= 21):
        return"Eres Sagitario"
    else:
        return"No tienes signo."

try:
    dia_nacimiento = int(input("Ingresa el día de tu cumpleaños: "))
    mes_nacimiento = int(input("Ingresa el mes de tu cumpleaños (en número): "))

    if not (1 <= mes_nacimiento <= 12):
        raise ValueError("El mes debe estar entre 1 y 12.")
except ValueError as e:
    print(f"Error: {e}")
    print("Por favor, ingresa un número válido para el mes.")
else:
    # Obtener y mostrar el signo
    signo = signo_zodiaco(dia_nacimiento, mes_nacimiento)
    print(f"{signo}.")
