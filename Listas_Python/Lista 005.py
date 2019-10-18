#Exercicio 01
num1 = input('Digite um número real(Positivo, negativo ou nulo): ')
if 'nulo' and 'null' and 'NULO' and 'NULL' in num1:
    print(f"O número digitado é {num1} e não contem dígitos númericos.")
else: 
    num = float(num1)
    num1 = num1.replace('-','')
    num1 = num1.replace('.','')
    numero = len(num1)

    if num < 0:
        print(f"O número {num} é negativo e contem {numero} dígitos númericos.")

    elif num >= 0:
        print(f"O número {num} é positivo e contem {numero} dígitos númericos.")

#Exercicio 02
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 13:40:34 2019

@author: Oswald
"""
from unicodedata import normalize
capital = (input('Qual a capital do Brasil?: '))
capital = normalize('NFKD', capital).encode('ASCII','ignore').decode('ASCII').upper().capitalize().lower()
if 'brasilia' in capital:
    print(f'Resposta correta.')
else:    
    print('Resposta incorreta.')

#Exercicio 03

# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 13:40:34 2019

@author: Oswald
"""
num = int((input('Digite um numero inteiro: ')))
if num > 0:
    num1 = num**0.5
    print(f'Raiz quadrada de {num} é {num1:.5f}')
    num2 = str(num)
    num3 = str(num1).replace('.','')
    print(f'{num2[0:1]}-{num2[1:2]}-{num3[0:1]}-{num3[1:2]}-{num3[2:3]}-{num3[3:4]}-{num3[4:5]}-{num3[5:6]}')
else:
    num1 = num**2
    print(f'O quadrado de {num} é {num1:.5f}')
    num2 = str(num)
    num3 = str(num1).replace('.','')
    print(f'{num2[1:2]}-{num2[2:3]}-{num3[0:1]}-{num3[1:2]}-{num3[2:3]}-{num3[3:4]}-{num3[4:5]}-{num3[5:6]}')

#ou, de outra forma, que deixa terminando com '-', mas dessa forma acima caso tenha mais do que 2 digitos nao funciona.
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 13:40:34 2019

@author: Oswald
"""
num = int((input('Digite um numero inteiro: ')))
if num > 0:
    num1 = num**0.5
    print(f'Raiz quadrada de {num} é {num1:.5f}')
    num2 = str(num)
    numero2 = str(num1).replace('.','')
    concate = num2 + numero2[0:6]
    for n in concate:
        print(f'{n}', end='-')  
else:
    num1 = num**2
    print(f'O quadrado de {num} é {num1:.5f}')
    num2 = str(num)
    numero2 = str(num1).replace('.','')
    concate = num2 + numero2[0:6]
    for n in concate:
        print(f'{n}', end='-')
#Exercicio 04
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 13:46:51 2019

@author: Oswald
"""

num = int(input('Digite um número inteiro: '))
if (num % 7 == 0):
   a = ('é')
else:
   a = ('não é')
if (num % 13 == 0):
   b = ('é')
else:
   b = ('não é')
if (num % 55 == 0):
   c = ('é')
else:
   c = ('não é')     
print(f'O número {num} {a} múltiplo de 7, {b} múltiplo de 13 e {c} mútipilo de 55.')

#Exercicio 05(fazendo)

# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 13:40:34 2019

@author: Oswald
"""
import math
num = int(input('Digite um número inteiro: '))
a = num%10
b = num%5
c = num%2
if a == 0 and b == 0 and c == 0:
   print(f'O número {num} é multiplo de 10, 5 e 2.')
else:
        i     = 1  # contador
        n_fat = 1  
while i <= num:
        n_fat = n_fat * i 
        i = i + 1
n_fat1 = str(n_fat)
print(f'O número {num} não é multiplo de 10, 5 e 2.')
print(f'Os 15 primeiros digitos do fatorial de {num} são:  {n_fat1[0:15]}')
log = math.log(num,10)
log = str(log)
print(f'O log na base 10 de {num} é: {log[0:16]}')
#Exercicio 06
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 13:40:34 2019

@author: Oswald
"""
from unicodedata import normalize
nome = (input('Digite o nome de uma pessoa: '))
nome = normalize('NFKD', nome).encode('ASCII','ignore').decode('ASCII').upper().capitalize().lower()
if (nome == 'joao'):
    a = ('José')
    print(f'O nome digitado possui o prenome {a}.')
elif (nome == 'maria'):
        a = ('Maria')
        print(f'O nome digitado possui o prenome {a}.')
else:
    print('O prenome digitado não é José ou Maria')

#Exercicio 07

import math
palavra = str(input('Digite uma palavra: ')).capitalize()
quant = len(palavra)

if quant % 2 != 0:
    print(f"Quantidade de letras ímpares da palavra '{palavra}': {quant}.")
    indice = math.ceil(quant/2) -1
    print(f'Indice da letra central {indice}')
    vogais = ['a', 'e', 'i', 'o', 'u']
    letracentro = str(palavra[indice])
    if letracentro in vogais:
        print(f'A letra central "{letracentro}" é vogal.')
    else:
        print(f'A letra central {letracentro} não é vogal.')

elif quant % 2 == 0:
    print(f"Quantidade de letras pares da palavra '{palavra}': {quant}.")
    indice = math.ceil(quant / 2)
    indice1 = indice - 1
    letrasindice = str(palavra[indice]) + str(palavra[indice1])
    digrafo = ['rr', 'ss']
    print(f'Indice das letras centrais: {indice1} e {indice}')
    if letrasindice in digrafo:
        print(f'As letras centrais "{letrasindice}" são um dígrafo.')
    else:
        print(f'As letras centrais "{letrasindice}" não são um dígrafo.')

#Exercicio 08

encerrar = 0
palavra = input("Digite um texto de 5 caracteres: ")
texto = len(palavra)
if texto > 5:
        print('O texto possui mais que 5 caracteres')
        encerrar = -1

elif texto < 5:
        print('O texto possui menos que 5 caracteres')
elif texto == 5:


    print('Digite "1" para deixar todos os caracteres minúsculos')
    print('Digite "2" para deixar todos os caracteres maiúsculos')
    print('Digite "-1" para encerrar')

    tentativa = int(input('Opção escolhida: '))    
if (tentativa == 1):
            print(palavra.lower())
elif tentativa == 2:
            print(palavra.upper())
elif tentativa == -1:
            encerrar = tentativa
            print('Programa encerrado')



#Exercicio 09

aluno = input("Digite o nome do alunx: ")
nota1, nota2, nota3 = input("Digite as notas finais das três matérias separadas por espaço: ").split(' ')
nota1 = float(nota1)
nota2 = float(nota2)
nota3 = float(nota3)
if nota1 >= 7:
    nota1 = "Aprovado"
elif 7 > nota1 > 3:
    nota1 = "Em recuperação"
else:
    nota1 = "Reprovado."    
if nota2 >= 7:
    nota2 = "Aprovado"
elif 7 > nota2 > 3:
    nota2 = "Em recuperação"
else:
    nota2 = "Reprovado."  
if nota3 >= 7:
    nota3 = "Aprovado"
elif 7 > nota3 > 3:
    nota3 = "Em recuperação"
else:
    nota3 = "Reprovado."      
    
print('*****')
print(f'Situação de "{aluno}"')
print(f'Matéria 1: {nota1}')
print(f'Matéria 2: {nota2}')
print(f'Matéria 3: {nota3}')
print('*****')


#Exercicio 10

verbo = input('Digite um verbo regular no infinitivo: ').lower()
if verbo [-1] != 'r':
    print(f'O verbo não esta no infinitivo')
elif 'ar' in verbo:
    print(f'O verbo {verbo} pertence à 1ª conjugação da língua portuguesa.')
elif 'er' in verbo:
    print(f'O verbo {verbo} pertence à 2ª conjugação da língua portuguesa.') 
elif 'ir' in verbo:
    print(f'O verbo {verbo} pertence à 3ª conjugação da língua portuguesa.')

#Segunda forma de fazer:
primeira_conjugação = ('ar')
segunda_conjugação = ('er')
terceira_conjugação = ('ir')

verbo = input('Digite um verbo regular no infinitivo: ').lower()

verbo_infinitivo = verbo[-1::]
#Ou menos 2

if primeira_conjugação == verbo_infinitivo:
    print(
        f'O verbo {verbo_infinitivo} pertence a 1ª conjugação da lingua portuguesa.')

elif segunda_conjugação == verbo_infinitivo:
    print(
        f'O verbo {verbo_infinitivo} pertence a 2ª conjugação da lingua portuguesa.')

elif terceira_conjugação == verbo_infinitivo:
    print(
        f'O verbo {verbo_infinitivo} pertence a 3ª conjugação da lingua portuguesa.')

elif verbo_infinitivo != primeira_conjugação or segunda_conjugação or terceira_conjugação:
    print(f'A paravra {verbo} não é um verbo no infinitivo.')
    

#Exercicio 11

grupo_1 = ( 'a' , 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k')
grupo_2 = ( 'l','m','n')
grupo_3 = ( 'o','p','q','r','s','t','u','v','w','x','y','z')
nome, sobrenome = input('Digite seu nome completo para descobrir seu grupo de prova: ').lower().split(' ')
Lsobrenome = sobrenome[0]
if Lsobrenome in grupo_1:
    print(f'O aluno(a) {nome} fará prova no grupo 1.')
elif Lsobrenome in grupo_2:
    print(f'O aluno(a) {nome} fará prova no grupo 2.')
else:
    print(f'O aluno(a) {nome} fará prova no grupo 3.')

#Exercicio 12
dd, mm, aaaa = input("Digite uma data no formato(dd/mm/aaaa): ").split('/')  
if not dd.isdigit():
    print("O texto digitado não corresponde a uma data pois possui valores não númericos.")
elif not mm.isdigit():
    print("O texto digitado não corresponde a uma data pois possui valores não númericos.")
elif not aaaa.isdigit():
    print("O texto digitado não corresponde a uma data pois possui valores não númericos.")
if   len(aaaa) != 4:
    print("O texto digitado esta fora do formato esperado(dd/mm/aaaa)")
elif  len(mm) != 2:
    print("O texto digitado esta fora do formato esperado(dd/mm/aaaa)")
elif  len(dd) != 2:
    print("O texto digitado esta fora do formato esperado(dd/mm/aaaa)")
else:    
    dd= int(dd)
    mm= int(mm)
    if dd == 1:
        dd = 'Primeiro'
    if dd == 2:
        dd =('Dois')
    if dd == 3:
        dd=('Três')
    if dd == 4:
        dd=('Quatro')
    if dd == 5:
        dd=('Cinco')
    if dd == 6:
        dd=('Seis')
    if dd == 7:
        dd=('Sete')
    if dd == 8:
        dd=('Oito')
    if dd == 9:
        dd=('Nove')
    if dd == 10:
        dd=('Dez')
    if dd == 11:
        dd=('Onze')
    if dd == 12:
        dd=('Doze')
    if dd == 13:
        dd=('Treze')
    if dd == 14:
        dd=('Catorze')
    if dd == 15:
        dd=('Quinze')
    if dd == 16:
        dd=('Dezesseis')
    if dd == 17:
        dd=('Dezessete')
    if dd == 18:
        dd=('Dezoito')
    if dd == 19:
        dd=('Dezenove')
    if dd == 20:
        dd=('Vinte')
    if dd == 21:
        dd=('Vinte e um')
    if dd == 22:
        dd=('Vinte e dois')
    if dd == 23:
        dd=('Vinte e três')
    if dd == 24:
        dd=('Vinte e quatro')
    if dd == 25:
        dd=('Vinte e cinco')
    if dd == 26:
        dd=('Vinte e seis')
    if dd == 27:
        dd=('Vinte e sete')
    if dd == 28:
        dd=('Vinte e oito')
    if dd == 29:
        dd=('Vinte e nove')
    if dd == 30:
        dd=('Trinta')
    if dd == 31:
        dd=('Trinta e um')
    if mm == 1: 
        mm=('Janeiro')
    if mm == 2: 
        mm=('Fevereiro')
    if mm == 3: 
        mm=('Março')
    if mm == 4: 
        mm=('Abril')
    if mm == 5: 
        mm=('Maio')
    if mm == 6: 
        mm=('Junho')
    if mm == 7: 
        mm=('Julho')
    if mm == 8: 
        mm=('Agosto')
    if mm == 9: 
        mm=('Setembro')
    if mm == 10: 
        mm=('Outubro')
    if mm == 11: 
        mm=('Novembro')
    elif mm == 12: 
        mm=('Dezembro')
    print(f'{dd} de {mm} de {aaaa}')



#ou(Apenas parte)

dia = int(input("Informe o dia de nascimento: "))
mes = int(input("Informe o mes de nascimento: "))
ano = int(input("Informe o ano de nascimento: "))
m = "Janeiro Fev Março Abril Maio Jun Jul Agost Setem Out Nov Dez"
m2 = m.split()

print("Data de nascimento: %i/ %i/ %i"%(dia,mes,ano))
print("Voce nasceu em",dia,"de",m2[mes-1]," ",ano)