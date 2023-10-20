import numpy as np
from sympy import * 
from matplotlib import pyplot
n = int(input("How many points do you have sir "))
xcords = np.zeros(n)
ycords = np.zeros(n)
x = symbols('x')
def constructLangrangian(xcords: np.array, ycords: np.array, k, n):
    expression = sympify(1)
    x = sympify('x')
    for i in range(n):
        if(i==k):
            continue
        else:
            expression = expression*(x-sympify(xcords[i]))/(xcords[k]-xcords[i])
  #  print(expression)
    return expression

def buildPolynomial(xcords:np.array, ycords:np.array, n):
    Polynomial = 0
    for i in range(n):
        Polynomial = Polynomial+ycords[i]*constructLangrangian(xcords, ycords, i , n)
    
    return Polynomial
def collectdata(xcords, ycords, n):
   
    for i in range(n):
        xcords[i] =float(input(f"Give x cordinate of point {i} "))
        ycords[i] = float(input(f"Give y cordinate of point {i} "))
    return xcords, ycords
#constructLangrangian(xcords, ycords, 2, n)
collectdata( xcords, ycords, n)
output = buildPolynomial(xcords, ycords, n)
print(output)
approx = input("what value do you want to approx")
out = sympify(output).subs({x: approx})
print(out)
output_array = np.linspace(0.1,10.0,num = 100)
output1 = []
output2 = []
for i in np.linspace(0.1,10.0,num = 100):
    output1.append(sympify(output).subs({x: i}))
    output2.append(sympify(x**-1).subs({x:i}))
pyplot.plot( output_array, output1, color = 'b', alpha = 0.3)
pyplot.plot( output_array, output2, color = 'r', alpha = 0.5)
pyplot.show()
