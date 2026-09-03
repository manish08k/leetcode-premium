class Solution:
    def minimumLines(self, points: List[List[int]]) -> int:
        n, line_points = len(points), collections.defaultdict(set)               
        for i in range(n):                                                        # calculate `line_points`
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                if x1 == x2:                                                      # handle divided by zero case
                    a, b = x1, sys.maxsize                                        # for `b`, you can use any number not in range of [-100, 100]
                else:
                    a = (y2 - y1) / (x2 - x1)
                    b = y1 - a * x1
                line_points[(a, b)].add((x1, y1))
                line_points[(a, b)].add((x2, y2))
        lines = [line for line, points in line_points.items() if len(points) > 2] 
        ans, m = math.ceil(n / 2), len(lines)                                    
        for i in range(1, 2**m):                                                 
            j, cnt = 0, bin(i).count('1')                                        
            cur_points = set()                                                  
            while i > 0:
                if i % 2:
                    cur_points |= line_points[lines[m-1-j]]                      
                i >>= 1                        
                j += 1
            ans = min(ans, cnt + math.ceil( (n-len(cur_points))/2 ))             
        return ans