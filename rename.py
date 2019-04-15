# autor: Evandro Avellar
# data: 15/04/2019

# -- Documentação -----------------------------------------
# Ex: span_teste.txt -> dosiero_teste.txt
# Renomeia os arquivos iniciados com span_ removendo eles
# Adiciona dosiero_ nos nomes dos arquivos
# o parametro filename[:-4] retira os quatro útimos caracteres
# o parametro filename[5:] retira os 5 primeiros caracteres
# Importante que o arquivo rename.py esteja dentro do diretório

# Importando biblioteca os
import os

for filename in os.listdir("."):
    if filename.startswith("span_"):
        os.rename(filename, filename[5:])

for nomo in os.listdir("."):
        if nomo[-2:] != 'py':
            nova_nomo = 'dosiero_' + nomo
            os.rename(nomo,nova_nomo)
