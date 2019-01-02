import matrixOperations

def addMultipleOfOneRowToAnother(factor,row_to_be_multiplied,row_to_be_added_to,matrix):
  for i in range(len(matrix)):
    matrix[row_to_be_added_to][i]=matrix[row_to_be_added_to][i]+factor*matrix[row_to_be_multiplied][i]

def gaussianEliminate(matrix):
  u=[i[:] for i in matrix]
  for i in range(len(matrix)):
    for j in range(i+1,len(matrix)):
      if(u[i][i]==0):
        for k in range(1,len(matrix)-i):
          if(u[i+k][i]==0):
            continue
          u[i],u[i+k]=u[i+k],u[i]
          break     
      addMultipleOfOneRowToAnother(-u[j][i]/u[i][i],i,j,u)  
  return u

def main():
  matrix=[[-3,-5,36,10],[-1,0,7,5],[1,1,-10,-4]]
  matrixOperations.printMatrix(gaussianEliminate(matrix))

if(__name__=="__main__"):
  main()
