# Given two strings containing backspaces(identified by the character ‘  "#" ’), check if the two strings are equal.
# Input: str1="xy#z", str2="xzz#"
# Output: true
# Explanation: After applying backspaces the strings become "xz" and "xz" respectively.
# Input: str1="xp#", str2="xyz##"
# Output: true
# Explanation: After applying backspaces the strings become "x" and "x" respectively.
# In "xyz##", the first '#' removes the character 'z' and the second '#' removes the character 'y'.


def helper(left, right):
  start = []
  end = []
  for x in list(left):
    if x == "#":
      start.pop()
    else:
      start.append(x)
  for x in list(right):
    if x == "#":
      end.pop()
    else:
      end.append(x)
  return start == end


left = "xyz#"
right = "xzz#"
print(helper(left, right))
