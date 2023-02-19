#39. Elabore um programa que:
# leia o peso de 5 pessoas
# Informe o mais pesado
# Informe o mais leve

def maior(Peso1,Peso2,Peso3,Peso4,Peso5):
    max = Peso1

    if Peso2 > max:
        max = Peso2
    if Peso3 > max:
        max = Peso3
    if Peso4 > max:
        max = Peso4
    if Peso5 > max:
        max = Peso5

    return max

def menor(Peso1,Peso2,Peso3,Peso4,Peso5):
    min = Peso1

    if Peso2 < min:
        min = Peso2
    if Peso3 < min:
        min = Peso3
    if Peso4 < min:
        min = Peso4
    if Peso5 < min:
        min = Peso5

    return min

def menu():
    Peso1 =int(input("Qual o Peso da 1° pessoa? "))
    Peso2 =int(input("Qual o Peso da 2° pessoa? "))
    Peso3 =int(input("Qual o Peso da 3° pessoa? "))
    Peso4 =int(input("Qual o Peso da 3° pessoa? "))
    Peso5 =int(input("Qual o Peso da 5° pessoa? "))

    print(f"\nO Mais Pesado, Pesa: {maior(Peso1,Peso2,Peso3,Peso4,Peso5)}Kg")
    print(f"O Mais Leve, Pesa: {menor(Peso1,Peso2,Peso3,Peso4,Peso5)}Kg")
    print()

while True:
    menu()