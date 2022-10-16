salario = int(input())

if salario <= 600:
  percentual = 17
  reajuste = (salario/100) * percentual
  novo_salario = (salario/100) * percentual + salario
  print('Novo salario:',"{:.2f}".format(novo_salario))
  print('Reajuste ganho:',"{:.2f}".format(reajuste))
  print('Em percentual: {} %'.format(percentual))
elif salario <= 900:
  percentual = 13
  reajuste = (salario/100) * percentual
  novo_salario = (salario/100) * percentual + salario
  print('Novo salario:',"{:.2f}".format(novo_salario))
  print('Reajuste ganho:',"{:.2f}".format(reajuste))
  print('Em percentual: {} %'.format(percentual))
elif salario <= 1500:
  percentual = 12
  reajuste = (salario/100) * percentual
  novo_salario = (salario/100) * percentual + salario
  print('Novo salario:',"{:.2f}".format(novo_salario))
  print('Reajuste ganho:',"{:.2f}".format(reajuste))
  print('Em percentual: {} %'.format(percentual))
elif salario <= 2000:
  percentual = 10
  reajuste = (salario/100) * percentual
  novo_salario = (salario/100) * percentual + salario
  print('Novo salario:',"{:.2f}".format(novo_salario))
  print('Reajuste ganho:',"{:.2f}".format(reajuste))
  print('Em percentual: {} %'.format(percentual))
else:
  percentual = 5
  reajuste = (salario/100) * percentual
  novo_salario = (salario/100) * percentual + salario
  print('Novo salario:',"{:.2f}".format(novo_salario))
  print('Reajuste ganho:',"{:.2f}".format(reajuste))
  print('Em percentual: {} %'.format(percentual))
