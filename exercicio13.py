# salarioantigo = float(input('Qual salario do funcionario: '))
# reajuste =  15 
# resultado = (salarioantigo * reajuste) / 100  #primeira tentativa que tive ao fazer
# resultado2 = salarioantigo + resultado
# print(resultado2)

# import tkinter as tk
# from tkinter import messagebox

# def calcular_reajuste():
#     salarioantigo = float(salario_entry.get())
#     reajuste = 15
#     resultado = (salarioantigo * reajuste) / 100
#     resultado2 = salarioantigo + resultado
#     messagebox.showinfo("Novo salário", f"O novo salário é: {resultado2}")

# root = tk.Tk()

# salario_label = tk.Label(root, text="Qual o salário do funcionário:")
# salario_label.pack()

# salario_entry = tk.Entry(root)
# salario_entry.pack()

# calcular_button = tk.Button(root, text="Calcular reajuste", command=calcular_reajuste)
# calcular_button.pack()

# root.mainloop()



salario = float(input('seu salario ? R$'))
novo = salario * 15 / 100
somaS = salario + novo
print('voce tinha um salario de R${}, e agora com 15% de desconto, Voce ganhara R${}'.format(salario, somaS))