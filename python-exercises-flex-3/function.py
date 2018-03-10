"""

# ex 1 
def hello(phrase):
    print("hello",phrase)
    
hello("bob")


#ex2 
import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot

def f(x):
    return x+1

xs = list(range(-3, 4))
ys = []
for x in xs:
    ys.append(f(x))

pyplot.plot(xs, ys)
pyplot.savefig('ex2.png')



#ex3
import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot

def f(x):
    return x*x

xs = list(range(-100, 101))
ys = []
for x in xs:
    ys.append(f(x))

pyplot.plot(xs, ys)
pyplot.savefig('ex3.png')
"""

#ex4
import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot

def f(x):
    if x % 2 == 0:
        var =-1
    else:
        var = 0
        
    print(x,var)
    return var

xs = list(range(-5,6,1))
ys = []
for x in xs:
    ys.append(f(x))

pyplot.bar(xs, ys)
pyplot.savefig('ex4.png')