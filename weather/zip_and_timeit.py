import timeit

def f0(aRange):
    x = []
    y = []
    for i in aRange:
        x.append(i*2)
        y.append(i*3)
    return x,y

def f1(aRange):
    x = [2*i for i in aRange]
    y = [3*i for i in aRange]
    return x,y

def f2(aRange):
    x, y = zip(*[(2*i, 3*i) for i in aRange])
    return x,y

def f3(aRange):
    x, y = zip(*((2*i, 3*i) for i in aRange))
    return x,y

def f4(aRange):
    x = []
    y = []
    for i in aRange:
        x.append(i*2)
        y.append(i*3)
    return x,y

print("f0: %f" %timeit.Timer("f0(range(100))", "from __main__ import f0").timeit(100000))
print("f1: %f" %timeit.Timer("f1(range(100))", "from __main__ import f1").timeit(100000))
print("f2: %f" %timeit.Timer("f2(range(100))", "from __main__ import f2").timeit(100000))
print("f3: %f" %timeit.Timer("f3(range(100))", "from __main__ import f3").timeit(100000))
print("f4: %f" %timeit.Timer("f4(range(100))", "from __main__ import f4").timeit(100000))