import systemSolverKramer
import sys
import determinant

#accepts points from console
def getPoints():  
  points=[]  
  while(True):
    print("Enter a point (end with a '.')")
    t=input()
    if(t=='.'):
      break
    points.append([float(i) for i in t.split()])

  if(len(set([i[0] for i in points]))!=len(points)):
    print("We cannot graphically model this distribution")
    sys.exit(0)

  return points

#prints polynomial
def printPolynomial(coefficients):
  print("\n\ny = ",end="")
  for i in range(len(coefficients)):
    print("("+str(round(coefficients[i],5))+" x^"+str(len(coefficients)-i-1)+")",end=" + " if len(coefficients)-i-1!=0 else "")
  print("\n\n")

def main():
  print()
  points=getPoints()
  coefficients=[]
  y_values=[]
  for i in range(len(points)):
    coefficients.append([points[i][0]**j for j in range(len(points)-1,-1,-1)])
    y_values.append(points[i][1])
  answers=systemSolverKramer.solve(coefficients,y_values)
  printPolynomial(answers)

if(__name__=="__main__"):
  main()
