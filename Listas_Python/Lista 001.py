#Ex.01
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite mais um número: '))
média = (num1 + num2 + num3) / 3

print('A média entre os três números é: ' + str(média))

#Ex.02
num = int(input('Digite um número: '))
print('Sucessor:', num + 1, '\nAntecessor:', num - 1)

#Ex.03
primeiro_nome = str(input('Digite o primeiro nome: '))
sobrenome = str(input('Digite o sobrenome: '))
rua = str(input('Digite o nome da rua: '))
num_residência = str(input('Digite o número da residência: '))
código_área = str(input('Digite os códigos de área: '))
num_telefone = str(input('Digite o número do telefone: '))

print('\nNome completo: ' + primeiro_nome + sobrenome + '\nEndereço: ' + rua + ', ' + 'número ' + num_residência + '\nTelefone: ' + código_área + num_telefone)

#Ex.04
num = float(input('Digite um número: '))

print('A terça parte inteira do número digitado é:', num // 3)
print('A terça parte real do número digitado é: {:.3f}'.format(num / 3))

#Ex.05
num1 = int(input('Digite o primeiro número inteiro: '))
num2 = int(input('Digite o segundo número inteiro: '))

print(f'\nDividendo: {num1}')
print(f'Divisor: {num2}')
print(f'Quociente: {num1 // num2}')
print(f'Resto: {num1 % num2}')

#Ex.06
valor = float(input('Digite o valor da conta sem taxas: R$'))

print(f'\nValor inicial da conta: R${valor:.2f}')
print(f'Impostos (5%): R${valor * 0.05:.2f}')
print(f'Taxa de serviço (10%): R${valor * 0.10:.2f}')
print(f'Valor final da conta: R${valor + valor * 0.15:.2f}')

#Ex.07
horas = int(input('Digite as horas: '))
minutos = int(input('Digite os minutos: '))
hora_atual = '{0:02}:{1:02}'.format(horas, minutos)

print(f'\nHora atual: {hora_atual}')
print(f'Se passaram {horas * 60 + minutos} minutos desde o início do dia.')


#Ex.08
var1 = float(input('Digite o valor de var1: '))
var2 = float(input('Digite o valor de var2: '))

print('\nValor de var1 antes da troca: {0:010.4f}'.format(var1))
print('Valor de var2 antes da troca: {0:010.4f}'.format(var2))
print('Valor de var1 DEPOIS da troca: {0:010.4f}'.format(var2))
print('Valor de var2 DEPOIS da troca: {0:010.4f}'.format(var1))

#Ex.09
base = float(input('Digite o valor da base (em metros): '))
altura = float(input('Digite o valor da altura (em metros): '))

print(f'\nÁrea do triângulo: {base * altura / 2} mestros quadrados.')

#Ex.10
salário_minímo = float(input('Qual é o valor do salário minímo? R$'))
valor_salário = float(input('Qual é o valor do salário do usuário? R$'))
quantidade_salários_minímos = valor_salário / salário_minímo

print(f'O usuário ganha {quantidade_salários_minímos:.3f} salários minímos.')

#Ex.11
peso = float(input('Digite seu peso: '))

print('Seu peso é gramas é {}g'.format(peso * 1000))
print('Se você engordar 12% passará a pesar {:.2f}kg'.format(peso + peso * 0.12))

#Ex.12
anos = int(input('Digite o componente ano da sua idade: '))
meses = int(input('Digite o componente mês da sua idade: '))
dias = int(input('Digite o componente dia da sua idade: '))
tempo_vivido_em_dias = anos * 365 + meses * 30 + dias

print(f'\nVocê já viveu {tempo_vivido_em_dias} dias')