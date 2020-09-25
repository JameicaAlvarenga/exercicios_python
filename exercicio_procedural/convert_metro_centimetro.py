#Faça um Programa que converta metros para centímetros.

def convert_m_cm (metro):
    return (metro * 100)

m= float(input("Informe a metragem desejada:"))
print("O valor em centimetros é: %1.4f" %convert_m_cm(m))