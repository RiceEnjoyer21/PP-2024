def gen_sq(n, m):
    for i in range (n, m):
        yield i*i

n = int(input())
m = int(input())
for sq in gen_sq(n, m):
    print(sq)
