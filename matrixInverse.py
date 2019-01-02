import determinant

def printMatrix(matrix):
  for i in matrix:
    for j in i:
      print(round(j,5),"\t",end="")
    print()
  print("\n\n\n")

def addMultipleOfOneRowToAnother(factor,row_to_be_multiplied,row_to_be_added_to,matrix):
  for i in range(len(matrix[0])):
    matrix[row_to_be_added_to][i]=matrix[row_to_be_added_to][i]+factor*matrix[row_to_be_multiplied][i]

def divideARowByANumber(factor,row_to_be_divided,matrix):
  for i in range(len(matrix[0])):
    matrix[row_to_be_divided][i]=matrix[row_to_be_divided][i]/factor

#row reduces augmented matrix [matrix|I_n] to 
#reduced echelon form to get [I_n|A^-1]
def invert(matrix):
  if(determinant.determinant(matrix)==0):
    print("No scene fam")
    return

  u=[matrix[i]+[0]*i+[1]+[0]*(len(matrix)-1-i) for i in range(len(matrix))]

  for i in range(len(matrix)):
    for j in range(len(matrix)):
      if(j==i):
        continue
      if(u[i][i]==0):
        for k in range(1,len(matrix)-i):
          if(u[i+k][i]==0):
            continue
          u[i],u[i+k]=u[i+k],u[i]
          break
      addMultipleOfOneRowToAnother(-u[j][i]/u[i][i],i,j,u) 


  for i in range(len(matrix)):
    divideARowByANumber(u[i][i],i,u)

  printMatrix([i[len(matrix):] for i in u])

def main():
  matrix=[[0,2,3],[0,5,6],[7,8,10]]
  invert(matrix)

if(__name__=="__main__"):
  main()
