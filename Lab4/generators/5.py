def down(n):
    for i in range(n, -1, -1):
        yield i


n = int(input())

for d in down(n):
    print(d)