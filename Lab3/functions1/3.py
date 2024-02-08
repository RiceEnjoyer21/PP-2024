def bebriki(numheads, numlegs):
    for x in range(numheads + 1):
        y = numheads - x
        if 2*x + 4*y == numlegs:
            return x, y 
    return False

c, r = bebriki(35, 94)
print(bebriki(35, 94))
