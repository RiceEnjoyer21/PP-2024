x = input()

def reversu(x):
    a = ' '.join(x.split(' ')[::-1])
    return a

print(reversu(x))
