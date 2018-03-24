number = input('Digite um número de base 2 até 16:').upper ()
base = int(input('O número digitado foi de base 2 até 16:'))
convert = int(input("Para qual base deseja converter de base 2 até 16: "))
dicionary = {'A':10,"B":11,"C":12,"D":13,"E":14,"F":15,10:'A',11:'B',12:'C',13:"D",14:'E',15:'F'}
def dectoall (x, y):
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
def othertodec(x, c):
    y = len (x)
    decimal = []
    b = 0
    for bases in x:
        if bases in dicionary:
            bases = dicionary [bases]
            decimal.append (bases)
        else:
            bases = int(bases)
            decimal.append (bases)
    for indice in range (0, y):
        b =  b + decimal [indice]*(c**(y - indice - 1))
    return b
if base == 10:
    r1 = dectoall (number, convert)
    print ('Base', convert, ':', '(', r1,')')
else:
    r1 = othertodec (number, base)
    r2 = dectoall (r1, convert)
    if convert == 10:
        print ('Base', convert, ': ','(', r1, ')')
    else:
        print ('Base', convert, ': ', '(', r2, ')')
