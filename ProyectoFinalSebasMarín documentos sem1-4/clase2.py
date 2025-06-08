
#Condicionales

#Condicional Simple --: TRUE

#Los miercoles se paga la entrada a mitad de precio

""""""""""
precio = int(input("Digite el precio de la entrada: "))
día = int(input("Digite el día en el que se encuentra:\n1.Lunes \n2.Martes \n3.Miervcoles \n4.Jueves \n\nSus opciones:  "))
#igualdad ==
#desigualdad !=
#día== miercoles
#lunes == miercoles --> False
if (día == 3):
    precio=precio/2
    print("Se hizo una reducción del precio")

print(f"El precio de la entrada es: {precio}")
"""""
"""
#CONDICION DOBLE --> True False
"""
"""
if(condicion):
    accion
else:
    accion
"""
"""

num=int(input("Digite un número: "))
#><=
if(num>=0):
    mensaje="Positivo"
else:
    mensaje="Negativo"
    
print(f"El número: {num} es un número {mensaje}")

if(num%2 != 0):
    mensaje="Impar"
else:
    mensaje="Par"

print(f"El número también es: {mensaje}")

"""
"""
numsecreto=25
"""

#Pregunte su nombre y luego determine si puede conducir
#Un mensaje llamandolo por su nombre y diciendole 
#Al saber la edad se decide si puede conducir o no

nombre=(input("Digite su nombre: "))

edad=int(input("Digite su edad: "))
if(edad>=18):
    mensaje="SI"
else:
    mensaje="No"
licencia=(input("¿Tiene licencia?:  "))
if licencia=="Si":
    respuesta="Si tiene licencia"
elif licencia=="no":
    respuesta= "no puede conducir porque no tiene licencia"
#Si el resultado es "Si" si tiene licencia
#Si el resultado es "No" no tiene licencia
#Acepta sí y no con o sin tilde y con o sin mayusculas

    

print(f"Usted {nombre} {mensaje} puede conducir porque tiene {edad} años y {respuesta}")
