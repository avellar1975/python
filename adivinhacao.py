print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42
tentativas = 3
rodada =1

while(rodada <= tentativas):
    print("Tentativa {} de {}"py.format(rodada,tentativas))
    chute_str = input("Digite o seu número: ")
    print("Você digitou: ", chute_str)
    chute = int(chute_str)

    acertou = numero_secreto == chute
    maior   = chute > numero_secreto

    if (acertou):
        print("Você acertou!")
        break
    else:
        if(maior):
            print("O seu chute foi maior que o número secreto!")
        else:
            print("O seu chute foi menor que o número secreto!")    

    rodada = rodada + 1
        
print("Fim do jogo")
