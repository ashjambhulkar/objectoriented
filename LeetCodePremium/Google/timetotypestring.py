import collections


def helper(keyboard, text):
  if not text:
    return 0

  sample = collections.defaultdict(int)

  for i in range(len(keyboard)):
    sample[keyboard[i]] = i 

  count = sample[text[0]]

  for i in range(1, len(text)):
    count += abs(sample[text[i]] - sample[text[i-1]])

  return count

  

keyboard = "abcdefghijklmnopqrstuvwxy"
text = "cba"

print(helper(keyboard, text))
