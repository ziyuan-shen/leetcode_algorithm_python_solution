class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if s1 == "" and s2 == "" and s3 == "":
            return True
        if len(s1) + len(s2) != len(s3):
            return False
        if len(s1) > 0 and len(s2) > 0 and s1[0] == s2[0]:
            return s3[0] == s1[0] and (self.isInterleave(s1[1:], s2, s3[1:]) or self.isInterleave(s1, s2[1:], s3[1:]))
        elif len(s1) > 0 and s1[0] == s3[0]:
            return self.isInterleave(s1[1:], s2, s3[1:])
        elif len(s2) > 0 and s2[0] == s3[0]:
            return self.isInterleave(s1, s2[1:], s3[1:])
        else:
            return False