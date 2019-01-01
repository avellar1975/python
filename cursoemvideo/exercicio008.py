#Desafio 016 ##################
'''Python – Exercício 016 – Quebrando um Número'''
num = float(input('Digite um número:'))

num_int = int(num  // 1)

print('O número {} tem a parte inteira {}'.format(num,num_int))


#Desafio 017 ##################
'''Python – Exercício 017 – Catetos e Hipotenusa'''
cateto_a = float(input('Digite o comprimento do cateto oposto:'))
cateto_b = float(input('Digite o comprimento do cateto adjacente:'))
hipotenusa = (cateto_a**2  + cateto_b**2)**(1/2)
print('O comprimento da hipotenusa é {:.2f}'.format(hipotenusa))


#Desafio 018 ##################
from math import sin, cos, tan, radians
angulo = float(input('Digite um ângulo qualquer:'))
sen = sin(radians(angulo))
cose = cos(radians(angulo))
tang = tan(radians(angulo))
print('Análise do ângulo {:.3f}: seno igual a {:.3f}, cosseno igual a {:.3f} e tangente igual a {:.3f}'.format(x, sen, cose, tang))

#Desafio 019 ##################
import random
a = input('Digite o nome o Aluno n.1:')
b = input('Digite o nome o Aluno n.2:')
c = input('Digite o nome o Aluno n.3:')
d = input('Digite o nome o Aluno n.4:')

itens = [a,b,c,d]

print('O aluno escolhido foi {}'.format(random.choice(itens)))


#Desafio 020 ##################
import random
a = input('Digite o nome o Aluno n.1:')
b = input('Digite o nome o Aluno n.2:')
c = input('Digite o nome o Aluno n.3:')
d = input('Digite o nome o Aluno n.4:')

itens = [a,b,c,d]
random.shuffle(itens)

print('A ordem dos alunos foi: {}, {}, {} e {}'.format(itens[0],itens[1],itens[2],itens[3]))

#Desafio 021 ##################
''' Exercício Python 021: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3. '''
import pygame
pygame.init()
pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.play()
pygame.event.wait()
