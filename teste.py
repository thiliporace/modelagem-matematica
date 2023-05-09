# import numpy as np

# def matrix_power(a, power):
#     rows, columns = len(a), len(a[0])
#     result = np.zeros((rows, columns))
#     b = a
#     for step in range(1, power):
#       result = np.zeros((rows, columns)) # reset result to all zeroes matrix here
#       for i in range(0, rows):
#           for j in range(0, columns):
#               for m in range(0, rows):
#                   result[i][j] += a[i][m] * b[m][j]        
#       a = result.copy()
#     for val in result:
#         print(val)
#     return result

# def main():
#   a = [[0,1,0,0,0],
#       [0,0.2,0.8,0,0],
#       [0,0,0.4,0.6,0],
#       [0,0,0,0.8,0.2],
#       [0,0,0,0,1]];
#   print("Qual a potencia?")
#   pot = int(input("R:"))
#   matrix_power(a,pot)
    
  
  