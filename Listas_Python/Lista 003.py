#Ex.01
#Entrada dos valores pelo usuário
kWh = int(input('Digite a quantidade de energia consumida (em Kwh): '))
instalação = str(input('Digite o tipo de instalação ("R" para residencial; "C" para comercial; "I" para industrial): '))

#Considerando instalação residencial
if instalação == 'R':
  if kWh <= 500:
    print('Preço a pagar pela energia consumida: R${:.2f}'.format (kWh * 0.40))
  else:
    print('Preço a pagar pela energia consumida: R${:.2f}'.format (kWh * 0.65))

#Considerando instalação comercial    
elif instalação == 'C':
  if kWh <= 1000:
    print('Preço a pagar pela energia consumida: R${:.2f}'.format (kWh * 0.55))
  else:
    print('Preço a pagar pela energia consumida: R${:.2f}'.format (kWh * 0.60))  

#Considerando instalação industrial    
elif instalação == 'I':
  if kWh <= 5000:
    print('Preço a pagar pela energia consumida: R${:.2f}'.format (kWh * 0.55))
  else:
    print('Preço a pagar pela energia consumida: R${:.2f}'.format (kWh * 0.60))



#Ex.02
#Mensagem de início do algoritmo e entrada dos valores pelo usuário
print('Você deverá digitar 3 números inteiros')
num1 = int(input('Por favor, digite o primeiro número: '))
num2 = int(input('Por favor, digite o segundo número: '))
num3 = int(input('Por favor, digite o terceiro número: '))

#Verificando qual é o maior número considerando de saída que "num1" o maior 
#(evitando uma operação lógica e deixando o código menor)
maior = num1
if num2 > num1 and num2 > num3:
  maior = num2
if num3 > num1 and num3 > num2:
  maior = num3
print('Maior número digitado:', maior) 

#Verificando qual é o menor número considerando de saída que "num1" o menor 
#(evitando uma operação lógica e deixando o código menor)
menor = num1
if num2 < num1 and num2 < num3:
  menor = num2
if num3 < num1 and num3 < num2:
  menor = num3
print('Menor número digitado:', menor) 

#Ex.03
#Entrada dos valores pelo usuário
casa = float(input('Por favor, digite o valor da compra da casa (em reais): '))
salário = float(input('Por favor, digite o salário: '))
anos = int(input('Em quantos anos pretende financiar? '))

#Calculando a prestação mensal
prestação = casa / (anos * 12)

#Calculando o teto das prestações
teto = salário * 0.3

#Retornando os valores ao usuário
print(f'Teto da prestação: R${teto:.2f}')
print(f'A prestação mensal será de: R${prestação:.2f}')

#Retornando o resultado da consulta
if prestação < teto:
  print('Empréstimo concedido.')
if prestação > teto:
  print('Empréstimo negado')



#Ex.04 - Questão corrigida pela do Rubens. Até agora não entendi direito que porra é essa.
a1 = 1
a2 = 10
a3 = 5

b1 = 2
b2 = 3
b3 = 1

c1 = True
c2 = False
c3 = True

d1 = False
d2 = False
d3 = True

resultado1 = a1 > b1 and c1 or d1
resultado2 = a2 > b2 and c2 or d2
resultado3 = a3 > b3 and c3 or d3

print('Situação 1:', resultado1)
print('Situação 1:', resultado2)
print('Situação 1:', resultado3)

#Ex.05
#Entrada da temperatura em graus pelo usuário
temp = float(input('Digite a temperatura a ser convetida (em graus): '))

#Mensagem das operações de conversão
print('*' * 40)
print('Operações de conversão:')
print('\t1) Celsius para Fahrenheit')
print('\t2) Celsius para Kelvin')
print('\t3) Fahrenheit para Celsius')
print('\t4) Fahrenheit para Kelvin')
print('\t5) Kelvin para Fahrenheit')
print('\t6) Kelvin para Celsius')
print('*' * 40)

#Entrada da operação de conversão pelo usuário
oper = int(input('Digite a operação de conversão: '))

#Saída considerando todas as operações de conversão
if oper == 1:
  temp_conv = (9 / 5 * temp) + 32
  print(f'Resposta: {temp} graus Celsius equivalem a {temp_conv:.2f} graus Fahrenheit.')
elif oper == 2:
  temp_conv = temp + 273
  print(f'Resposta: {temp} graus Celsius equivalem a {temp_conv:.2f} graus Kelvin.')
elif oper == 3:
  temp_conv = 5 / 9 (temp - 32)
  print(f'Resposta: {temp} graus Fahrenheit equivalem a {temp_conv:.2f} graus Celsius.')
elif oper == 4:
  temp_conv = 5 / 9 (temp - 32) + 273
  print(f'Resposta: {temp} graus Fahrenheit equivalem a {temp_conv:.2f} graus Kelvin.')
elif oper == 5:
  temp_conv = (9 / 5 * (temp - 273)) + 32
  print(f'Resposta: {temp} graus Kelvin equivalem a {temp_conv:.2f} graus Fahrenheit.')
elif oper == 6:
  temp_conv = temp - 273
  print(f'Resposta: {temp} graus Kelvin equivalem a {temp_conv:.2f} graus Celsius.')
    


#Ex.06
#Entrada do sexo do/a aluno/a
sexo = str(input('Digite o sexo da pessoa ("M" ou "F"): '))

#Definindo a média
média = 7

#Separado em duas condicionais (Masculino ou Feminino)
if sexo == 'M':
  nome = str(input('Digite o nome do aluno: '))
  #Entrando as notas do aluno (sendo "n" as respectivas notas)
  n1, n2, n3, n4, n5 = (input('Digite as notas finais da 5 matérias, separadas por ponto-e-vírgula: ')).split(';')
  #Convertendo as notas
  n1 = float(n1)
  n2 = float(n2)
  n3 = float(n3)
  n4 = float(n4)
  n5 = float(n5)
  if n1 >= média and n2 >= média and n3 >= média and n4 >= média and n5 >= média:
    print(f'O aluno {nome} foi aprovado no ano letivo.')
  else:
    print(f'O aluno {nome} foi reprovado no ano letivo.')

if sexo == 'F':
  nome = str(input('Digite o nome da aluna: '))
  #Entrando as notas do aluno (sendo "n" as respectivas notas)
  n1, n2, n3, n4, n5 = (input('Digite as notas finais da 5 matérias, separadas por ponto-e-vírgula: ')).split(';')
  #Convertendo as notas
  n1 = float(n1)
  n2 = float(n2)
  n3 = float(n3)
  n4 = float(n4)
  n5 = float(n5)
  if n1 >= média and n2 >= média and n3 >= média and n4 >= média and n5 >= média:
    print(f'A aluna {nome} foi aprovada no ano letivo.')
  else:
    print(f'A aluna {nome} foi reprovada no ano letivo.')

#Ex.07
#Entrada dos valores pelo usuário
num1, num2, num3 = input('Digite três números reais, separados por espaço: ').split()
itr = int(input('Digite um número inteiro: '))

#Convertendo os número reais
num1 = float(num1)
num2 = float(num2)
num3 = float(num3)

#Condicionais para o primeiro número
if num1 < 0:
  print(f'O primeiro número lido ({num1}) é negativo.')
else:
  print(f'O primeiro número lido ({num1}) é positivo.')
  
if num1 > itr:
  print(f'O primeiro número lido ({num1}) é maior que {itr}.')
elif num1 < itr:
  print(f'O primeiro número lido ({num1}) é menor que {itr}.')
elif num1 == itr:
  print(f'O primeiro número lido ({num1}) é igual a {itr}.')
  
if num1 % 2 == 0:
  print(f'O primeiro número lido ({num1}) é par.')
else:
  print(f'O primeiro número lido ({num1}) é ímpar.')
  
#Condicionais para o segundo número
if num2 < 0:
  print(f'O primeiro número lido ({num2}) é negativo.')
else:
  print(f'O primeiro número lido ({num2}) é positivo.')
  
if num2 > itr:
  print(f'O primeiro número lido ({num2}) é maior que {itr}.')
elif num2 < itr:
  print(f'O primeiro número lido ({num2}) é menor que {itr}.')
elif num2 == itr:
  print(f'O primeiro número lido ({num2}) é igual a {itr}.')
  
if num2 % 2 == 0:
  print(f'O primeiro número lido ({num2}) é par.')
else:
  print(f'O primeiro número lido ({num2}) é ímpar.')
  
#Condicionais para o terceiro número
if num3 < 0:
  print(f'O primeiro número lido ({num3}) é negativo.')
else:
  print(f'O primeiro número lido ({num3}) é positivo.')
  
if num3 > itr:
  print(f'O primeiro número lido ({num3}) é maior que {itr}.')
elif num3 < itr:
  print(f'O primeiro número lido ({num3}) é menor que {itr}.')
elif num3 == itr:
  print(f'O primeiro número lido ({num3}) é igual a {itr}.')
  
if num3 % 2 == 0:
  print(f'O primeiro número lido ({num3}) é par.')
else:
  print(f'O primeiro número lido ({num3}) é ímpar.')

  #Ex.08 - Os preços de cada item estão rodando certo, mas o total não está considerando os descontos
#Entrada das características do produtos
nm1, prç1, qtdd1 = input('Digite o nome, preço e quantidade do produto 1, separados por vírgula: ').split(',')
nm2, prç2, qtdd2 = input('Digite o nome, preço e quantidade do produto 2, separados por vírgula: ').split(',')
nm3, prç3, qtdd3 = input('Digite o nome, preço e quantidade do produto 3, separados por vírgula: ').split(',')
nm4, prç4, qtdd4 = input('Digite o nome, preço e quantidade do produto 4, separados por vírgula: ').split(',')
nm5, prç5, qtdd5 = input('Digite o nome, preço e quantidade do produto 5, separados por vírgula: ').split(',')

#Convertendo os preços
prç1 = float(prç1)
prç2 = float(prç2)
prç3 = float(prç3)
prç4 = float(prç4)
prç5 = float(prç5)

#Convertendo as quantidades
qtdd1 = int(qtdd1)
qtdd2 = int(qtdd2)
qtdd3 = int(qtdd3)
qtdd4 = int(qtdd4)
qtdd5 = int(qtdd5)

#Nota de compras
print('#' * 15)
print('Nota de compras')
print('#' * 15)

#Condicionais para o primeiro produto
total1 = prç1 * qtdd1
dsct1 = total1 * 0.2
if qtdd1 >= 12:
  print(f'\t1) {nm1} (R${prç1:.2f}, {qtdd1} unidades): R${total1:.2f} - R${dsct1:.2f} (desconto) = R${total1 - dsct1:.2f}')
else:
  print(f'\t1) {nm1} (R${prç1:.2f}, {qtdd1} unidade): R${total1:.2f}')
  
#Condicionais para o segundo produto
total2 = prç2 * qtdd2
dsct2 = total2 * 0.2
if qtdd2 >= 12:
  print(f'\t2) {nm2} (R${prç2:.2f}, {qtdd2} unidades): R${total2:.2f} - R${dsct2:.2f} (desconto) = R${total2 - dsct2:.2f}')
else:
  print(f'\t2) {nm2} (R${prç2:.2f}, {qtdd2} unidades): R${total2:.2f}')
  
#Condicionais para o terceiro produto
total3 = prç3 * qtdd3
dsct3 = total3 * 0.2
if qtdd3 >= 12:
  print(f'\t3) {nm1} (R${prç3:.2f}, {qtdd3} unidades): R${total3:.2f} - R${dsct3:.2f} (desconto) = R${total3 - dsct3:.2f}')
else:
  print(f'\t3) {nm3} (R${prç3:.2f}, {qtdd3} unidades): R${total3:.2f}')
  
#Condicionais para o quarto produto
total4 = prç4 * qtdd4
dsct4 = total4 * 0.2
if qtdd4 >= 12:
  print(f'\t4) {nm4} (R${prç4:.2f}, {qtdd4} unidades): R${total4:.2f} - R${dsct4:.2f} (desconto) = R${total4 - dsct4:.2f}')
else:
  print(f'\t4) {nm4} (R${prç4:.2f}, {qtdd4} unidades): R${total4:.2f}')
  
#Condicionais para o quinto produto
total5 = prç5 * qtdd5
dsct5 = total5 * 0.2
if qtdd5 >= 12:
  print(f'\t5) {nm5} (R${prç5:.2f}, {qtdd5} unidades): R${total5:.2f} - R${dsct5:.2f} (desconto) = R${total5 - dsct5:.2f}')
else:
  print(f'\t5) {nm5} (R${prç1:.2f}, {qtdd5} unidades): R${total5:.2f}')
  
total = total1 + total2 + total3 + total4 + total5

print(f'Total da compra: R${total}')
print('#' * 15)

#Ex.09
#Entrada dos valores pelo usuário
num1, num2, num3 = input('Digite três números inteiros, separados por espaço: ').split()

#Convertendo os valores
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

#Definindo as condicionais
if num1 < num2 + num3:
  print('As medidas acima podem formar triângulo.')
elif num2 < num1 + num3:
  print('As medidas acima podem formar triângulo.')
elif num3 < num1 + num2:
  print('As medidas acima podem formar triângulo.')  
else:
  print('As medidas acima não podem formar triângulo.')

  #Ex.10
#Entrada das notas pelo o usuário
n1, n2, n3, mEx = input('Digite na sequência as três notas e a média dos exercícios, separados por espaço: ').split()

#Convertendo os valores
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
mEx = float(mEx)

#Definindo a nota
nota = (n1 + n2 * 2 + n3 * 3 + mEx) / 7

#Saída por conceito
if nota >= 9:
  print('Conceito final da disciplina: A')
elif 9 > nota >= 7.5:
  print('Conceito final da disciplina: B')
elif 6 <= nota < 7.5:
  print('Conceito final da disciplina: C')
else:
  print('Conceito final da disciplina: D')

  #Ex.11
#Entrada dos valores pelo usuário
n1, n2, n3 = input('Digite três números inteiros diferentes entre si e separados por espaço: ').split()

#Convertendo os valores
n1 = int(n1)
n2 = int(n2)
n3 = int(n3)

#Verificando qual é o menor número considerando de saída que "n1" o menor 
#(evitando uma operação lógica e deixando o código menor)
menor = n1
if n2 < n1 and n2 < n3:
  menor = n2
if n3 < n1 and n3 < n2:
  menor = n3
print('Menor número:', menor) 

#Verificando qual é o maior número considerando de saída que "n1" o maior 
#(evitando uma operação lógica e deixando o código menor)
maior = n1
if n2 > n1 and n2 > n3:
  maior = n2
if n3 > n1 and n3 > n2:
  maior = n3
print('Maior número:', maior)

#Somando os dois menores
if n1 < n2 and n3 < n2:
  print('Soma dos dois menores:', n1 + n3)
elif n2 < n1 and n3 < n1:
  print('Soma dos dois menores:', n2 + n3)
elif n1 < n3 and n2 < n3:
  print('Soma dos dois menores:', n1 + n2)

#Organizando em ordem crescente
if n1 < n2 and n2 < n3:
  print('Números lidos em ordem crescente: {}, {}, {}.'.format(n1, n2, n3))
elif n2 < n1 and n1 < n3:
  print('Números lidos em ordem crescente: {}, {}, {}.'.format(n2, n1, n3))
elif n3 < n1 and n1 < n2:
  print('Números lidos em ordem crescente: {}, {}, {}.'.format(n3, n1, n2))
elif n1 < n3 and n3 < n2:
  print('Números lidos em ordem crescente: {}, {}, {}.'.format(n1, n3, n2))
elif n2 < n3 and n3 < n1:
  print('Números lidos em ordem crescente: {}, {}, {}.'.format(n2, n3, n1))
elif n3 < n2 and n2 < n1:
  print('Números lidos em ordem crescente: {}, {}, {}.'.format(n3, n2,n1))

  #Ex.12 - Meu resultado não bate com o do Moisés, mas não sei mais o que fazer
#Entrada das informações pelo usuário
h_mês = float(input('Quantas horas foram trabalhadas no mês? '))
h_salário = float(input('Qual é o salário por hora (em reais)? '))

#Calculando salário e a hora extra
if h_mês == 160:
  salário = 160 * h_salário
  print(f'Neste mês, o funcionário receberá R${salário:.2f} de salário.')
if h_mês > 160:
  bônus = (h_mês - 160) * (h_salário * 1.5)
  salário = 160 * h_salário
  total = salário + bônus
  print(f'Neste mês, o funcionário receberá R${total:.2f} de salário.')


#Ex.13
#Entrada dos operandos pelo usuário
op1 = int(input('Por favor, digite o primeiro operando: '))
op2 = int(input('Por favor, digite o segundo operando: '))

#Mensagem das opções de operações
print('*' * 40)
print('Operações aritméticas:')
print('\t1) Adição')
print('\t2) Subtração')
print('\t3) Divisão')
print('\t4) Multiplicação')
print('\t5) Exponeciação')
print('\t6) Resto da divisão')
print('\t7) Quociente da divisão')
print('*' * 40)

#Entrada da operação pelo usuário
oper = int(input('Por favor, digite a operação: '))

#Saída considerando todas as operações aritméticas
if oper == 1:
  print(f'Resultado: {op1} + {op2} = {op1 + op2}')
if oper == 2:
  print(f'Resultado: {op1} + {op2} = {op1 - op2}')
if oper == 3:
  print(f'Resultado: {op1} + {op2} = {op1 / op2}')
if oper == 4:
  print(f'Resultado: {op1} + {op2} = {op1 * op2}')
if oper == 5:
  print(f'Resultado: {op1} + {op2} = {op1 ** op2}')
if oper == 6:
  print(f'Resultado: {op1} + {op2} = {op1 % op2}')
if oper == 7:
  print(f'Resultado: {op1} + {op2} = {op1 // op2}')