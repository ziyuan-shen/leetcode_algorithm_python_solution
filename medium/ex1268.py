class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        ans = [[]]
        for product in products:
            if product[0] == searchWord[0]:
                ans[0].append(product)
        ans[0].sort()
        for i, letter in enumerate(searchWord[1:]):
            l = []
            for product in ans[-1]:
                if len(product) > (i + 1) and product[i+1] == letter:
                    l.append(product)
            ans.append(l)
        for l in ans:
            while len(l) > 3:
                l.pop()
        return ans