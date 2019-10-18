#Exercício 01
Palavra1 = input("Digite uma palavra: ")
#Input permite escrever as informações de fora do codigo
Número1 = int(input("Digite um número: "))
#Comando int permite por apenas números inteiros
Palavra2 = input("Digite uma palavra: ")
Número2 = int(input("Digite um número: "))
Palavra3 = input("Digite uma palavra: ")
Número3 = int(input("Digite um número: "))
print(f'{Palavra1}-{Número1}-{Palavra2}-{Número2}-{Palavra3}-{Número3}')
#A função f string nesse caso permite colocar os nomes pre salvos em chaves para ordenar.
Número1x2 = Número1 * 2
Número2x2 = Número2 * 2
Número3x2 = Número3 * 2
print(str(Número3x2)+"-"+(Palavra3 )+"-"+ str(Número2x2)+'-'+ (Palavra2)+'-'+str(Número1x2)+'-'+(Palavra1))
#O comando str permite a leitura de números fora de aspas ou apostofros.


#Exercício 02

print("CONVERSOR DE MOEDA:")
valor = float(input("Escreva o valor em reais: "))
#O valor que vocês quer que seja convertido, Float permite ser real e o comando "input" permite que o usuario escreva o número.
valor_Euro = valor * 0.25
valor_Iene = valor * 26.38
valor_Yuan = valor * 1.75
valor_Dolar = valor * 0.25
#Acíma são as formas matemáticas que fazem a conversão de moeda.
print("R$",valor , " em Euro é: %010.2f " %valor_Euro, "euros; em Iene é: %010.2f " %valor_Iene, " Iene Japonêses; em Yuan é: %010.2f " %valor_Yuan , " Yuan Chineses; em dolar é: %010.2f " %valor_Dolar ," doláres.")
#%"Número de casas totais"."Número de casas depois da virgula.", "float"



#Exercício 03

nome = (input('Digite seu nome completo: '))
origem = (input("Digite o seu local de origem: "))
destino = (input('Digite o seu local de destino: '))
assento= (input("Digite o seu assento: "))
data1= (input('Digite seu dia de embarque:  '))
data2= (input('Digite seu mês de embarque:  '))
data3= (input('Digite seu ano de embarque:  '))
hora1= (input("Digite a sua hora de embarque: "))
hora2= (input("Digite a seus minutos de embarque: "))
#O input para escrever toda informaçõa necessária
print("#" * 60 )
      #O asterisco permite multiplicação não só de palavras mas também de simbolos.
print("COMPANHIA AÉREA VOLARE")     
print("#" * 60 )
print("Nome do passageiro: {}".format(nome))
print("\tOrigem: {}".format(origem))
#O comando \t faz espaçamento de linha
print("\tDestino: {}".format(destino))
print("\t\tData de embarque: {0}/{1}/{2}".format(data1,data2,data3))
#Os números nas chaves correspondem a ordem.
print("\t\tHorário: {0:.02}:{1:.02}".format(hora1,hora2))
print("\tAssento: {}".format(assento))
print("*" * 10)
print("Obrigado por voar conosco!")
print("*" * 10)