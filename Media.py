#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

def media_bimestre (bim1,bim2,bim3,bim4):
    return (bim1+bim2+bim3+bim4)/4

Bimestre1 = float(input("Nota 1° bimestre:"))
Bimestre2 = float(input("Nota 2° bimestre:"))
Bimestre3 = float(input("Nota 3° bimestre:"))
Bimestre4 = float(input("Nota 4° bimestre:"))

print ("A média do aluno é: %1.2f" %media_bimestre(Bimestre1,Bimestre2,Bimestre3,Bimestre4))
