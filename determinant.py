def printMatrix(matrix):
  for i in matrix:
    for j in i:
      print(j,end="\t")
    print()
  print("\n\n\n")

def addMultipleOfOneRowToAnother(factor,row_to_be_multiplied,row_to_be_added_to,matrix):
  for i in range(len(matrix)):
    matrix[row_to_be_added_to][i]=matrix[row_to_be_added_to][i]+factor*matrix[row_to_be_multiplied][i]

#gets determinant of a matrix by converting to
#Upper Triangular Matrix and multiplying diagonal elements
def determinant(matrix):
  num_swapsies=0
  u=[i[:] for i in matrix]
  for i in range(len(matrix)):
    for j in range(i+1,len(matrix)):
      if(u[i][i]==0):
        for k in range(1,len(matrix)-i):
          if(u[i+k][i]==0):
            continue
          u[i],u[i+k]=u[i+k],u[i]
          num_swapsies+=1
          break
      addMultipleOfOneRowToAnother(-u[j][i]/u[i][i],i,j,u)  

  prod=1
  for i in range(len(matrix)):
    prod=prod*u[i][i]

  return prod*(-1)**num_swapsies

def main():
  matrix=[[0,0,0,2],[0,-2,3,-7],[0,0,1,5],[3,5,-8,4]]
  print(determinant(matrix))

if(__name__=="__main__"):
  main()
