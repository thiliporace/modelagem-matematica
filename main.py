# ATIVIDADE 10 -  TURMA 4D  - MODELAGEM MATEMÁTICA 2
# BRUNO CASTRO TOMAZ        - 32150989
# GABRIEL DE FRANÇA MARQUES - 42107490 
# RAFAELA PERROTTI ZYNGIER  - 42112125
# THIAGO LEANDRO LIPORACE   - 42128481 
# TOMÁS FIORELLI BARBOSA    - 42122791 

import copy

def multiplica_matrizes(A, B, mA, nA, nB, pB):
  if nA != nB:
    print ("Não é possível multiplicar estas matrizes")
    return  

  C = [[0 for _ in range(pB)] for _ in range(mA)]
 
  #realizando a multiplicação
  for i in range(mA):
    for j in range(pB): 
      for k in range(nA):
        C[i][j] += A[i][k] * B[k][j]    
  return C

def main(): 
  print("***MULTIPLICAÇÃO DE MATRIZES***\n")
  mA = 6
  nA = 6
  nB = 6
  pB = 6
  A = [[0,1,0,0,0,0],
      [0,0.2,0.8,0,0,0],
      [0,0,0.4,0.6,0,0],
      [0,0,0,0.6,0.4,0],
      [0,0,0,0,0.8,0.2],
      [0,0,0,0,0,1]]

  
  B = copy.deepcopy(A)

  print("P^1: ")
  for row in A:
    for num in row:
      print("{:.8f}".format(num), end=" ")
    print()

  array = [2,5,10,20]
  for i in range(2,21):
    C = multiplica_matrizes(A,B,mA,nA,nB,pB)
    if(i==5):
      quinta = copy.deepcopy(C)
    if i in array:
      print(f"\nP^{i}")
      print("Resultado da multiplicação dessas matrizes: ") 
      for row in C:
        for num in row:
          print("{:.8f}".format(num), end=" ")
        print()  # pula para a próxima linha
      B = copy.deepcopy(C)


  print("LETRA C:")
  
  print(quinta[0][2] * quinta[2][3] * quinta [3][4] *quinta [4][5])
  return 0 
main()