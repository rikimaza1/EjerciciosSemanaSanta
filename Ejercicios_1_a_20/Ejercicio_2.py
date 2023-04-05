# Calcular el salario de un empleado
# Entrada
salarioBase = ("Introduzca Salario Base")
pagasExtra = ("Introduzca Pagas Extra ")
complementos = ("Introduzca Complementos")
otrosConceptosRetributivos = ("Introduzca Otros Conceptos Retributivos")
irpf = ("Introduzca IRPF ")
seguridadSocial = ("Introduzca Seguridad Social ")
# Proceso
salarioBruto = salarioBase+pagasExtra+complementos+otrosConceptosRetributivos
deduciones = irpf+seguridadSocial
salarioNeto = salarioBruto - deduciones
# Salida
print(F"El salario neto del empleado es {salarioNeto}")
