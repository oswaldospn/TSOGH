#Exercicio 01

texto = input('Por favor digite o texto: ')
texto_1 = input('Por favor digite outro texto: ')
if texto_1 not in texto:
    print(f'O texto "{texto_1}" não está dentro do texto "{texto}"')
else:
        vezesR = texto.rfind(texto_1)
        vezes = texto.find(texto_1)
        print(f'O texto "{texto_1}" ocorre {texto.count(texto_1)} vezes no texto "{texto}"')
        print(f'O texto "{texto_1}" foi encontrado na posição {vezes} do texto "{texto}"')
        print(f'O texto "{texto_1}" foi encontrado na posição {vezesR} do texto "{texto}"')

#exercicio 02:

#Funciona mas mostra "CTB" e não "CBT"
texto = input('Por favor digite o texto: ')
texto_1 = input('Por favor digite outro texto: ')
intersec = ""
for i in texto:
    if i in texto_1 and not i in intersec:
        intersec += i
if intersec not in texto and texto_1:
    print(f'Não existem caracteres comuns aos dois textos.')
else:
        print(f'Os caracteres comuns ao texto são "{intersec}"')
    
#funciona
texto = input('Por favor digite o texto: ')
texto_1 = input('Por favor digite outro texto: ')
intersec = ''.join(set(texto).intersection(texto_1))
if not intersec:
    print(f'Não existem caracteres comuns aos dois textos.')
else:
    print(f'Os caracteres comuns ao texto são "{intersec}"')

#Exercicio 03 

texto = input('Por favor digite o texto: ')
texto_1 = input('Por favor digite outro texto: ')
texto_2 = texto.replace(""," ")
texto_3 = texto_1.replace(""," ")
a = set(texto_2.split())
b = set(texto_3.split())
simetric_diference = ''.join(set(a).symmetric_difference(b))
if not intersec:
    print(f'Não existem caracteres que apareçam apenas em um dos textos.')
else:
    print(f'Os caracteres que aparecem somente em um texto são "{simetric_diference}"')
#Exercicio 04

texto= input('Por favor digite o texto: ').upper()
texto_1 = texto.replace(""," ")
a = texto_1.split()
alfabeto = {'A' , 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'}
if "A" in a:
    print(f'O caractere "A" aparece {[texto.count("A")]} vezes.')
if "B" in a:
    print(f'O caractere "B" aparece {[texto.count("B")]} vezes.')
if "C" in a:
    print(f'O caractere "C" aparece {[texto.count("C")]} vezes.')
if "D" in a:
    print(f'O caractere "D" aparece {[texto.count("D")]} vezes.')
if "E" in a:
    print(f'O caractere "E" aparece {[texto.count("E")]} vezes.')
if "F" in a:
    print(f'O caractere "F" aparece {[texto.count("F")]} vezes.')
if "G" in a:
    print(f'O caractere "G" aparece {[texto.count("G")]} vezes.')
if "H" in a:
    print(f'O caractere "H" aparece {[texto.count("H")]} vezes.')
if "I" in a:
    print(f'O caractere "I" aparece {[texto.count("I")]} vezes.')
if "J" in a:
    print(f'O caractere "J" aparece {[texto.count("J")]} vezes.')
if "K" in a:
    print(f'O caractere "K" aparece {[texto.count("K")]} vezes.')
if "L" in a:
    print(f'O caractere "L" aparece {[texto.count("L")]} vezes.')
if "N" in a:
    print(f'O caractere "M" aparece {[texto.count("M")]} vezes.')
if "M" in a:
    print(f'O caractere "N" aparece {[texto.count("N")]} vezes.')
if "O" in a:
    print(f'O caractere "O" aparece {[texto.count("O")]} vezes.')
if "P" in a:
    print(f'O caractere "P" aparece {[texto.count("P")]} vezes.')
if "Q" in a:
    print(f'O caractere "Q" aparece {[texto.count("Q")]} vezes.')
if "R" in a:
    print(f'O caractere "R" aparece {[texto.count("R")]} vezes.')
if "S" in a:
    print(f'O caractere "S" aparece {[texto.count("S")]} vezes.')
if "T" in a:
    print(f'O caractere "T" aparece {[texto.count("T")]} vezes.')
if "U" in a:
    print(f'O caractere "U" aparece {[texto.count("U")]} vezes.')
if "V" in a:
    print(f'O caractere "V" aparece {[texto.count("V")]} vezes.')
if "W" in a:
    print(f'O caractere "W" aparece {[texto.count("W")]} vezes.')
if "X" in a:
    print(f'O caractere "X" aparece {[texto.count("X")]} vezes.')
if "Z" in a:
    print(f'O caractere "Z" aparece {[texto.count("Z")]} vezes.')
if "Y" in a:
    print(f'O caractere "Y" aparece {[texto.count("Y")]} vezes.')

#Exercicio 05(tirando apenas um TG e não todos os TG's)

texto = input('Por favor digite o texto: ')
texto_1 = input('Por favor digite outro texto: ')
print(f'O texto restante após as retiradas é "{texto.replace(texto_1,"")}"')

#Tentativa 02 falha:
import re
texto = ('AAFFGAA')
texto_1 = ('FG')
a = re.sub('texto_1','',texto)
print(f'O texto restante após as retiradas é {a}')
#Exercicio 06

texto1 = input('Por favor digite um texto que sera usado de base para as alterações:')
texto2 = input('Por favor digite um grupo de caracteres que será substituido por outro.')
texto3 = input('Porfavor digite  o grupo de caracteres que irá substituir')

if texto2 in texto1:
	texto = texto1.replace(texto2, texto3)
	print(f'Este é o novo texto após a retirada dos caracteres"{texto}"')
else:
	print(f'Não foram digitados caracteres a serem retirados. Portando o texto permanece o mesmo"{texto1}"')
#Exercicio 07

import re
txt = input('Por favor digite um texto: ')
txt1 = input('Por favor digite outro texto: ')
txt_lower = txt.lower()
txt_lower1= txt1.lower()
qnt=len(txt_lower)
qnt1=len(txt_lower1)
a = txt_lower.replace(" ","")
b = a.replace(",","")
c = b.replace(".","")
d = txt_lower1.replace(" ","")
e = a.replace(",","")
f = b.replace(".","")
qnt_=len(c)
qnt_1=len(f)
espaço = re.sub('[áéíóúâêîôûãiõABCDEFGHIJKLMNOPQRSTUWVXYZabcdefghijklmnopqrstuvwxyz.,´`^~]', '', txt_lower)
espaço_qnt = len(espaço)
espaço_novo = re.sub('[áéíóúâêîôûãiõABCDEFGHIJKLMNOPQRSTUWVXYZabcdefghijklmnopqrstuvwxyz.,´`^~]', '', txt_lower1)
espaço_qnt_novo = len(espaço_novo)
ponto = re.sub('[áéíóúâêîôûãiõABCDEFGHIJKLMNOPQRSTUWVXYZabcdefghijklmnopqrstuvwxyz ,´`^~]', '', txt_lower)
ponto_qnt = len(ponto)
ponto_novo = re.sub('[áéíóúâêîôûãiõABCDEFGHIJKLMNOPQRSTUWVXYZabcdefghijklmnopqrstuvwxyz ,´`^~]', '', txt_lower1)
ponto_qnt_novo = len(ponto_novo)
virg = re.sub('[áéíóúâêîôûãiõABCDEFGHIJKLMNOPQRSTUWVXYZabcdefghijklmnopqrstuvwxyz .´`^~]', '', txt_lower)
virg_qnt = len(virg)
virg_novo = re.sub('[áéíóúâêîôûãiõABCDEFGHIJKLMNOPQRSTUWVXYZabcdefghijklmnopqrstuvwxyz. ´`^~]', '', txt_lower1)
virg_qnt_novo = len(virg_novo)
print(f'Primeiro texto: "{txt}"')
print(f'Segundo texto: "{txt1}"')
print(f'O primeiro texto possui {qnt} caracteres, {qnt_} letras, {espaço_qnt} espaços, {virg_qnt} virgulas, {ponto_qnt} pontos. ')
print(f'O segundo texto possui {qnt1} caracteres, {qnt_1} letras, {espaço_qnt_novo} espaços, {virg_qnt_novo} virgulas, {ponto_qnt_novo} pontos.')
if txt is not txt1:
    print(f'Os dois textos nao sao identicos se considerar todos os caracteres.')
iguais = re.sub('[áéíóúâêîôûãiõ., ´`^~]', '', txt_lower)
iguais1 = re.sub('[áéíóúâêîôûãiõ., ´`^~]', '', txt_lower1)
if iguais ==  iguais1:
     print(f'Se considerar apenas as letras os dois textos são identicos.')
else:
    print(f'Se considerar apenas as letras os dois textos não são identicos.')
print(f'O primeiro texto invertido é "{txt[::-1]}"')
print(f'O segundo texto invertido é "{txt1[::-1]}"')
print(f'O primeiro texto invertido em minusculas é "{c[::-1].lower()}"')
print(f'O segundo texto invertido em minusculas é "{f[::-1].lower()}"')

#Exercicio 08

palavra = input("Por favor digite uma palavra: ")
cont = 0 
while cont < len(palavra):
    c = int(cont)
    print(palavra[c])
    cont += 1 
#ou

for c in input("Digite seu nome: "): print(c)
#Exercicio 09

palavra = input('Digite uma palavra: ')
for c in range(0, len(palavra)+1):
    print(palavra[:c])
#Exercicio 10

palavra= input('Digite uma palavra: ')
palavra2 = ""
palavra2 = palavra
for letra in palavra:
	s+=letra
for c in range (len(palavra)):
	h = s[0:(len(palavra))-c:]
	print(h)
#Exercicio 11

import re
cct= ""
lf= []
cont=0
con2=[]
fc= ""

frase = input("Informe a frase: ").lower()
frase_contavel = re.sub('[àèìòùÀÈÌÒÙáéíóúýÁÉÍÓÚÝâêîôûÂÊÎÔÛãñõÃÑÕäëïöüÿÄËÏÖÜŸåÅðÐøØ,.-]', '', frase)
for letra in frase_contavel:
	if (letra != " "):
		fc+=letra
		lf.append(letra)
for i in lf[::-1]:
  	cct+=i
	
if(fc == cct):
	print(f'A frase {frase} é um palindromo.')
else:
	print(f'A frase {frase} não é um palindromo.')
#Exercicio 12

import math
data = input("Digite a string de entrada: ")
#data = '#06/05/1856#23/09/1939#'
data1 = data.replace("#", "") 
f, g, h, i = data.split("#")
a, b, c = g.split("/")
d, e, j = h.split("/")
f = c.split("#")
anoN= int(c)
mesN= int(b)
diaN= int(a)
anoM= int(j)
mesM= int(e)
diaM= int(d)



diasAnoN = anoN*365
if mesN == 1:
    n=31
if mesN == 2:
    n=30
if mesN == 3:
    n=31
if mesN == 4:
    n=30
if mesN == 5:
    n=30#certo é 31
if mesN == 6:
    n=30
if mesN == 7:
    n=31
if mesN == 8:
    n=31
if mesN == 9:
    n=30
if mesN == 10:
    n=31
if mesN == 11:
    n=30
if mesN == 12:
    n=31
diasMesN = mesN*n
diasAnoM = anoM*365
if mesM == 1:
    nM=31
if mesM == 2:
    nM=30
if mesM == 3:
    nM=31
if mesM == 4:
    nM=30
if mesM == 5:
    nM=31
if mesM == 6:
    nM=30
if mesM == 7:
    nM=31
if mesM == 8:
    nM=31
if mesM == 9:
    nM=30
if mesM == 10:
    nM=31
if mesM == 11:
    nM=30
if mesM == 12:
    nM=31
diasMesM = mesM*nM
diasT= int((diasAnoM-diasAnoN)+(diasMesM-diasMesN)+(diaM-diaN))
anoT = diasT//365
mesT = ((diasT%365)/30)
diaT = ((diasT%365)%30)


print(f'Data de nascimento: {data1[0:10]}')
print(f'Data de falecimento: {data1[10:20]}')
print(f'Esta pessoa viveu: {(anoT)} anos, {math.floor(mesT)} meses, {diaT} dias.')
#Exercicio 13

import math

nome1 = input('Digite um nome: ')
salario1= float(input('Digite um salário: '))
nome2 = input('Digite um nome: ')
salario2= float(input('Digite um salário: '))
nome3 = input('Digite um nome: ')
salario3 = float(input('Digite um salário: '))
nome4 = input('Digite um nome: ')
salario4 = float(input('Digite um salário: '))
nome5 = input('Digite um nome: ')
salario5= float(input('Digite um salário: '))
nome6 = input('Digite um nome: ')
salario6= float(input('Digite um salário: '))
nome7 = input('Digite um nome: ')
salario7= float(input('Digite um salário: '))
nome8 = input('Digite um nome: ')
salario8 = float(input('Digite um salário: '))
nome9 = input('Digite um nome: ')'
salario9 = float(input('Digite um salário: '))
nome10 = input('Digite um nome: ')
salario10= float(input('Digite um salário: '))
nome11 = input('Digite um nome: ')
salario11= float(input('Digite um salário: '))
nome12 = input('Digite um nome: ')
salario12= float(input('Digite um salário: '))
nome13 = input('Digite um nome: ')
salario13 = float(input('Digite um salário: '))
nome14 = input('Digite um nome: ')
salario14 = float(input('Digite um salário: '))
nome15 = input('Digite um nome: ')
salario15= float(input('Digite um salário: '))
#nome1 = 'Fulano da Silva'
#salario1= float(1000)
#nome2 = 'Beltrano de Souze'
#salario2= float(2000)
#nome3 = 'Sicrano dos Santos'
#salario3 = float(2500)
#nome4 = 'Maria das Couves'
#salario4 = float(3000)
#nome5 = 'João Ninguém'
#salario5= float(4000)
#nome6 = 'Maria Chiquinha'
#salario6= float(2230)
#nome7 = 'João Valentão'
#salario7= float(1400)
#nome8 = 'Nonô sem dente'
#salario8 = float(27000)
#nome9 = 'Robernélson da Luz'
#salario9 = float(3000)
#nome10 = 'José Maria João'
#salario10= float(1000)
#nome11 = 'Agrícola Beterraba areia Leão'
#salario11= float(1500)
#nome12 = 'Kenquem que Ninguém Quer'
#salario12= float(800)
#nome13 = 'Lindolfa Celidônia Calafange de Tefé'
#salario13 = float(25000)
#nome14 = 'Simplicio Simplório da Simplicidade Simples'
#salario14 = float(10000)
#nome15 = 'Anônimo João Toquato'
#salario15= float(7200)

a1 = 'Sálarios 1 a 5'
b1 = 'Sálarios 6 a 10'
c1 = 'Sálarios 11 a 15'
a = 'Salário 1 ({nome1}:{len(nome1)}): RS{salario1:.2f}'
b = 'Salário 2 ({nome2}:{len(nome2)}): RS{salario2:.2f}'
c = 'Salário 3 ({nome3}:{len(nome3)}): RS{salario3:.2f}'
d = 'Salário 4 ({nome4}:{len(nome4)}): RS{salario4:.2f}'


print(50*'#')
print(f' {a1.center(50)} ')
print(50*'#')
print(f'    Salário 1 ({nome1}:{len(nome1)}): RS{salario1:.2f}')
print(f'    Salário 2 ({nome2}:{len(nome2)}): RS{salario2:.2f}')
print(f'    Salário 3 ({nome3}:{len(nome3)}): RS{salario3:.2f}')
print(f'    Salário 4 ({nome4}:{len(nome4)}): RS{salario4:.2f}')
print(f'    Salário 5 ({nome5}:{len(nome5)}): RS{salario5:.2f}')
print(50*'#')
print(f' {b1.center(50)} ')
print(50*'#')
print(f'    Salário 6 ({nome6}:{len(nome6)}): RS{salario6:.2f}')
print(f'    Salário 7 ({nome7}:{len(nome7)}): RS{salario7:.2f}')
print(f'    Salário 8 ({nome8}:{len(nome8)}): RS{salario8:.2f}')
print(f'    Salário 9 ({nome9}:{len(nome9)}): RS{salario9:.2f}')
print(f'    Salário 10 ({nome10}:{len(nome10)}): RS{salario10:.2f}')
print(50*'#')
print(f' {c1.center(50)} ')
print(50*'#')
print(f'    Salário 11 ({nome11}:{len(nome11)}): RS{salario11:.2f}')
print(f'    Salário 12 ({nome12}:{len(nome12)}): RS{salario12:.2f}')
print(f'    Salário 13 ({nome13}:{len(nome13)}): RS{salario13:.2f}')
print(f'    Salário 14 ({nome14}:{len(nome14)}): RS{salario14:.2f}')
print(f'    Salário 15 ({nome15}:{len(nome15)}): RS{salario15:.2f}')
print(50*'#')
salarioTotal =salario1 + salario2 + salario3 + salario4 + salario5 + salario6 +  salario7 + salario8 + salario9 + salario10 + salario11 + salario12 + salario13 + salario14 + salario15
salarioMedia = math.floor(salarioTotal/15)
if salarioMedia % 10 == 0:
    e_nao10 = 'é'
else:
    e_nao10 = 'não é'
if salarioMedia % 5 == 0:
    e_nao5 = 'é'
else:
    e_nao5 = 'não é'
if salarioMedia % 2 == 0:
    e_nao2 = 'é'
else:
    e_nao2 = 'não é'
print(f'    Total somado dos salário dos funcionários: RS{salarioTotal:.2f}')
print(f'    Média salarial da empresa: RS{math.floor(salarioMedia)}')
print(f'    A parte inteira da média {int(salarioMedia)} {e_nao10} divisivel por 10')
print(f'    A árte inteira da média {int(salarioMedia)} {e_nao5} divisivel por 5')
print(f'    A parte inteira da média {int(salarioMedia)} {e_nao2} divisivel por 2')
print(50*'#')
todosNome = (nome1 + nome2 + nome3 + nome4 + nome5 + nome6 +  nome7 + nome8 + nome9 + nome10 + nome11 + nome12 + nome13 + nome14 + nome15).lower()
mariaX = todosNome.count('maria')
joaoX = todosNome.count('joão')
if mariaX % 2 == 0:
    impar_parM = 'par'
else:
    impar_parM = 'impar'
if joaoX % 2 == 0:
     impar_parJ = 'par'
else:
     impar_parJ = 'impar'
print(f'    Ocorrências da palavra Maria: {mariaX} é um número {impar_parM}')
print(f'    Ocorrência da palavra João: {joaoX} é um número {impar_parJ}')
print(50*'#')

#Exercicio 14

a, b, c, d = input('Digite 83 caracteres, tendo 30 no nome, 30 no local, separados por # e com data no formato dd/mm/aaaa: ').strip(' ').split('#')
#a, b, c, d = 'Sigmund Freud                 #06/05/1856#23/09/1939#Império Austro-Hungaro        '.strip(' ').split('#')

cont =  len(a) + len(b) + len(c) + len(d)                  
while (cont != 72):
    a, b, c, d = input('Digite 83 caracteres, tendo 30 no nome, 30 no local, separados por # e com data no formato dd/mm/aaaa: ').strip(' ').split('#')
    cont =  len(a) + len(b) + len(c) + len(d)
    if cont == 72:
        a_1 = 'Biografia'
    nome = a
    dataN = b
    dataM = c
    local = d
    anoN = int(b[6:10])
    anoM = int(c[6:10])
    diaN = int(b[0:2])
    diaM = int(c[0:2])
    mesM = int(b[3:5])
    mesN = int(c[3:5])
    idade = anoM - anoN
    idade_1 = 2019 - anoN
    if anoN % 2 == 0:
        impar_par = 'Par'
    else:
        impar_par = ('impar')
    if anoM % 2 == 0:
        impar_par1 = 'Par'
    else:
        impar_par1 = ('impar')
        if mesM == 1:
            nM=31
        if mesM == 2:
            nM=30
        if mesM == 3:
            nM=31
        if mesM == 4:
            nM=30
        if mesM == 5:
            nM=31
        if mesM == 6:
            nM=30
        if mesM == 7:
            nM=31
        if mesM == 8:
            nM=31
        if mesM == 9:
            nM=30
        if mesM == 10:
            nM=31
        if mesM == 11:
            nM=30
        if mesM == 12:
            nM=31
        if mesN == 1:
            n=31
        if mesN == 2:
            n=30
        if mesN == 3:
            n=31
        if mesN == 4:
            n=30
        if mesN == 5:
            n=31
        if mesN == 6:
            n=30
        if mesN == 7:
            n=31
        if mesN == 8:
            n=31
        if mesN == 9:
            n=30
        if mesN == 10:
            n=31
        if mesN == 11:
            n=30
        if mesN == 12:
            n=31
        dias =  n - diaN
        diasM = nM - diaM
        print(50*'#')
        print(a_1.center(50))
        print(50*'#')
        print(f'Nome completo: {nome}')
        print(f'Data de nascimento: {dataN}')
        print(f'Local de nascimento: {local}')
        print(f'Morte: {dataM}')
        print(f'Idade ao falecer: {idade} anos.\n')
        print(f'{nome} nasceu há {idade_1} anos atrás.')
        print(f'{nome} nasceu em um ano {impar_par}.')
        print(f'{nome} morreu em um ano {impar_par1}.')
        print(f'Quando ele nasceu, faltavam {dias} dias para o ultimo dia do mês.')
        print(f'Quando ele morreu, faltavam {diasM} dias para o último dia do mês.')
        print(50*'#')
        print(50*'#')
else:
    a_1 = 'Biografia'
    nome = a
    dataN = b
    dataM = c
    local = d
    anoN = int(b[6:10])
    anoM = int(c[6:10])
    diaN = int(b[0:2])
    diaM = int(c[0:2])
    mesM = int(b[3:5])
    mesN = int(c[3:5])
    idade = anoM - anoN
    idade_1 = 2019 - anoN
    if anoN % 2 == 0:
        impar_par = 'Par'
    else:
        impar_par = ('impar')
    if anoM % 2 == 0:
        impar_par1 = 'Par'
    else:
        impar_par1 = ('impar')
        if mesM == 1:
            nM=31
        if mesM == 2:
            nM=30
        if mesM == 3:
            nM=31
        if mesM == 4:
            nM=30
        if mesM == 5:
            nM=31
        if mesM == 6:
            nM=30
        if mesM == 7:
            nM=31
        if mesM == 8:
            nM=31
        if mesM == 9:
            nM=30
        if mesM == 10:
            nM=31
        if mesM == 11:
            nM=30
        if mesM == 12:
            nM=31
        if mesN == 1:
            n=31
        if mesN == 2:
            n=30
        if mesN == 3:
            n=31
        if mesN == 4:
            n=30
        if mesN == 5:
            n=31
        if mesN == 6:
            n=30
        if mesN == 7:
            n=31
        if mesN == 8:
            n=31
        if mesN == 9:
            n=30
        if mesN == 10:
            n=31
        if mesN == 11:
            n=30
        if mesN == 12:
            n=31
        dias =  n - diaN
        diasM = nM - diaM
        print(50*'#')
        print(a_1.center(50))
        print(50*'#')
        print(f'Nome completo: {nome}')
        print(f'Data de nascimento: {dataN}')
        print(f'Local de nascimento: {local}')
        print(f'Morte: {dataM}')
        print(f'Idade ao falecer: {idade} anos.\n')
        print(f'{nome} nasceu há {idade_1} anos atrás.')
        print(f'{nome} nasceu em um ano {impar_par}.')
        print(f'{nome} morreu em um ano {impar_par1}.')
        print(f'Quando ele nasceu, faltavam {dias} dias para o ultimo dia do mês.')
        print(f'Quando ele morreu, faltavam {diasM} dias para o último dia do mês.')
        print(50*'#')
        print(50*'#')
#O do professor considera todos os meses como tendo 30 dias


#Exercicio 15(Ainda tentando, nao funciona nada.)


#txt = input('Digite um texto qualquer de 5 caracteres: ')
txt = 'aBCde'
mud = int(input('Digite "1" para retornar todas as letras em minusculas ou "2" para retornar todos em maiuscula : '))
txta = txt[0:len(txt)].replace("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxxyz")
for caractere2 in "abcdefghijklmnopqrstuvwxxyz":
    for caractere3 in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        txtB = txt.replace(caractere2, caractere3)
if mud == 1:
    print(txta)
elif mud == 2:
        print(txtB)
else:
        print('Digite apenas "1" ou "2".')