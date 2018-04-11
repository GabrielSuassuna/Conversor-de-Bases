number = input('Digite um número que tenha base 2 até 32:').upper ()
base = int(input('Qual a base do número digitado:'))
convert = int(input("Para qual base deseja converter o número digitado (entre 2 a 32): "))
dicionary = {"A":10,"B":11,"C":12,"D":13,"E":14,"F":15,"G":16,"H":17,"J":18,"K":19,"M":20,"N":21,
             "P":22,"Q":23,"R":24,"S":25,"T":26,"V":27,"W":28,"X":29,"Y":30,"Z":31,10:'A',11:'B',12:'C',
             13:"D",14:'E',15:'F',16:'G',17:'H',18:'J',19:"K",20:'M',21:'N',22:'P',23:'Q',24:'R',25:"S",26:'T',
             27:'V',28:'W',29:'X',30:"Y",31:"Z"}
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
