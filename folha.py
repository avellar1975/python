"""Calcula Folha CLT."""

faixa = [1045, 2089.6, 3134.4, 6101.06]
aliquota = [7.5, 9, 12, 14]
taxa = [x/100 for x in aliquota]
"""
situação 1 - salario <= faixa1
situacao 2 - faixa1 < salario <= faixa2
situacao 3 - faixa2 < salario <= faixa3
situacao 4 - faixa3 < salario <= faixa4
situacao 5 - salario > faixa4
"""


def calcula_inss(salario):
    """Função recebe salario e devolve contribuição."""
    if salario <= faixa[0]:
        contribuicao = salario * taxa[0]
    elif faixa[0] < salario <= faixa[1]:
        contrib_1 = faixa[0] * taxa[0]
        contrib_2 = (salario - faixa[0]) * taxa[1]
        contribuicao = contrib_1 + contrib_2
    elif faixa[1] < salario <= faixa[2]:
        contrib_1 = faixa[0] * taxa[0]
        contrib_2 = (faixa[1] - faixa[0]) * taxa[1]
        contrib_3 = (salario - faixa[1]) * taxa[2]
        contribuicao = contrib_1 + contrib_2 + contrib_3
    elif faixa[2] < salario <= faixa[3]:
        contrib_1 = faixa[0] * taxa[0]
        contrib_2 = (faixa[1] - faixa[0]) * taxa[1]
        contrib_3 = (faixa[2] - faixa[1]) * taxa[2]
        contrib_4 = (salario - faixa[2]) * taxa[3]
        contribuicao = contrib_1 + contrib_2 + contrib_3 + contrib_4
    elif faixa[3] < salario:
        contribuicao = 713.08
    return round(contribuicao, 2)
