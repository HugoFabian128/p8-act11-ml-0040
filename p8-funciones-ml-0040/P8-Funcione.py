# ==============================================================================
# ACTIVIDAD: FUNCIONES EN PYTHON (EL PYTHONISTA)
# Hugo Fabian NC = 0040 | Lista = 17
#
# Ejercicios del 1 al 30 (Referencia: elpythonista.com)
# ==============================================================================

print("--- EJERCICIOS: EL PYTHONISTA ---")

# Ejercicio 1: Función básica sin parámetros
def saludar():
    print("1. ¡Hola! Bienvenido al sistema de gestión.")

saludar()


# Ejercicio 2: Función con parámetros posicionales y retorno
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return round(imc, 2)

print("2. IMC calculado:", calcular_imc(75, 1.75))


# Ejercicio 3: Parámetros con valores por defecto
def clasificar_glucosa(nivel, unidad="mg/dL"):
    if nivel < 100:
        return f"{nivel} {unidad} -> Normal"
    else:
        return f"{nivel} {unidad} -> Elevada"

print("3.", clasificar_glucosa(85))
print("3.", clasificar_glucosa(140))


# Ejercicio 4: Uso de *args (múltiples argumentos posicionales)
def promedio_presion(*lecturas):
    return sum(lecturas) / len(lecturas)

print("4. Promedio de presión:", promedio_presion(120, 125, 118, 130))


# Ejercicio 5: Uso de **kwargs (argumentos con clave variables)
def registrar_paciente(nombre, **datos):
    return {"nombre": nombre, "detalles": datos}

print("5. Registro:", registrar_paciente("Carlos", edad=45, glucosa=110))


# Ejercicio 6: Retorno de múltiples valores (Tupla)
def evaluar_salud(glucosa, presion):
    alerta_glucosa = glucosa >= 126
    alerta_presion = presion >= 130
    return alerta_glucosa, alerta_presion

alerta_g, alerta_p = evaluar_salud(140, 120)
print(f"6. Alerta Glucosa: {alerta_g} | Alerta Presión: {alerta_p}")
print("Hugo Fabian NC = 0040 NL  = 17")