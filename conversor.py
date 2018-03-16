number = input('Digite um número de base 2, 10 ou 16:')
base = input('O número digitado foi de base 2, 10 ou 16:')
dicionary = {'A':10,"B":11,"C":12,"D":13,"E":14,"F":15,10:'A',11:'B',12:'C',13:"D",14:'E',15:'F'}
def dectobin (x):
    x = int(x)
    binary =[]
    while x>0:
        a = x%2
        binary.append (a)
        x = x//2
    binary = binary [::-1]
    b = ''.join(map(str, binary))
    return b
def dectohex (x):
    x = int(x)
    hexadecimal = []
    while x>0:
        a = x%16
        if a in dicionary:
            a = dicionary [a]
            hexadecimal.append (a)
        else:
            hexadecimal.append (a)
        x = x//16
    hexadecimal = hexadecimal[::-1]
    b = ''.join(map(str, hexadecimal))
    return b
def bintodec(x):
    y = len (x)
    decimal = []
    b = 0
    for binary in x:
        binary = int (binary)
        decimal.append (binary)
    for indice in range (0, y):
        b =  b + decimal [indice]*(2**(y - indice - 1))
    return b
def hextodec(x):
    y = len (x)
    b = 0
    decimal = []
    for a in x:
        if a in dicionary:
            a = dicionary [a]
            decimal.append (a)
        else:
            a = int(a)
            decimal.append (a)
    for indice in range (0, y):
        b =  b + decimal [indice]*(16**(y - indice - 1))
    return b
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
