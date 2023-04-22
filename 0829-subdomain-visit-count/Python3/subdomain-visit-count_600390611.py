class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
    
        values = {}
        
        for c in cpdomains:
            num, rest = c.split(" ")
            d1, d2, *d3 = rest.split(".")
            num = int(num)
            if d3:
                d3 = d3[0]
                values[d3] = values.get(d3, 0) + num
                values[f"{d1}.{d2}.{d3}"] = values.get(f"{d1}.{d2}.{d3}", 0) + num
                values[f"{d2}.{d3}"] = values.get(f"{d2}.{d3}", 0) + num
            else:
                values[d2] = values.get(d2, 0) + num
                values[f"{d1}.{d2}"] = values.get(f"{d1}.{d2}", 0) + num
            
        res = []
        for k, v in values.items():
            res.append(f"{v} {k}")
        return res

                
            
    