class Solution:
    def moveSubTree(self, root: 'Node', p: 'Node', q: 'Node') -> 'Node':
        def search(r,x,path):
            if not r: return False
            path.append(r)
            if r == x: return True
            for child in r.children:
                checkChild = search(child, x, path)
                if checkChild:
                    return True
            path.pop()
            return False
        
        pathp, pathq = [], []
        _,_ = search(root, p, pathp), search(root, q, pathq)
        
        if p in pathq:
            if len(pathp) > 1:
                i = pathp[-2].children.index(p)
            pathq[-2].children.remove(q)
            q.children.append(p)
            if len(pathp)>1:
                pathp[-2].children[i] = q
                return root
            else:
                return q
        else:
            if pathp[-2] == q:
                return root
            pathp[-2].children.remove(p)
            q.children.append(p)
            return root