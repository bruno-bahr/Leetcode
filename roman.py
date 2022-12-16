'''
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000'''

num = int(input('Digite o número que deseja transformar para romanos? '))
num_orig = num
roman = ''

if (num >= 1000):
    m = num//1000
    num -= (m*1000)
    roman += 'M'*m
if (1000 > num > 899):
    d = num//900
    num -= 900
    roman += 'CM'
if (499 < num < 900):
    d = num//500
    num -= 500
    roman += 'D'
if (99 < num < 400):
    c = num//100
    num -= (100*c)
    roman += 'C'*c
if (399 < num < 499):
    cd = num//400
    num -= 400
    roman += 'CD'
if (89 < num < 99):
    xc = num//9
    num -= 90
    roman += 'XC'
if (49 < num < 90):
    l = num//50
    num -= 50
    roman += 'L'
if (39 < num < 49):
    xl = num//40
    num -= 40
    roman += 'XL'
if (9 < num < 40):
    x = num //10
    num -= (x*10)
    roman += 'X'*x
if (num == 9):
    roman += 'IX'
if (4 < num < 9):
    v = num//5
    num -= 5
    roman += 'V'
if (num == 4):
    roman += 'IV'
if (num < 4):
    roman += "I"*num

print(f'O número {num_orig} em romanos é {roman}')