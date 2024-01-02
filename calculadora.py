numero1 = int(input('Digite um numero'))
operador = input('digite um operador')
numero2 = int(input('Digite um segundo numero'))

if operador == '+':
    resultado = numero1 + numero2
    print(resultado)
elif operador == '-':
    resultado = numero1 - numero2
    print(resultado)
elif operador == '/':
    resultado = numero1 / numero2
    print(resultado)
elif operador == '*':
    resultado = numero1 * numero2
    print(resultado)
else:
    print('operador incorreto')