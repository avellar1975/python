n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))

a = n1 + n2
s = n1 - n2
d = n1 / n2
m = n1 * n2
p = n1 ** n2
mod = n1 % n2
di = n1 // n2

print('A soma entre {} e {} é {}'.format(n1, n2, a))
print('A subtração entre {} e {} é {}'.format(n1, n2, s))
print('A divisão entre {} e {} é {:.3f}'.format(n1, n2, d))
print('A multiplicação entre {} e {} é {}'.format(n1, n2, m))
print('A potência de {} por {} é {}'.format(n1, n2, p))
print('O módulo de {} por {} é {}'.format(n1, n2, mod))
print('A divisão inteira de {} por {} é {}'.format(n1, n2, di))

