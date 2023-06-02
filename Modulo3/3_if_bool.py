'''
Érase una vez una tierra de leche y miel, habitada por gente feliz y próspera. 
La gente pagaba impuestos, por supuesto, su felicidad tenía límites. 

El impuesto más importante, denominado Impuesto Personal de Ingresos (IPI, para abreviar) 
tenía que pagarse una vez al año y se evaluó utilizando la siguiente regla:

Si el ingreso del ciudadano no era superior a 85,528 pesos, el impuesto era igual al 18%
del ingreso menos 556 pesos y 2 centavos (esta fue la llamada exención fiscal ).

Si el ingreso era superior a esta cantidad, el impuesto era igual a 14,839 pesos y 2 centavos,
más el 32% del excedente sobre 85,528 pesos.
'''

income = float(input("Introduce el ingreso anual: "))

if income < 85528:
	tax = income * 0.18 - 556.02
else:
	tax = (income - 85528) * 0.32 + 14839.02

if tax < 0.0:
	tax = 0.0

tax = round(tax, 0)
print("El impuesto es:", tax, "pesos")

# Entrada de muestra: 10000
# Resultado esperado: El impuesto es: 1244.0 pesos

# Entrada de muestra: 100000
# Resultado esperado: El impuesto es: 19470.0 pesos