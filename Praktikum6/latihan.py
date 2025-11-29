import math

a = lambda x: x**2
print(a(19))

b = lambda x, y : math.sqrt(x**2 + y**2)
print(b(3, 4))

c = lambda *args : sum(args)/len(args)
print(c(20,30,40))

d = lambda s : "".join(set(s))
print(d("HelloWorld!"))