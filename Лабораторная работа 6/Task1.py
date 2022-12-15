'''''
def func (x):
    def infunc (x):
        return x
    return(infunc(x) + x)
print(func(6))
'''''
f1 = lambda n: n
f2 = lambda n : n + f1(n)
print(f2(f1(2)))