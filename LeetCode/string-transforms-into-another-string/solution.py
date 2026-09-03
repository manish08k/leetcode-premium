class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if str1 == str2:
            return True
        
        alphabet_size = 26
        
        domain_to_range_map = {}
        range_to_domain_map = collections.defaultdict(list)
        
        for i in range(len(str1)):
            src = str1[i]
            dst = str2[i]
            
            if src not in domain_to_range_map:
                
                domain_to_range_map[src] = dst
                range_to_domain_map[dst].append(src)
            else:
                if domain_to_range_map[src] != dst:
                    return False
        
        if len(range_to_domain_map) == alphabet_size:
            return False
        
        return True