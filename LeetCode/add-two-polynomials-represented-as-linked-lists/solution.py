class Solution:
    def addPoly(self, poly1, poly2):
        power = {}
        
        def map_polynode_to_dict(polynode):
            while polynode:
                if polynode.coefficient != 0:
                    power[polynode.power] = power.get(polynode.power, 0) + polynode.coefficient
                polynode = polynode.next
                
        map_polynode_to_dict(poly1)
        map_polynode_to_dict(poly2)
            
        newVals = sorted([k for k in power.keys() if power[k] != 0], reverse=True)
        
        def fill_polynomial():
            if len(newVals) == 0:
                return None
            toThePower = newVals.pop(0)
            return PolyNode(x=power[toThePower], y=toThePower, next=fill_polynomial())
        
        return fill_polynomial()