'''
Seção de Comandos
A tabela atual do IRRF é:
Base de cálculo mensal | Alíquota | Parcela a deduzir
Até 1.787,77 | - | -
De 1.787,78 até 2.679,29 | 7,5 | 134,08
De 2.679,30 até 3.572,43 | 15,0 | 335,03
De 3.572,44 até 4.463,81 | 22,5 | 602,96
Acima de 4.463,81 | 27,5 | 826,15
'''
salario = float(input('Digite o seu salário: R$'))
if salario <= 1787.77:
    print('Isento')
elif 1787.77 < salario <= 2679.43:
    imposto = (salario * 0.075)-134.08
    salarioliq = salario - imposto
    print(f'Salario Liquido: {imposto:.2f}')
    print(f'R${salarioliq}')
elif 2679.30 < salario <= 3572.44:
    imposto = (salario * 0.15)-335.03
    salarioliq = salario - imposto
    print(f'Salario Liquido: {imposto:.2f}')
    print(f'R${salarioliq}')

elif 3572.44 < salario <= 4463.81:
    imposto = (salario * 0.225)-602.96
    salarioliq = salario - imposto
    print(f'Salario Liquido: {imposto :.2f}')
    print(f'R${salarioliq}')
else:
    imposto = (salario * 0.275)-826.15
    salarioliq = salario - imposto
    print(f'Salario Liquido: {imposto:.2f}')
    print(f'R${salarioliq}')

