#https://projecteuler.net/problem=5

def evenlyDivisible(seq):
    num = 0
    i = 20
    while(True):
        #print('i : ' + str(i))
        bools = []
        i += 2
        for x in seq:
            if i % x != 0:
                break
            elif i % x == 0:
                bools.append(True)
        if len(bools) == len(seq):
            num = i
            break
    return num

print( evenlyDivisible(range(1,21)) )
