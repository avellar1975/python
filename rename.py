# autor: Evandro Avellar
# data: 15/04/2019

# -- Documentação -----------------------------------------
# Ex: span_teste.txt -> dosiero_teste.txt
# Renomeia os arquivos iniciados com span_ removendo eles
# Adiciona dosiero_ nos nomes dos arquivos
# o parametro filename[:-4] retira os quatro útimos caracteres
# o parametro filename[5:] retira os 5 primeiros caracteres

# Importando biblioteca os
import os

for filename in os.listdir("."):
    if filename.startswith("span_"):
        os.rename(filename, filename[5:])

for nome in os.listdir("."):
        if nome[-2:] != 'py':
            new_filename = 'dosiero_' + nome
            os.rename(nome,new_filename)
