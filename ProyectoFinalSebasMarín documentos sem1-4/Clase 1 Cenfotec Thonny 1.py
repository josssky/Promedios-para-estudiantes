#COMENTARIOS DE UNA SOLA LINEA
"""HOLAA N LINEAS
S
S
S"""
print("hola mundo")
#mostrar al usuario pero para solicitar algo
input("Digite su nombre: ")

#VARIABLES
#PASO 1 ES ASIGNARSE UN NOMBRE
#PASO 2 DETERMINAR EL TIPO DE EDAD

"""
Tipos de datos

String--> '' o "25" .. 'palabra' cadena de caracteres
Int--> 25 dato numerico (numero entero)
flotantes (float)--> 2.5 decimales .decimal
Booleano---> True/False 1/0


nombre = ""
edad = 0
estatura = 0.0
esPar = True

""

""CONVERSION DE TIPO DE DATOS

STRING --> NUMERO ENTERO
str-->int---int(str)
'25' --> 25
'STE' --> ERROR

string-->float

int---bool
bool(1) -->True
bool(0) -->False



nombre=input('Digite su nombre: ')
edad=int(input('Digite su edad: '))
estatura=float(input('Digite su estatura: '))
esPar=bool(int(input('Digite 1 si su edad es Par, 0 si su edad es Impar')))

print('Mi nombre es:',nombre,'tengo', edad,'años, y mido:', estatura)
print("Mi nombre es: "+nombre+"tengo",edad+50)
print(f"Mi nombre es:{nombre} tengo {edad} años, y mido: {estatura} m")

"""

#EJERCICIO 1
num1=int(input('Digite un primer numero: '))
num2=int(input('Digite un segundo numero: '))

#Suma +

suma=num1+num2
print(f'{num1}+{num2}={suma}')
#       5+2=7
multi=num1*num2
resultadomulti=suma*multi
print(f"{num1}*{num2}={multi}")
print(resultadomulti)
#Multiplicacion *

#Division /

divi=num1/num2
resultadodivi=multi/divi
print(f"{num1}/{num2}={divi}")
print(resultadodivi)
#Resta -
resta=num1-num2
resultadoresta=divi-resta
print(f'{num1}-{num2}={resta}')
print=(resultadoresta)
#Modulo %
#Exponente ** 2**2



'''
num1
num2

suma
resulSuma=num1+num2 ---> resulSum
multiplicacion
num1*num2 ---> resulMul*resulSuma=ResultadoFinal
resta
num1-num2---> resulRest-ResultadoFinal=ResultadoFinalRes
modulo
exponente
'''
