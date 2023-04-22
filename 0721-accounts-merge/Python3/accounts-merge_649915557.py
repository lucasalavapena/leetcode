class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = defaultdict(list)
        
        for account_name, *emails in accounts:
            graph[account_name].append(set(emails))
        
        changes = 1
        while changes:
            changes = 0
            for account_name in graph:
                N = len(graph[account_name])
                i, j = 0, 1
                while i < len(graph[account_name]) -1: 
                    if not graph[account_name][i].isdisjoint(graph[account_name][j]):
                        graph[account_name][i] = graph[account_name][i].union(graph[account_name][j])
                        graph[account_name].pop(j)
                        changes += 1
                    else:
                        j += 1

                    if j == len(graph[account_name]):
                        i += 1
                        j = i + 1
                
        
        res = []
        for account_name, different_emails in graph.items():
            for email in different_emails:
                res.append([account_name] + sorted(list(email)) )
                
        return res
        # print(list(graph))