# Criar um programa que leia se um ano qualquer E bisexto #

print('Digite um ano qualquer e veja se ele é bisexto!     (exemplo: 2020)') 
ano = int(input('Digite um ano qualquer!\n'))


if ano % 4 == 0:
    print("o ano de {} é bisexto!".format(ano))

else: 
    print('O ano de {} não é bisexto!'.format(ano))

