# Calculadora em Python

print("\n******************* Python Calculator *******************")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("\nSelecione o número da operação desejada: \n")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcoes = ['1','2','3','4']

while True:
    escolha = input("\nDigite sua opção (1/2/3/4): ")
    if escolha in opcoes:
       break
    else:
       print('Opção inválida')
        
    
num1 = int(input("\nDigite o primeiro número: "))
while True:
    num2 = int(input("\nDigite o segundo número: "))
    if num2 == 0 and escolha == '4':
        print('Não pode ter divisor igual a zero')
    else:
        break


if escolha == '1':
	print("\n")
	print(num1, "+", num2, "=", add(num1, num2))
	print("\n")

elif escolha == '2':
	print("\n")
	print(num1, "-", num2, "=", subtract(num1, num2))
	print("\n")

elif escolha == '3':
	print("\n")
	print(num1, "*", num2, "=", multiply(num1, num2))
	print("\n")

elif escolha == '4':
	print("\n")
	print(num1, "/", num2, "=", divide(num1, num2))
	print("\n")