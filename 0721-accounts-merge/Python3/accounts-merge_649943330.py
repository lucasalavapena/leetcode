class DSU:
    def __init__(self, N):
        self.p = list(range(N)) 
        self.components = N
        
    def union(self, a, b):
        x = self.find(a)
        y = self.find(b)
        
        if x != y:
            self.components -= 1
            self.p[y] = x 
            
    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        N = len(accounts)
        
        dsu = DSU(N)
        email_to_account = {}
        
        for i, (account_name, *emails) in enumerate(accounts):
            for email in emails:
                if email in email_to_account:
                    other_idx = email_to_account[email]
                    dsu.union(other_idx, i)
                    email_to_account[email] = i
                else:
                    email_to_account[email] = i
        
        res = [[] for i in range(N)]
        visited = set()
        
        for email, value in email_to_account.items():
            group_id = dsu.find(value)
            if group_id in visited:
                res[group_id].append(email)
            else:
                visited.add(group_id)
                account_name = accounts[group_id][0]
                res[group_id].append(account_name)
                res[group_id].append(email)

        for i in range(len(res)):
            res[i][1:] = sorted(res[i][1:])
        return [r for r in res if r]
            
    
        