#Ex.01
primeiro_num = int(input('Por favor, digite o primeiro número: '))
segundo_num = int(input('Por favor, digite o segundo número: '))
terceiro_num = int(input('Por favor, digite o terceiro número: '))
primeira_op = primeiro_num * segundo_num

print('\nMultiplicação de ' + str(primeiro_num) + ' por ' + str(segundo_num) + ': ' + str(primeira_op))
print('Resto dadivisão entre ' + str(primeira_op) + ' e ' + str(terceiro_num) + ': ' + str(primeira_op % terceiro_num)) 

#Ex.02
primeiro_num = int(input('Por favor, digite o primeiro número: '))
segundo_num = int(input('Por favor, digite o segundo número: '))
terceiro_num = int(input('Por favor, digite o terceiro número: '))
quarto_num = int(input('Por favor, digite o quarto número: '))
soma = primeiro_num + segundo_num + terceiro_num
subtração = soma - quarto_num

print('\nOperações efetuadas:')
print(primeiro_num, '+', segundo_num, '+', terceiro_num, '=', soma)
print(soma, '-', quarto_num, '=', subtração)

#Ex.03
primeiro_num = int(input('Por favor, digite o primeiro número: '))
segundo_num = int(input('Por favor, digite o segundo número: '))
terceiro_num = int(input('Por favor, digite o terceiro número: '))
quarto_num = int(input('Por favor, digite o quarto número: '))
quinto_num = int(input('Por favor, digite o quinto número: '))
sexto_num = int(input('Por favor, digite o sexto número: '))
sétimo_num = int(input('Por favor, digite o sétimo número: '))
oitavo_num = int(input('Por favor, digite o oitavo número: '))
soma = primeiro_num + segundo_num + terceiro_num + quarto_num + quinto_num + sexto_num
subtração = soma - sétimo_num - oitavo_num

print('\nOperações efetuadas:')
print(f'{primeiro_num} + {segundo_num} + {terceiro_num} + {quarto_num} + {quinto_num} + {sexto_num} = {soma}')
print(f'{soma} - {sétimo_num} - {oitavo_num} = {subtração}')


#Ex.04
from math import sqrt
primeiro_num = float(input('Por favor, digite o primeiro número real: '))
segundo_num = float(input('Por favor, digite o segundo número real: '))
terceiro_num = float(input('Por favor, digite o terceiro número real: '))
quarto_num = float(input('Por favor, digite o quarto número real: '))

print('\nOperações efetuadas:')
print(f'{primeiro_num} + {terceiro_num} = {primeiro_num + terceiro_num}')
print(f'{segundo_num} + {quarto_num} = {segundo_num + quarto_num}')
print(f'{primeiro_num + terceiro_num} * {segundo_num + quarto_num} = {(primeiro_num + terceiro_num) * (segundo_num + quarto_num)}')
print(f'Raiz quadrada de {(primeiro_num + terceiro_num) * (segundo_num + quarto_num)} = {sqrt((primeiro_num + terceiro_num) * (segundo_num + quarto_num)):.4f}')

#Ex.05
primeiro_num = float(input('Por favor, digite o primeiro número: '))
segundo_num = float(input('Por favor, digite o segundo número: '))
terceiro_num = float(input('Por favor, digite o terceiro número: '))
quarto_num = float(input('Por favor, digite o quarto número: '))
quinto_num = float(input('Por favor, digite o quinto número: '))
sexto_num = float(input('Por favor, digite o sexto número: '))
op_1 = primeiro_num + segundo_num
op_2 = quarto_num - terceiro_num
op_3 = quinto_num / sexto_num
op_4 = op_1 * op_2 * op_3

print('\nOperações efetuadas:')
print(primeiro_num, '+', segundo_num, '=', op_1)
print(quarto_num, '-', terceiro_num, '=', op_2)
print(quinto_num, '/', sexto_num, '=', ('%.5f' % op_3))
print('Resultado final da multiplicação dos três resultados anteriores:', '%015.3f'%op_4)

#Ex.06
primeiro_num = int(input('Por favor, digite o primeiro número: '))
segundo_num = int(input('Por favor, digite o segundo número: '))
terceiro_num = int(input('Por favor, digite o terceiro número: '))
quarto_num = int(input('Por favor, digite o quarto número: '))
quinto_num = int(input('Por favor, digite o quinto número: '))
sexto_num = int(input('Por favor, digite o sexto número: '))
sétimo_num = int(input('Por favor, digite o sétimo número: '))
oitavo_num = int(input('Por favor, digite o oitavo número: '))
nono_num = int(input('Por favor, digite o nono número: '))
décimo_num = int(input('Por favor, digite o décimo número: '))
décimoprimeiro_num = int(input('Por favor, digite o décimo primeiro número: '))
op_a = primeiro_num + segundo_num + terceiro_num
op_b = quinto_num / quarto_num
op_c = sétimo_num - sexto_num
op_d = oitavo_num + nono_num + décimo_num
op_e = op_d - op_c - op_b - op_a
op_f = op_e * décimoprimeiro_num
op_g = op_f // 10
op_g2 = op_f % 10

print('\nOperações efetuadas:')
print(f'{primeiro_num} + {segundo_num} + {terceiro_num} = {op_a}')
print(f'{quinto_num} / {quarto_num} = {op_b}')
print(f'{sétimo_num} - {sexto_num} = {op_c}')
print(f'{oitavo_num} + {nono_num} + {décimo_num} = {op_d}')
print(f'{op_d} - {op_c} - {op_b} - {op_a} = {op_e}')
print(f'{op_e} - {décimo_num} = {op_f}')
print(f'Quociente da divisão de {op_f} // 10: {op_g}')
print(f'Resto da divisão de {op_f} // 10: {op_g2}')
      

#Ex.07
distância = float(input('Digite uma distância em metros: '))

print(f'Distância convertida para milímetros: {distância * 1000}mm.')
print(f'Distância convertida para quilômetros: {distância / 1000}km.')

#Ex.08
dias = int(input('Digite uma quantidade de dias: '))
horas = int(input('Digite uma quantidade de horas: '))
minutos = int(input('Digite uma quantidade de minutos: '))
segundos = int(input('Digite uma quantidade de segundos: '))
total = (((dias * 24) * 60) + (horas * 60) + minutos) * 60 + segundos

print('A soma do tempo lido corresponde a um total de', total, 'segundos')

#Ex.09
p1 = str(input('Digite o nome do produto 1: '))
p1_preço = float(input('Digite o preço do produto 1: R$'))
p1_quantidade = int(input('Quantas unidades do produto 1 foram compradas? '))
p2 = str(input('Digite o nome do produto 2: '))
p2_preço = float(input('Digite o preço do produto 2: R$'))
p2_quantidade = int(input('Quantas unidades do produto 2 foram compradas? '))
p3 = str(input('Digite o nome do produto 3: '))
p3_preço = float(input('Digite o preço do produto 3: R$'))
p3_quantidade = int(input('Quantas unidades do produto 3 foram compradas? '))
p4 = str(input('Digite o nome do produto 4: '))
p4_preço = float(input('Digite o preço do produto 4: R$'))
p4_quantidade = int(input('Quantas unidades do produto 4 foram compradas? '))
p5 = str(input('Digite o nome do produto 5: '))
p5_preço = float(input('Digite o preço do produto 5: R$'))
p5_quantidade = int(input('Quantas unidades do produto 5 foram compradas? '))
total = (p1_quantidade * p1_preço) + (p2_quantidade * p2_preço) + (p3_quantidade * p3_preço) + (p4_quantidade * p4_preço) + (p5_quantidade * p5_preço)

print('\n********************')
print('Lista de produtos')
print('********************')
print(f'\t1) {p1} (R${p1_preço:.2f} - {p1_quantidade} unidade(s)): R${p1_quantidade * p1_preço:.2f}')
print(f'\t2) {p2} (R${p2_preço:.2f} - {p2_quantidade} unidade(s)): R${p2_quantidade * p2_preço:.2f}')
print(f'\t3) {p3} (R${p3_preço:.2f} - {p3_quantidade} unidade(s)): R${p3_quantidade * p3_preço:.2f}')
print(f'\t4) {p4} (R${p4_preço:.2f} - {p4_quantidade} unidade(s)): R${p4_quantidade * p4_preço:.2f}')
print(f'\t5) {p5} (R${p5_preço:.2f} - {p5_quantidade} unidade(s)): R${p5_quantidade * p5_preço:.2f}')
print(f'Total da compra: R${total:.2f}')
print('********************')



#Ex.10
import math
n1 = str(input('Digite o nome do primeiro funcionário: '))
s1 = float(input('Digite quando ganha o primeiro funcionário: R$'))
n2 = str(input('Digite o nome do segundo funcionário: '))
s2 = float(input('Digite quando ganha o segundo funcionário: R$'))
n3 = str(input('Digite o nome do terceiro funcionário: '))
s3 = float(input('Digite quando ganha o terceiro funcionário: R$'))
n4 = str(input('Digite o nome do quarto funcionário: '))
s4 = float(input('Digite quando ganha o quarto funcionário: R$'))
n5 = str(input('Digite o nome do quinto funcionário: '))
s5 = float(input('Digite quando ganha o quinto funcionário: R$'))
total = s1 + s2 + s3 + s4 + s5
média = (s1 + s2 + s3 + s4 + s5) / 5
cubo = pow(total, 3)
quadrado = math.sqrt(média)

print('********************')
print('Funcionários')
print('\n********************')
print(f'Salário 1 ({n1}): R${s1:.2f}')
print(f'\tSalário 2 ({n2}): R${s2:.2f}')
print(f'Salário 3 ({n3}): R${s3:.2f}')
print(f'\tSalário 4 ({n4}): R${s4:.2f}')
print(f'Salário 5 ({n5}): R${s5:2f}')
print('\t####################')
print(f'\tTotal somado dos salários: R${total:2.f}')
print(f'\tMédia salarial da empresa: R${média:2.f}')
print('\t####################')
print('\n********************')
print(f'Somatório dos salários elevado ao cubo: R${total:.2f}')
print(f'Raiz quadrada da média salarial: R${média:.2f}')
print('\n********************')







