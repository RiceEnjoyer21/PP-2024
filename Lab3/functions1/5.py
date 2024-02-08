from itertools import permutations

def permutes(a):

    plist = permutations(a)
    for perm in list(plist):
        print(''.join(perm))

a = str(input())

print(permutes(a))
