class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        s = s.split(" ")
        s = list(filter(lambda x: bool(x), s))
        return " ".join(s[::-1])