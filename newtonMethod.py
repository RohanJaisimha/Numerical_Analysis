import math

#approximates the first derivative of the function g at x 
def firstDerivative(g,x):
  return (g(x)-g(x-10**-4))/10**-4

def f(x):
  return x**3-2*x-2

def main():
  x_0=-0.5
  for i in range(10**6):
    x_1=x_0-f(x_0)/firstDerivative(f,x_0)
    if(abs(x_0-x_1)<1e-8):
      print("At x =",round(x_1,8),"\b, f(x) = 0")
      break
    x_0=x_1

if(__name__=="__main__"):
  main()
