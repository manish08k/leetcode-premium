class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        d, visited = {num:i for i, num in enumerate(org)}, set()    
        for nums in seqs:
            prev_num = prev_idx = -1                                
            for num in nums:
                if num not in d: return False                      
                cur_idx = d[num]
                if prev_idx + 1 == cur_idx and num not in visited:  
                    visited.add(num)
                elif prev_idx >= cur_idx: return False             
                prev_num, prev_idx = num, cur_idx                   
        return len(visited) == len(org)                           