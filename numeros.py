'''
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000'''

r = input(str('Digite o número em algarismos romanos: ')).upper()

r = r + (r[-1])
num = valor = valor1 = 0

for l in r:
    if len(r) > 1:
        if r[0] == 'M':
            valor = 1000
        if r[1] == 'M':
            valor1 = 1000
        if r[0] == 'D':
            valor = 500
        if r[1] == 'D':
            valor1 = 500
        if r[0] == 'C':
            valor = 100
        if r[1] == 'C':
            valor1 = 100
        if r[0] == 'L':
            valor = 50
        if r[1] == 'L':
            valor1 = 50
        if r[0] == 'X':
            valor = 10
        if r[1] == 'X':
            valor1 = 10
        if r[0] == 'V':
            valor = 5
        if r[1] == 'V':
            valor1 = 5
        if r[0] == 'I':
            valor = 1
        if r[1] == 'I':
            valor1 = 1

        if (valor >= valor1):
            num += valor
            r = r[1:]
        if (valor1 > valor):
            num += (valor1 - valor)
            r = r[2:]

print(num)



