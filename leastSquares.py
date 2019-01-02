import matrixOperations

def rootMeanSquareError(answers,coefficients,x_bar):
  error_vector=matrixOperations.subtract(answers,matrixOperations.multiply(coefficients,x_bar))
  s=0
  for i in error_vector:
    s=s+i[0]**2

  return (s/len(error_vector))**0.5
  
def leastSquares(A,b):
  A_transpose=matrixOperations.transpose(A)
  return matrixOperations.multiply(matrixOperations.multiply(matrixOperations.invert(matrixOperations.multiply(A_transpose,A)),A_transpose),b)

def main():
  #we have x+y=3,x+2y=4,2x+3y=8
  A=[[1,1],[1,2],[2,3]]
  b=[[3],[4],[8]]
  x_bar=leastSquares(A,b)
  matrixOperations.printMatrix(x_bar)
  print("Root mean square error: ",rootMeanSquareError(b,A,x_bar))  

if(__name__=="__main__"):
  main()


