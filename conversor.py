number = input('Digite um número de base 2, 10 ou 16:').upper ()
base = input('O número digitado foi de base 2, 10 ou 16:')
convert = int(input("Para qual base deseja converter: "))
dicionary = {'A':10,"B":11,"C":12,"D":13,"E":14,"F":15,10:'A',11:'B',12:'C',13:"D",14:'E',15:'F'}
def dectoall (x,y):
    x = int(x)
    binary =[]
    while x>0:
        a = x%y
        if a in dicionary:
            a = dicionary [a]
            binary.append (a)
        else:
            binary.append (a)
        x = x//y
    binary = binary [::-1]
    b = ''.join(map(str, binary))
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
    r1 = dectoall (number, convert)
    print ('Base', convert, ':', '(', r1,')')
elif base =='2':
    r1 = bintodec (number)
    r2 = dectoall (r1, convert)
    if convert == 10:
        print ('Base 10: ','(', r1,')')
    elif convert == 16:
        print ('Base 16: ','(', r2, ')')
    else:
        print ("Essa conversão não é possível")
elif base =='16':
    r1 = hextodec (number)
    r2 = dectoall (r1, convert)
    if convert == 10:
        print ('Base 10: ','(', r1,')')
    elif convert == 16:
        print ('Base 2: ','(', r2, ')')
    else:
        print ("Essa conversão não é possível")
else:
    print ('Base não reconhecida, tente outra vez.')
