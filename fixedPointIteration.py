import math

def g(x):
  return (math.cos(x))**2

def main():
  x_0=1.76929235
  tol=1e-8
  for i in range(10**6):
    x_1=g(x_0)
    if(abs(x_0-x_1)<tol):
      print("At x =",round(x_1,8),"\b, f(x) = 0")
      print("Found after",i,"iterations")
      break
    x_0=x_1 

if(__name__=="__main__"):
  main()
