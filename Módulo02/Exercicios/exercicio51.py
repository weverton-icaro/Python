#Programa que leia o primeiro termo e a razão de uma Progressão Aritmética
#No final, mostre os 10 primeiros termos dessa progressão.

primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razão
for c in range (primeiro, decimo + razão, razão):
  print('{} '.format(c), end='-> ')
print('Fim')