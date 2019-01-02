import matrixOperations

def addMultipleOfOneRowToAnother(factor,row_to_be_multiplied,row_to_be_added_to,matrix):
  for i in range(len(matrix)):
    matrix[row_to_be_added_to][i]=matrix[row_to_be_added_to][i]+factor*matrix[row_to_be_multiplied][i]

def decomposeIntoUAndL(matrix):
  l=[[0 for i in range(len(matrix))] for j in range(len(matrix))]
  for i in range(len(matrix)):
    l[i][i]=1
  u=[i[:] for i in matrix]
  for i in range(len(matrix)):
    for j in range(i+1,len(matrix)):
      l[j][i]=u[j][i]/u[i][i]
      addMultipleOfOneRowToAnother(-u[j][i]/u[i][i],i,j,u)  
  print("Lower Triangular Matrix:")
  matrixOperations.printMatrix(l)
  print("\n\n\nUpper Triangular Matrix:")
  matrixOperations.printMatrix(u)
  print("\n\n\nOriginal Matrix:")
  matrixOperations.printMatrix(matrix)

def main():
  matrix=[[2,7],[5,6]]
  decomposeIntoUAndL(matrix)

if(__name__=="__main__"):
  main()
