import matrixOperations

#solves system using Kramer's method
def solve(coefficients,y_values):
  coefficients=transpose(coefficients)
  answers=[]
  for i in range(len(coefficients)):
    answers.append((matrixOperations.determinant(coefficients[:i]+[y_values]+coefficients[i+1:])/matrixOperations.determinant(coefficients)))
  return answers

def transpose(matrix):
  return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def main():
  print(solve([[1,0,-7],[0,1,-3],[0,0,0]],[-5,1,1]))

if(__name__=="__main__"):
  main()
