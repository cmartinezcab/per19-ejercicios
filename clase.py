import sys

print("-------------------------------------------")
print("Programa para el análisis de niveles de glucosa.")
print("Introduzca primero el tipo de glucosa al que corresponde la medida.")
print("Luego introduzca la medida obtenida (en mg/dL).")
print()
print("Los valores aceptados para tipo de glucosa son:")
print("plasma, total o aleatoria.")
print()
print("El valor de la medida debe ser un número real positivo mayor que cero")
print("y menor que 500.")
print("-------------------------------------------")

print()
tipo = input("Introduzca el tipo de glucosa a medir: ")
tipo = tipo.lower()

if tipo not in ("plasma", "total", "aleatoria"):
	print("Tipo de glucosa incorrecto. Los valores aceptados son:")
	print("plasma, total o aleatoria.")
	sys.exit(1)

if tipo == "plasma":
	plasma_glucose = int(input("Inserta valor de glucosa en plasma (mg/dL): "))
	if plasma_glucose < 72:
		print("Nivel de glucosa en plasma es bajo.")
	elif 72 <= plasma_glucose <= 110:
		print("Nivel de glucosa en plasma es normal.")
	else:
		print("Nivel de glucosa en plasma es alto.")

elif tipo == "total":
	full_glucose = int(input("Inserta valor de glucosa total (mg/dL): "))
	if full_glucose < 60:
		print("Nivel de glucosa total es bajo.")
	elif 60 <= full_glucose <= 100:
		print("Nivel de glucosa total es normal.")
	else:
		print("Nivel de glucosa total es alto.")

elif tipo == "aleatoria":
	random_glucose = int(input("Inserta valor de glucosa aleatoria (mg/dL): "))
	if random_glucose < 70:
		print("Nivel de glucosa aleatoria es bajo.")
	elif 70 <= random_glucose <= 140:
		print("Nivel de glucosa aleatoria es normal.")
	else:
		print("Nivel de glucosa aleatoria es alto.")

print()
print("Fin del programa.")
       
