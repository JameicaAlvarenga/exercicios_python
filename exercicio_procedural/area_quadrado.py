'''Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.'''

def area_quadrado(a):
    return (a**2)*2

a1=float(input("Informe a area do quadrado:"))
print("A area do quadrado é %1.3f" %area_quadrado(a1),  "e o dobro dessa área é: %1.3f" %area_quadrado(a1))