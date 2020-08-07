def helper(string):
  result = []
  def permutation(string, temp):
    result.append(temp[:])
    for i in range(len(string)):
      temp.append(string[i])
      permutation(string[i+1:] , temp)
      temp.pop()
  permutation(string, [])
  return result


print(helper("abc"))