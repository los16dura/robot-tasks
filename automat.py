N = 35

def cell_calculate(left, current, right, s):
    k = ''.join(map(str, (left, current, right)))
    return int(s[k])

def calculate_field(field, substitution):
    """field -- список из N ноликов или единичек"""
    N = len(field)
    new_field = 0*[N]
    for i in range(1, N-1):
        new_field[i] = cell_calculate(field[i-1], field[i], field[i+1], substitution)
    field[:] = new_field

def generate_field():
    field = [0]*N
    x = N//2
    field[x] = 1
    return field

def print_field(field):
    for cell in field:
        print('★' if cell else ' ' , end = '')
    print()

def getCodeDict(num):
    binNum = '{0:08b}'.format(num)
    binNum = binNum[::-1]
    code = {}

    for i in range(8):




def modelling():
    """ цикл моделирования клеточного автомата """
    f = open("cellAutomat.txt", "r")
    codeV = int(f.readline())
    field = list(map(int, f.readline()))
    time = int(f.readline())
    f.close()
    code = getCodeDict(codeV)
    print_field(field)
    for t in range(time):
        calculate_field(field, code)
        print_field(field)

if __name__ == '__main__':
    modelling()

