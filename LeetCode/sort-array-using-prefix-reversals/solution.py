class Solution:
    def sortArray(self, A: List[int], pre: List[int]) -> int:
        # BFS

        seen = set()
        N = len(A)
        dq = deque()

        dq.append(A)
        seen.add(",".join(str(x) for x in A))
        
        cnt = 0
        while len(dq) > 0:
            size = len(dq)

            for i in range(size):
                cur = dq.popleft()

                flag = True
                for k in range(len(cur)):
                    if k != cur[k]:
                        flag = False
                        break

                if flag:
                    return cnt

                for p in pre:
                    nxt = cur[:p][::-1] + cur[p:]
                    key = ",".join(str(x) for x in nxt)
                    if key not in seen:
                        seen.add(key)
                        dq.append(nxt)
                    
            cnt += 1

        return -1
        
        