class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        parent = {}
        for region_list in regions:
            u = region_list[0]
            for i in range(1, len(region_list)):
                v = region_list[i]
                parent[v] = u
            
        def get_path(region):
            path = []
            while region is not None:
                path.append(region)
                region = parent.get(region)
            path.reverse()
            return path
        
        result = None
        for a, b in zip(get_path(region1), get_path(region2)):
            if a != b:
                break
            result = a
        return result