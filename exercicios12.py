produto = float(input('Qual valor do produto para receber o desconto de 5%?'))
novo = produto - (produto * 5 / 100)
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(produto, novo))


salario = 20000
porc = float(input('quanto voce ganha de porcentagem?'))
novo = porc - (salario * 5 / 100)
print(porc, novo)