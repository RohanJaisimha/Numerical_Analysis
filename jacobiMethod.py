import math
import matrixOperations

def printMatrix(matrix):
  for i in matrix:
    for j in i:
      print(j,"\t",end="")
    print()
  print("\n\n\n")

def jacobi(D,L,U,solution_vector):
  vector_x_0=[[0] for i in range(len(solution_vector))]
  tol=10**-6
  D_inverse=[[0 for i in range(len(D))] for j in range(len(D))]
  for i in range(len(D)):
    D_inverse[i][i]=1/D[i][i]
  for i in range(10**6):
    vector_x_1=matrixOperations.multiply(D_inverse,matrixOperations.subtract(solution_vector,matrixOperations.multiply(matrixOperations.add(L,U),vector_x_0)))
    if(matrixOperations.isEqual(vector_x_1,vector_x_0,tol)):
      vector_x_0=[i[:] for i in vector_x_1]
      print("Required",i,"steps")
      break
    vector_x_0=[i[:] for i in vector_x_1]

  matrixOperations.printMatrix(vector_x_0)

#get the original matrix with just the diagonal elements
def getDiagonalMatrix(matrix):
  d=[i[:] for i in matrix]
  for i in range(len(d)):
    for j in range(len(d[i])):
      if(i!=j):
        d[i][j]=0
  return d

#get the original matrix with just the lower-triangular elements
def getLowerTriangularMatrix(matrix):
  l=[i[:] for i in matrix]
  for i in range(len(l)):
    for j in range(len(l[i])):
      if(i>=j):
        l[i][j]=0
  return l


#get the original matrix with just the lower-triangular elements
def getUpperTriangularMatrix(matrix):
  u=[i[:] for i in matrix]
  for i in range(len(u)):
    for j in range(len(u[i])):
      if(i<=j):
        u[i][j]=0
  return u

def main():
  matrix=[[1,1],[1,2]]
  solution_vector=[[1],[1]]
  jacobi(getDiagonalMatrix(matrix),getLowerTriangularMatrix(matrix),getUpperTriangularMatrix(matrix),solution_vector)

if(__name__=="__main__"):
  main()
