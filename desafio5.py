numero = int(input('digite um numero: '))
s = numero - 1
s2 = numero + 1
print('Analisando o valor {}! Seu antecessor é {}, e seu sucessor é {}'.format(numero, s, s2))


numero = int(input('digite um numero: '))
print('Analisando o valor {}! Seu antecessor é {}, e seu sucessor é {}'.format(numero, (numero-1), (numero+1)))


# duas formas acima de fazer o antecessor e sucessor de um numero,
# sendo um dentro do formt e outro sendo criando as varieveis para criar a formatação

n = int(input('qual sua idade?'))
print('sua idade é {}! Parabens ano passado você tinha {}, e ano que vem faz {}'.format(n, (n-1), (n+1)))