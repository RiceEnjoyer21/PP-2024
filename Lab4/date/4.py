import datetime

a = int(input())
b = int(input())
c = int(input())
a1 = int(input())
a2 = int(input())
a3 = int(input())

x = datetime.datetime(a, b, c, a1, a2, a3)

d = int(input())
e = int(input())
f = int(input())
d1 = int(input())
d2 = int(input())
d3 = int(input())

y = datetime.datetime(d, e, f, d1, d2, d3)

z = abs(x - y).total_seconds()

print("Difference in seconds:", z)
