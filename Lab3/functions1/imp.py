grams = float(input())

def ounce(grams):
    ounces = 28.3495231 * grams
    print(ounces)

ounce(grams)

F = int(input())

def centigrade(C):
    C = (5 / 9) * (F - 32)
    return C

print(centigrade(F))

def bebriki(numheads, numlegs):
    for x in range(numheads + 1):
        y = numheads - x
        if 2*x + 4*y == numlegs:
            return x, y 
    return False

c, r = bebriki(35, 94)
print(bebriki(35, 94))



