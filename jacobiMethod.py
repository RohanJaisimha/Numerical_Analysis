import math
import matrixOperations

def printMatrix(matrix):
  for i in matrix:
    for j in i:
      print(j,"\t",end="")
    print()
  print("\n\n\n")

def jacobi(D,L,U,coefficient_vector):
  vector_x_0=matrixOperations.transpose([[0 for i in range(len(D))]])
  tol=10**-6
  D_inverse=[[0 for i in range(len(D))] for j in range(len(D))]
  for i in range(len(D)):
    D_inverse[i][i]=1/D[i][i]
  for i in range(10**6):
    vector_x_1=matrixOperations.multiply(D_inverse,matrixOperations.subtract(coefficient_vector,matrixOperations.multiply(matrixOperations.add(L,U),vector_x_0)))
    if(matrixOperations.isEqual(vector_x_1,vector_x_0,tol)):
      vector_x_0=[i[:] for i in vector_x_1]
      print("Required",i,"steps")
      break
    vector_x_0=[i[:] for i in vector_x_1]

  printMatrix(vector_x_0)
  error_vector=matrixOperations.subtract(vector_x_0,[[1] for i in range(len(D))])
  error_vector=[abs(i[0]) for i in error_vector]
  print("Backward Error =",sum(error_vector)/len(D))

def main():
  n=100
  vector_x_0=[0 for i in range(n)]
  D=[[0 for i in range(n)] for j in range(n)]
  for i in range(n):
    D[i][i]=3
  L=[[0 for i in range(n)] for j in range(n)]
  U=[[0 for i in range(n)] for j in range(n)]
  for i in range(1,n):
    L[i][i-1]=-1
  for i in range(1,n):
    U[i-1][i]=-1

  coefficient_vector=[1 for i in range(n)]
  coefficient_vector[0]=coefficient_vector[-1]=2
  coefficient_vector=matrixOperations.transpose([coefficient_vector])

  jacobi(D,L,U,coefficient_vector)

if(__name__=="__main__"):
  main()
