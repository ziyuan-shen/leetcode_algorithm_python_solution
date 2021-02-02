class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = {'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'}
        s = list(s)
        vowelchar = []
        for idx, char in enumerate(s):
            if char in vowel:
                vowelchar.append(char)
                s[idx] = None
        for i in range(len(s)):
            if not s[i]:
                s[i] = vowelchar[-1]
                vowelchar.pop()
        return "".join(s)