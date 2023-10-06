salario = float(input("Cuanto cobras: "))
hipoteca= float(input("De cuanto es la hipoteca: "))
en_cuantos_meses= float(input("En cuantos meses pretendes pagarlo: "))
interes= float(input("Que cantidad de interés tienes, en decimales: "))
print(((hipoteca * interes) + hipoteca )/en_cuantos_meses)
if (((hipoteca * interes) + hipoteca )/en_cuantos_meses)>salario:
    print("no puedes pagarlo en esos meses")