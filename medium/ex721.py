from collections import defaultdict
class Solution:
    def dfs(self, email, neighbordic, visited, email_list):
        for neighbor in neighbordic[email]:
            if not visited[neighbor]:
                visited[neighbor] = True
                email_list.append(neighbor)
                self.dfs(neighbor, neighbordic, visited, email_list)
    
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graphdic = defaultdict(lambda: defaultdict(set))
        for account in accounts:
            n = len(account)
            if n == 2 and account[1] not in graphdic[account[0]]:
                graphdic[account[0]][account[1]] = set()
            else:
                for i in range(1, n):
                    for email in account[1:i] + account[i+1:]:
                        graphdic[account[0]][account[i]].add(email)
        merged_accounts = defaultdict(list)
        for name in graphdic:
            neighbordic = graphdic[name]
            visited = {email: False for email in neighbordic}
            for email in neighbordic:
                if not visited[email]:
                    merged_accounts[name].append([email])
                    visited[email] = True
                    self.dfs(email, neighbordic, visited, merged_accounts[name][-1])
        ans = []
        for name in merged_accounts:
            for li in merged_accounts[name]:
                li.sort()
                ans.append([name] + li)
        return ans
        