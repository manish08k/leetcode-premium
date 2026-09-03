class Solution:
    def lastMarkedNodes(self, E: List[List[int]]) -> List[int]:
        G, n = defaultdict(list), len(E) + 1
        for a, b in E:
            G[a].append(b)
            G[b].append(a)

        # find one
        D, seen, dq = [0] * n, set([0]), deque([(0, 0)])
        while dq:
            node, dist = dq.popleft()
            for nxt in G[node]:
                if nxt in seen: continue
                seen.add(nxt)
                dq.append((nxt, dist + 1))
                D[nxt] = dist + 1
        one = max(range(n), key=lambda i: D[i])

        # find two + distance from one
        D1 = [inf] * n
        seen, dq, D1[one] = set([one]), deque([(one, 0)]), 0
        while dq:
            node, dist = dq.popleft()
            for nxt in G[node]:
                if nxt in seen: continue
                seen.add(nxt)
                dq.append((nxt, dist + 1))
                D1[nxt] = dist + 1
        two = max(range(n), key=lambda i: D1[i])

        # distance from two
        D2 = [inf] * n
        seen, dq, D2[two] = set([two]), deque([(two, 0)]), 0
        while dq:
            node, dist = dq.popleft()
            for nxt in G[node]:
                if nxt in seen: continue
                seen.add(nxt)
                dq.append((nxt, dist + 1))
                D2[nxt] = dist + 1

        return [two if D1[i] <= D2[i] else one for i in range(n)]