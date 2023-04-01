# Crea un programa que le pida al usuario un número entero y luego calcule y muestre la suma de todos los números desde 1 hasta el número ingresado.

# El programa debe utilizar un bucle for para sumar los números.

numeroUsuario = int(input("Introduce un numero entero "))
suma=0
for x in range(1,numeroUsuario+1):
    suma+=x
    
print(suma)