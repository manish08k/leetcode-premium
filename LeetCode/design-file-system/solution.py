class Node:
  def __init__(self, val: int = 0):
    self.val: int = val
    self.children: Dict[str, 'Node'] = {}

class FileSystem:
  def __init__(self):
    self.tree = Node()

  def createPath(self, path: str, value: int) -> bool:
    if not path or path == "/" or path[-1] == "/":
      return False

    parts = path.split("/")[1:]
    node = self.tree

    for part in parts[:-1]:
      if part not in node.children:
        return False
      node = node.children[part]

    last_part = parts[-1]
    if last_part in node.children:
      return False

    node.children[last_part] = Node(value)
    return True

  def get(self, path: str) -> int:
    node = self.tree
    for part in path.split("/")[1:]:
      if part not in node.children:
        return -1
      node = node.children[part]

    return node.val