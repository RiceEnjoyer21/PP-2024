def gen_sq(n):
    for i in range (1, n+1):
        if i % 2 == 0:
            yield i

n = int(input())
for sq in gen_sq(n):
    print(sq)
