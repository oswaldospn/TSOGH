#Ex 01
  #Com While

print('Contagem regressiva...')
cont = 10
while (cont >=1):
    print (cont)
    cont = cont -1
print('Fogo!')
  #Com for
print('Contagem regressiva...')
for cont in range (0,10):
    print (cont)
    cont = cont -1
print('Fogo!')


#Ex 02
  #Com While
y = int(input('Digite um nÃºmero inteiro maior que 1: '))
x = 1
while (x <= y):
    print (x)
    x = x + 1

  #Com for

y = int(input('Digite um nÃºmero inteiro maior que 1: '))
x = 1
for x in range (1,y+1):
    print (x)


#Ex 03
#Com While
y = int(input('Digite um nÃºmero inteiro maior que 3: '))
x = 1
while (x <= y):
    print (x)
    x = x + 2

#Com for

y = int(input('Digite um nÃºmero inteiro maior que 3: '))
x = 1
for x in range (1,y+1,2):
    print (x)


#Ex 04

  #Com While
x = int(input('Digite um nÃºmero inteiro: '))
print("Abaixo estÃ£o os 20 primeiros multiplos de: ", x)
cont = x
while (cont <= 20*x+1 ):
    print (cont, end = ';')
    cont = cont + x

  #Com for

y = int(input('Digite um nÃºmero inteiro: '))
print("Abaixo estÃ£o os 20 primeiros multiplos de : ", x)
cont = x
for cont in range (cont,20*x+1,x):
    print (cont, end = ';')


#Ex 05

  #Com While
x = int(input('Digite um número inteiro: '))
print('Tabuada de adição do', x)
y = 1
cont = x
h = 1
j = 6
while h+1<=11:
    print(cont,'+',h,'=',j, end = '\n')
    h = h+1
    j = j+1
  #Com for
x = int(input('Digite um número inteiro: '))
print('Tabuada de adição do', x)
y = 1
cont = x
h = 1
j = 6
for cont in range (h,11):
    print('5','+',h,'=',j, end = '\n')
    h = h+1
    j = j+1
    

#Ex 06

  #Com While
x = int(input('Digite um número inteiro: '))
print('Tabuada de adição:')
cont = 1
while cont<=10 :
    print(x,'+',cont,'=',(cont+ x))
    cont += 1
print('Tabuada de subtração:')
cont = 1
while cont<=10 :
    print(x,'-',cont,'=',(cont - x))
    cont += 1
print('Tabuada de multiplicação:')
cont = 1
while cont<=10 :
    print(x,'*',cont,'=',(cont * x))
    cont += 1
print('Tabuada de divisão:')
cont = 1
while cont<=10 :
    print(x,'/',cont,'=',(cont / x))
    cont += 1

  #Com for
x = int(input('Digite um número inteiro: '))
print('Tabuada de adição:')
cont = 1
for cont in range ( cont,11 ):
    print(x,'+',cont,'=',(cont+ x))
    cont += 1
print('Tabuada de subtração:')
cont = 1
for cont in range ( cont,11 ):
    print(x,'-',cont,'=',(cont - x))
    cont += 1
print('Tabuada de multiplicação:')
cont = 1
for cont in range ( cont,11 ):
    print(x,'*',cont,'=',(cont * x))
    cont += 1
print('Tabuada de divisão:')
cont = 1
for cont in range ( cont,11 ):
    print(x,'/',cont,'=',(cont / x))
    cont += 1


#Ex 07


#Com While
contador = 0
soma = 0
sair = False

while sair== False:
    x = int(input("Digite um número inteiro (0 para sair): "))
    if x==0:
        sair= True
    else:
        contador+=1
        soma = soma +x

print("Foram digitados", contador,"número(s)")
print("Soma dos números digitados:", soma)
print("Média dos números digitados:", soma/contador)

#Ex 08

valido = False

while valido== False:
    valor = int(input("Entre com um valor inteiro em reais: "))
    if valor >0:
        valido = True

if valor%50 !=0:
    if valor//50 >=1:
        print(valor//50, "cédulas de 50 reais")
        valor =  valor - (valor//50)* 50
else:
    print(valor//50, "cédulas de  50 reais"  )
    valor =  valor - (valor//50)* 50

if valor%20 !=0:
    if valor//20 >=1:
        print(valor//20, "cédulas de 20 reais")
        valor =  valor - (valor//20)* 20
else:
    print(valor//20, "cédula de  20 reais"  )
    valor =  valor - (valor//20)* 20

if valor%10 !=0:
    if valor//10 >=1:
        print(valor//10, "cédulas de 10 reais")
        valor =  valor - (valor//10)* 10
else:
    print(valor//10, "cédulas de  10 reais"  )
    valor =  valor - (valor//10)* 10

if valor%5 !=0:
    if valor//5 >=1:
        print(valor//5, "cédulas de 5 reais")
        valor =  valor - (valor//5)* 5
else:
    print(valor//5, "cédula de  5 reais"  )
    valor =  valor - (valor//5)* 5
    
if valor%1 !=0:
    if valor//1 >=1:
        print(valor//1, "cédulas de 1 reais")
        valor =  valor - (valor//1)* 1
else:
    print(valor//1, "cédula de  1 reais"  )
    valor =  valor - (valor//1)*1


#Ex 09

valido = False

while valido== False:
    valor = int(input("Entre com um valor inteiro em reais: "))
    if valor >0:
        valido = True
    else:
            print('É necessário que você digite um valor positivo, diferente de 0.')
if valor%100 !=0:
    if valor//100 >=1:
        print(valor//100, "cédulas de 100 reais")
        valor =  valor - (valor//100)* 100
else:
    print(valor//50, "cédulas de  50 reais"  )
    valor =  valor - (valor//50)* 50

if valor%50 !=0:
    if valor//50 >=1:
        print(valor//50, "cédulas de 50 reais")
        valor =  valor - (valor//50)* 50
else:
    print(valor//50, "cédulas de  50 reais"  )
    valor =  valor - (valor//50)* 50

if valor%20 !=0:
    if valor//20 >=1:
        print(valor//20, "cédulas de 20 reais")
        valor =  valor - (valor//20)* 20
else:
    print(valor//20, "cédula de  20 reais"  )
    valor =  valor - (valor//20)* 20

if valor%10 !=0:
    if valor//10 >=1:
        print(valor//10, "cédulas de 10 reais")
        valor =  valor - (valor//10)* 10
else:
    print(valor//10, "cédulas de  10 reais"  )
    valor =  valor - (valor//10)* 10

if valor%5 !=0:
    if valor//5 >=1:
        print(valor//5, "cédulas de 5 reais")
        valor =  valor - (valor//5)* 5
else:
    print(valor//5, "cédula de  5 reais"  )
    valor =  valor - (valor//5)* 5
    
if valor%1 !=0:
    if valor//1 >=1:
        print(valor//1, "cédulas de 1 reais")
        valor =  valor - (valor//1)* 1
else:
    print(valor//1, "cédula de  1 reais"  )
    valor =  valor - (valor//1)*1




#Ex 10

valido = False

while valido== False:
    valor = float(input("Entre com um valor em reais: "))
    if valor >0:
        valido = True
    else:
            print('É necessário que você digite um valor positivo, diferente de 0.')
if valor%100 !=0:
    if valor//100 >=1:
        print(valor//100, "cédulas de 100 reais")
        valor =  valor - (valor//100)* 100
else:
    print(valor//100, "cédulas de  100 reais"  )
    valor =  valor - (valor//100)* 100

if valor%50 !=0:
    if valor//50 >=1:
        print(valor//50, "cédulas de 50 reais")
        valor =  valor - (valor//50)* 50
else:
    print(valor//50, "cédulas de  50 reais"  )
    valor =  valor - (valor//50)* 50

if valor%20 !=0:
    if valor//20 >=1:
        print(valor//20, "cédulas de 20 reais")
        valor =  valor - (valor//20)* 20
else:
    print(valor//20, "cédula de  20 reais"  )
    valor =  valor - (valor//20)* 20

if valor%10 !=0:
    if valor//10 >=1:
        print(valor//10, "cédulas de 10 reais")
        valor =  valor - (valor//10)* 10
else:
    print(valor//10, "cédulas de  10 reais"  )
    valor =  valor - (valor//10)* 10

if valor%5 !=0:
    if valor//5 >=1:
        print(valor//5, "cédulas de 5 reais")
        valor =  valor - (valor//5)* 5
else:
    print(valor//5, "cédula de  5 reais"  )
    valor =  valor - (valor//5)* 5
    
if valor%1 !=0:
    if valor//1 >=1:
        print(valor//1, "cédulas de 1 reais")
        valor =  valor - (valor//1)* 1
else:
    print(valor//1, "cédula de  1 reais"  )
    valor =  valor - (valor//1)*1

if valor%0.50 !=0:
    if valor//0.50 >=1:
        print(valor//0.50, "moedas de 50 centavos")
        valor =  valor - (valor//0.50)* 0.50
else:
    print(valor//0.50, "moedas de 50 centavos"  )
    valor =  valor - (valor//0.50)* 0.50

if valor%0.1 !=0:
    if valor//0.1 >=1:
        print(valor//0.1, "moedas de 10 centavos")
        valor =  valor - (valor//0.1)* 0.1
else:
    print(valor//0.1, "moedas de 10 centavos"  )
    valor =  valor - (valor//0.1)* 0.1

if valor%0.05 !=0:
    if valor//0.05 >=1:
        print(valor//0.05, "moedas de 05 centavos")
        valor =  valor - (valor//0.05)* 0.05
else:
    print(valor//0.05, "moedas de 05 centavos"  )
    valor =  valor - (valor//0.05)* 0.05

if valor%0.02 !=0:
    if valor//0.02 >=1:
        print(valor//0.02, "moedas de 02 centavos")
        valor =  valor - (valor//0.02)* 0.02
else:
    print(valor//0.02, "moedas de 02 centavos"  )
    valor =  valor - (valor//0.02)* 0.02

if valor%0.01 !=0:
    if valor//0.01 >=1:
        print(valor//0.01, "moedas de 01 centavos")
        valor =  valor - (valor//0.01)* 0.01
else:
    print(valor//0.01, "moedas de 01 centavos"  )
    valor =  valor - (valor//0.01)* 0.01