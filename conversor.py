# Grupo: Davi Bessa, Diego, Gabriel Suassuna
number = input('Digite um número de base 2, 10 ou 16:')
base = input('O número digitado foi de base 2, 10 ou 16:')
def dectobin (x):
    x = int(x)
    binary =[]
    while x>0:
        a = x%2
        binary.append (a)
        x = x//2
    binary = binary [::-1]
    numb = ''.join(map(str, binary))
    return numb
def dectohex (x):
    x = int(x)
    hexadecimal = []
    while x>0:       
        if x%16 == 15:
            hexadecimal.append ('F')
            x = x//16
        elif x%16 == 14:
            hexadecimal.append ('E')
            x = x//16
        elif x%16 == 13:
            hexadecimal.append ('D')
            x = x//16
        elif x%16 == 12:
            hexadecimal.append ('C')
            x = x//16
        elif x%16 == 11:
            hexadecimal.append ('B')
            x = x//16
        elif x%16 == 10:
            hexadecimal.append ('A')
            x = x//16
        else:
            a = x%16
            hexadecimal.append (a)
            x = x//16
    hexadecimal = hexadecimal[::-1]
    numbh = ''.join(map(str, hexadecimal))
    return numbh
def bintodec(x):
    y = len (x)
    decimal = []
    a = 0
    for binary in x:
        binary = int (binary)
        decimal.append (binary)
    for indice in range (0, y):
        a =  a + decimal [indice]*(2**(y - indice - 1))
    return a
def hextodec(x):
    y = len (x)
    a = 0
    decimal = []
    for hexadecimal in x:
        if hexadecimal == 'A':
            hexadecimal = 10
            decimal.append (hexadecimal)
        elif hexadecimal == 'B':
            hexadecimal = 11
            decimal.append (hexadecimal)
        elif hexadecimal == 'C':
            hexadecimal = 12
            decimal.append (hexadecimal)
        elif hexadecimal == 'D':
            hexadecimal = 13
            decimal.append (hexadecimal)
        elif hexadecimal == 'E':
            hexadecimal = 14
            decimal.append (hexadecimal)
        elif hexadecimal == 'F':
            hexadecimal = 15
            decimal.append (hexadecimal)
        else:
            hexadecimal = int(hexadecimal)
            decimal.append (hexadecimal)
    for indice in range (0, y):
        a =  a + decimal [indice]*(16**(y - indice - 1))
    return a
if base == '10':
    r1 = dectobin (number)
    print ('Base 2: ','(', r1,')')
    r2 = dectohex (number)
    print ('Base 16: ','(', r2, ')')
elif base =='2':
    r1 = bintodec (number)
    print ('Base 10: ','(', r1,')')
    r2 = dectohex (r1)
    print ('Base 16: ','(', r2, ')')
elif base =='16':
    r1 = hextodec (number)
    print ('Base 10: ','(', r1,')')
    r2 = dectobin (r1)
    print ('Base 2: ','(', r2,')')
else:
    print('Base não reconhecida, tente outra vez.')
