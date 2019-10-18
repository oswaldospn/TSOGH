#Exercicio 1
for hora in range (0, 24):
    for minuto in range(0, 60):
        for segundo in range(0,60):
            print(f'{hora:02}:{minuto:02}:{segundo:02}')

#Exercicio 2

finalizar = 0
#Assim foi criado as condições para encerrar o programa.
while (finalizar != -1):
    
    valor1 = int (input("Digite o valor 1(0 ou 1): "))
    valor2 = int (input("Digite o valor 2:(0 ou 1): "))
    valor3 = int (input("Digite o valor 3:(0 ou 1): "))
    #Explicitando todas as variaveis.

    if valor1 == 0 and valor2 == 0 and valor3 == 0:
        print ("Nenhum.")
        finalizar = int (input ("Digite '-1' para finalizar: "))

    elif valor1 == 0 and valor2 == 0 and valor3 == 1:
        print (    "Direita." )
        finalizar = int (input ("Digite '-1' para finalizar: "))

    elif valor1 == 0 and valor2 == 1 and valor3 == 0:
        print (    "Centro." )
        finalizar = int (input ("Digite '-1' para finalizar: "))

    elif valor1 == 0 and valor2 == 1 and valor3 == 1:
        print (    "Centro-Direita." )
        finalizar = int (input ("Digite '-1' para finalizar: "))

    elif valor1 == 1 and valor2 == 0 and valor3 == 0:
        print (    "Esquerda." )
        finalizar = int (input ("Digite '-1' para finalizar: "))

    elif valor1 == 1 and valor2 == 0 and valor3 == 1:
        print (    "Esquerda-Direita." )
        finalizar = int (input ("Digite '-1' para finalizar: "))


    elif valor1 == 1 and valor2 == 1 and valor3 == 0:
        print (    "Centro-Esquerda." )
        finalizar = int (input ("Digite '-1' para finalizar: "))

    elif valor1 == 1 and valor2 == 1 and valor3 == 1:
        print (    "Todos." )
        finalizar = int (input ("Digite '-1' para finalizar: "))
    #Dessa forma se cria todas as possibildiades possiveis para preencher com texto em resposta a tabela.    

    else :
        print ("Valor inválido, digite apenas 0 ou 1.")
        finalizar = int (input ("Digite '-1' para finalizar: "))
    #O texto indica de maneira facíl como fechar o programa.
    #O comando 'else' é usado por ser a ultima variavel possivel que se encaixa no pedido.    






#Exercicio 3

a,b,c = input('Digite um número inteiro(separado em espaços): ').split(' ')
a = int(a)
b = int(b)
c = int(c)
#Dessa forma os números colocados em string se tornam número inteiros
if a<=b<=c:
    print('O menor deles é: ',a)
elif b<=c<=a:
    print('O menor deles é: ',b)
else:
    print('O menor deles é: ',c)  
#Dessa forma se cobre todas as possibilidades.    
if a>=b>=c:      
  print('O maior deles é: ',a)
elif b>=c>=a:  
  print('O maior deles é: ',b)
else:
  print('O maior deles é: ',c)
if a<b<=c:  
  print('A soma dos dois menores é: ',b+a)
elif b<c<=a: 
  print('A soma dos dois menores é: ',b+c) 
elif c<a<=b: 
  print('A soma dos dois menores é: ',a+c) 
#Dessa forma se cobre todas as possibilidades.   
if a>b>c:
 print('Os três números em ordem crescente:', c,b,a)
elif b>c>a:
 print('Os três números em ordem crescente:', b,c,a)
elif c>b>a:
 print('Os três números em ordem crescente:', a,b,c)
elif b>a>c:
 print('Os três números em ordem crescente:', c,a,b)
elif a>c>b:
 print('Os três números em ordem crescente:', b,c,a)
elif c>a>b:
 print('Os três números em ordem crescente:', b,a,c)    
#Dessa forma se cobre todas as possibilidades.     