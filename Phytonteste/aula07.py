n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma dos valores é {},\n a multiplicação é {},\n e a divisão é {:.3f}'.format(s, m, d))
print('A divisção inteira é {},\n a exponenciação é {}'.format(di, e))