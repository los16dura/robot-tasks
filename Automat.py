binNum = '{0:08b}'.format(int(input()))
print(binNum, type(binNum))

CJIOBAPb = {}
cnucok_4uceJI = ['111', '110', '101', '100', '011', '010', '001', '000']
for i in range(8):
    CJIOBAPb[cnucok_4uceJI[i]] = binNum[i]
print(CJIOBAPb)
JIEHTA = input()
time = int(input())
right = JIEHTA[-1]
left = JIEHTA[1]
current = JIEHTA[0]
#print(left, current, right)

def generate_field():
    field = [0]*N
    x = N//2
    field[x] = 1
    return field


def field(left, current, right):
    for i in range()