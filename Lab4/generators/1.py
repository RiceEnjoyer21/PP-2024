def gen_sq(n):
    for i in range (n):
        yield i*i

n = int(input())
for sq in gen_sq(n):
    print(sq)
