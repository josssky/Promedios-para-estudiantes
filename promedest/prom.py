#Pedimos las notas a la persona
nota1=float(input("Escriba su primera nota: "))
nota2=float(input("Escriba su segunda nota: "))
nota3=float(input("Escriba su tercera nota: "))

#Pues el calculo de la nta
prom=(nota1+nota2+nota3) /3

#Resultado de pasar o no
if prom=>65:
    print("Aprobado")
else:
    print("Reprobado")
