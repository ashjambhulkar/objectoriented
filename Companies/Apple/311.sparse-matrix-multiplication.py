
def helper(a, b):
  # x, y, z = len(a), len(a[0]), len(b)
  # result = [[0 for _ in range(z)] for _ in range(x)]
  # for i in range(x):
  #   for j in range(y):
  #     if a[i][j] != 0:
  #       for k in range(z):
  #         if b[j][k] != 0:
  #           result[i][k] += a[i][j] * b[j][k]
  # return result
  
  x, y, z = len(a), len(a[0]), len(b)
  result = [[0 for _ in range(z)] for _ in range(x)]
  sample = []
  for i in range(x):
    temp = []
    for j in range(y):
      if A[i][j] != 0:
        temp.append((j, A[i][j]))
    sample.append(temp)
  for i in range(len(sample)):
    for j, p in sample[i]:
      for k in range(z):
        if B[j][k] != 0:
          result[i][k] += p * B[j][k]
  return result


A = [
    [1, 0, 0],
    [-1, 0, 3]
]

B = [
    [7, 0, 0],
    [0, 0, 0],
    [0, 0, 1]
]
print(helper(A, B))
