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
  A=[[81,9,1],[100,10,1],[121,11,1],[144,12,1]]
  b=[[100],[200],[350],[50]]
  x_bar=leastSquares(A,b)
  matrixOperations.printMatrix(x_bar)
  print(rootMeanSquareError(b,A,x_bar))  

if(__name__=="__main__"):
  main()


#We have
#(1960, 3039585530)
#(1970, 3707475887)
#(1990, 5281653820)
#(2000, 6079603571)

