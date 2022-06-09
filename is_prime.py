#Primer ejercicio, tarea 1 
# Karla Itzel Barrera Aza 


def is_prime(P):

	prime = True
	i = 2

	while i < P:
		residuo = division (P, i) [1]
		if residuo == 0:

			prime = False
			break

		else:
		     i += 1

		return prime 
