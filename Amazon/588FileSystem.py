import collections

#created trie data structure to maintain the directory structure
class Trie:
  def __init__(self):
    self.childern = collections.defaultdict(Trie)


class Solution:
  def __init__(self):
    self.file = Trie()
    #This is the key:value pair in which the value will be string and key will be the filepath
    self.details = collections.defaultdict(str)

  def ls(self, path):
    if path in self.details:
      return path.split("/")[-1:]

    cur = self.file
    for x in path.split("/"):
      if x in cur:
        cur = cur[x]
      elif x:
        return []

    return sorted(cur.keys())

  def mkdir(self, path):
    cur = self.file
    for x in path.split("/"):
      if x:
        cur = cur[x]
    

  def add_content_to_file(self, filepath, content):
    self.mkdir(filepath)
    self.details[filepath] += content
  

  def read_content_from_file(self, filepath):
    return self.details[filepath]

  