class Solution:
    def count(self, prev, rem):
        if (prev, rem) in self.mem:
            return self.mem[(prev, rem)]
        if rem == 0:
            self.mem[(prev, rem)] = 1
            return 1
        else:
            ans = 0
            for char in self.mapping[prev]:
                ans += self.count(char, rem - 1)
            ans %= (10 ** 9 + 7)
            self.mem[(prev, rem)] = ans
            return ans
        
    def countVowelPermutation(self, n: int) -> int:
        self.mem = dict()
        self.mapping = {'a': ['e'], 'e': ['a', 'i'], 'i': ['a', 'e', 'o', 'u'], 'o': ['i', 'u'], 'u': ['a']}
        ans = 0
        for prev in ['a', 'e', 'i', 'o', 'u']:
            ans += self.count(prev, n - 1)
        return ans % (10 ** 9 + 7)