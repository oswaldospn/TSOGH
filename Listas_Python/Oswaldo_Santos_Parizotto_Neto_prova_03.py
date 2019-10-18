#Exercicio 01
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 20:27:29 2019

@author: Oswald
"""
from unicodedata import normalize
fecha = 0
while fecha != -1: #Dessa forma o programa irá fechar quando o comando -1 for exposto.
    pesoTerra = float(input('Digite um peso: ')) #O peso em float para permitir maior variedade de valores.
    gravidade = input('Digite o nome do planeta que deseja saber o peso do objeto para servir de codigo:  \n mercurio\n venus\n saturno\n marte \n jupiter\n urano: ')
    gravidade =  normalize('NFKD', gravidade).encode('ASCII','ignore').decode('ASCII').upper().capitalize().lower() #Usando normalize para nao importa a forma, corrigir para letras minusculas sem acentos.
    peso = float(pesoTerra/10)
    if gravidade == 'mercurio' :
        gravidadeP = float(0.37)
        peso_final = float(gravidadeP * peso)
        print(f'O peso no planeta {str(gravidade)} é: "{float(peso_final)}".')
    if gravidade == 'venus':
        gravidadeP = float(0.88)
        peso_final = float(gravidadeP * peso)
        print(f'O peso no planeta {str(gravidade)} é: "{float(peso_final)}".')
    if gravidade == 'marte' :
        gravidadeP = float(0.38)
        peso_final = float(gravidadeP * peso)
        print(f'O peso no planeta {str(gravidade)} é: "{float(peso_final)}".')
    if gravidade == 'jupiter' :
        gravidadeP = float(2.64)
        peso_final = float(gravidadeP * peso)
        print(f'O peso no planeta {str(gravidade)} é: "{float(peso_final)}".')
    if gravidade == 'saturno' :
        gravidadeP = float(1.15)
        peso_final = float(gravidadeP * peso)
        print(f'O peso no planeta {str(gravidade)} é: "{float(peso_final)}".')
    if gravidade == 'urano' :
        gravidadeP = float(1.17)
        peso_final = float(gravidadeP * peso)
        print(f'O peso no planeta {str(gravidade)} é: "{float(peso_final)}".')
    fecha = int(input('Digite -1 para encerrar:(ou qualquer outra coisa para continuar e ver o peso em oturos planetas.) '))
    gravidade = input('Digite o nome do planeta que deseja saber o peso do objeto para servir de codigo:  \n mercurio\n venus\n saturno\n marte \n jupiter\n urano: ')
    gravidade =  normalize('NFKD', gravidade).encode('ASCII','ignore').decode('ASCII').upper().capitalize().lower()

      
else:
    
    print('Obrigado por usar o programa.')


#Exercicio 02

# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 20:27:29 2019

@author: Oswald
"""
c = 1

while (c != 0): #Dessa forma enquanto nao digitar 0 o codigo nao ira parar.
    num1, num2 = input('Digite dois numero separados por "-": ').split('-') #O split permite mais de uma variavel.
    code = input(' Digite um dos codigos:\n    -1:Adição\n    -2:Subtração\n    -3:Divisão\n-    4:Multiplicação\n    -5:Exponenciação\n    -6:Resto da divisão\n    -7:Quociente da divisão\n    -0:Sair do programa: ') #Usando \n formata os paragrafos e 4 espaços se iguala a uma indexazação.
    a = float(num1)
    b = float(num2)
    c = float(code)
    if c == 1.0:
        d = a + b
        print(f'O resultado da sua conta é "{d}"')
    elif c == 2.0:
        d = a - b
        print(f'O resultado da sua conta é "{d}"')
    elif c == 3.0:
        d = a/b
        print(f'O resultado da sua conta é "{d}"')
    elif c == 4.0:
        d = a*b
        print(f'O resultado da sua conta é "{d}"')
    elif c == 5.0:
        d = a **b
        print(f'O resultado da sua conta é "{d}"')
    elif c == 6.0:
        d = a % b
        print(f'O resultado da sua conta é "{d}"')
    elif c == 7.0:
        d = a // b
        print(f'O resultado da sua conta é "{d}"')
    else:
        print(f'Código invalido.')
        #Cada condição demonstra um dos comandos para a calculadora. sendo que caso nao seja nenhum dos conhecido demonstrará uma tela avisando o mesmo.
else:
    print('Obrigado por usar o programa.')

#Exercico 03:
