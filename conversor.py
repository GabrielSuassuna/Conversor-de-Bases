number = input('Digite um número que tenha base 2 até 32:').upper ()
base = int(input('Qual a base do número digitado:'))
convert = int(input("Para qual base deseja converter o número digitado (entre 2 a 32): "))
dicionary = {"A":10,"B":11,"C":12,"D":13,"E":14,"F":15,"G":16,"H":17,"J":18,"K":19,"M":20,"N":21,
             "P":22,"Q":23,"R":24,"S":25,"T":26,"V":27,"W":28,"X":29,"Y":30,"Z":31,10:'A',11:'B',12:'C',
             13:"D",14:'E',15:'F',16:'G',17:'H',18:'J',19:"K",20:'M',21:'N',22:'P',23:'Q',24:'R',25:"S",26:'T',
             27:'V',28:'W',29:'X',30:"Y",31:"Z"}


def dec_to_all (decimalNum, conversionBase):
    decimalNum = int(decimalNum)
    binary =[]

    while decimalNum>0:
        digit = decimalNum%conversionBase
        if digit in dicionary:
            digit= dicionary[digit]
            binary.append(digit)
        else:
            binary.append(digit)
        decimalNum = decimalNum//conversionBase

    binary = binary [::-1]
    b = ''.join(map(str, binary))
    return b


def other_to_dec(entryNum, entnumBase):
    y = len (entryNum)
    decimal = []
    b = 0
    for bases in entryNum:
        if bases in dicionary:
            bases = dicionary [bases]
            decimal.append (bases)
        else:
            bases = int(bases)
            decimal.append (bases)
    for indice in range (0, y):
        b =  b + decimal [indice]*(entnumBase**(y - indice - 1))
    return b
if base == 10:
    r1 = dec_to_all(number, convert)
    print ('Base', convert, ':', '(', r1,')')
else:
    r1 = other_to_dec (number, base)
    r2 = dec_to_all (r1, convert)
    if convert == 10:
        print ('Base', convert, ': ','(', r1, ')')
    else:
        print ('Base', convert, ': ', '(', r2, ')')
