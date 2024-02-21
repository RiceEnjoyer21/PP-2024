import datetime

x = datetime.datetime.now()
y = datetime.datetime.now() - datetime.timedelta(days = 1)
z = datetime.datetime.now() + datetime.timedelta(days = 1)

a = x.strftime("%A")
b = y.strftime("%A")
c = z.strftime("%A")

print(y)
print(x)
print(z)

print(b)
print(a)
print(c)

