import determinant

def printMatrix(matrix):
  if(matrix==None):
    print(None)
    return
  for i in matrix:
    for j in i:
      print(round(j,5),"\t",end="")
    print()
  print("\n\n\n")

def multiply(m1,m2):
  if(len(m1[0])!=len(m2)):
    return None
  answer=[[0 for j in range(len(m2[0]))] for i in range(len(m1))]
  
  for i in range(len(m1)):
    for j in range(len(m2[0])):
      for k in range(len(m1[0])):
        answer[i][j]=answer[i][j]+m1[i][k]*m2[k][j]

  return answer

def add(m1,m2):
  if(len(m1[0])!=len(m2[0]) or len(m1)!=len(m2)):
    return None
  answer=[[0 for j in range(len(m1[0]))] for i in range(len(m1))]
  
  for i in range(len(m1)):
    for j in range(len(m1[0])):
      answer[i][j]=m1[i][j]+m2[i][j]

  return answer

def subtract(m1,m2):
  if(len(m1[0])!=len(m2[0]) or len(m1)!=len(m2)):
    return None
  answer=[[0 for j in range(len(m1[0]))] for i in range(len(m1))]
  
  for i in range(len(m1)):
    for j in range(len(m1[0])):
      answer[i][j]=m1[i][j]-m2[i][j]

  return answer

def isEqual(m1,m2,tol=10**-8):
  if(len(m1)!=len(m2) or len(m1[0])!=len(m2[0])):
    return False

  for i in range(len(m1)):
    for j in range(len(m1[0])):
      if(abs(m1[i][j]-m2[i][j])>tol):
        return False

  return True

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
    return None

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
 
  return [i[len(matrix):] for i in u]

def transpose(matrix):
  return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]

def getDimensions(matrix):
  return (len(matrix),len(matrix[0]))
    
def main():
  m1=[[1,2],[3,4]]
  printMatrix(invert(m1))

if(__name__=="__main__"):
  main()
