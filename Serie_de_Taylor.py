#Actividad 4 
# Karla Itzel Barrera Aza 

def funcion_exponencial(x):
	suma = 0

	for n in range(0, 50):
 	 suma += math.pow(x, n) / math.factorial(n)

	return suma

print("Resultado con la función exponencial: ", funcion_exponencual(2))
print("Resultado con la funcion math.exp ", math.exp(2))
