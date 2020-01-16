class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        if n < 4 or n > 12:
            return []
        ans = []
        for a in range(n-3):
            for b in range(a+1, n-2):
                for c in range(b+1, n-1):
                    num1 = s[:a+1]
                    num2 = s[a+1:b+1]
                    num3 = s[b+1:c+1]
                    num4 = s[c+1:]
                    nums = [num1, num2, num3, num4]
                    nums = list(filter(lambda x: int(x) in range(256) and not (len(x) > 1 and x[0] == "0"), nums))
                    if len(nums) == 4:
                        ans.append(".".join(nums))
        return ans