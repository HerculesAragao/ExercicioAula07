salario = int(input('Digite o salário do funcionário: '))
if salario > 1500:
    salario = salario * 1.10
else:
    salario = salario * 1.15
print(f'Novo salário é de R${salario:,.2f}')