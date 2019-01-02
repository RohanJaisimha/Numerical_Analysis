import math

def f(x):
  return math.sin(x)

def find_zero(lo,hi,tol):
  mid_point=None
  if(f(lo)*f(hi)<0):
    while((hi-lo)/2>=tol):
      mid_point=(lo+hi)/2
      if(abs(f(mid_point))<tol):
        break
      elif(f(lo)*f(mid_point)<0):
        hi=mid_point
      else:
        lo=mid_point
  return round(mid_point,-int(math.log(tol)/math.log(10)))

def main():
  lo=0
  hi=10**6
  tol=10**-6
  print("At",find_zero(lo,hi,tol),"\b, f(x) = 0")

if(__name__=="__main__"):
  main()
