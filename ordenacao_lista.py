lista = []
lista = input().split(" ") #separa a entrada por espaço e guarda como string
lista = [float(i) for i in lista] # converte em float cada item da lista

lista_ord = sorted(lista) # ordena em ordem crescente


print(lista_ord[0]) # imprime na ordem crescente
print(lista_ord[1])
print(lista_ord[2])
print('\n') #pula uma linha
print(lista[0]) # imprime na ordem inicial
print(lista[1])
print(lista[2])
