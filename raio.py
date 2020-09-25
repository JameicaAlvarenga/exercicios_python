'''Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.'''

def raio(r):
    pi=3.14
    return (pi*(r**2))

r2=float(input("Informe o raio:"))
print("A área da circuferencia é: %1.4f" %raio(r2))