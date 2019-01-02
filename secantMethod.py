import math

def f(x):
  return x**3-2*x-2

def main():
  x_0=1
  x_1=2
  for i in range(2):
    x_2=x_1-(f(x_1)*(x_1-x_0))/(f(x_1)-f(x_0))
    if(abs(x_2-x_1)<1e-8):
      print("At x =",round(x_3,8),"\b, f(x) = 0")
      break
    print(x_2)
    x_0=x_1
    x_1=x_2

if(__name__=="__main__"):
  main()
