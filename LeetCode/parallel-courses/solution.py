class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        in_degree, next_courses = [0 for _ in range(n + 1)], [[] for _ in range(n + 1)]
        for prev, next in relations:
            in_degree[next] += 1
            next_courses[prev].append(next)
        
        dq = collections.deque([])
        for i in range(1, n + 1):
            if in_degree[i] == 0: dq.append(i)
        
        num_semesters = 0
        while dq:
            l = len(dq)
            for _ in range(l):
                course = dq.popleft()
                n -= 1
                for c in next_courses[course]:
                    in_degree[c] -= 1
                    if in_degree[c] == 0: dq.append(c)
            num_semesters += 1

            if n == 0: return num_semesters
        
        return -1