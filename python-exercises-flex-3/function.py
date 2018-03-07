"""

# ex 1 
def hello(phrase):
    print("hello",phrase)
    
hello("bob")

"""
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

plot.plot(xs, ys)
plot.show()
