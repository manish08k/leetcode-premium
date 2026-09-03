class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.lst = []
        self.ptr = -1
        def dfs(cur):
            if cur == None: return
            dfs(cur.left)
            self.lst.append(cur)
            dfs(cur.right)
        dfs(root)

    def hasNext(self) -> bool:
        return self.ptr+1 < len(self.lst)

    def next(self) -> int:
        self.ptr+=1
        return self.lst[self.ptr].val

    def hasPrev(self) -> bool:
        return self.ptr-1 >= 0

    def prev(self) -> int:
        self.ptr-=1
        return self.lst[self.ptr].val