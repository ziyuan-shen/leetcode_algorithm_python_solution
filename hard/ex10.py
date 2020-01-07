class Solution:
    def match(self, s, p, sp, pp):
        while sp < self.strlen and pp < self.patlen:
            if pp == self.patlen - 1:
                if p[pp] == ".":
                    return sp == self.strlen - 1
                else:
                    return sp == self.strlen - 1 and p[pp] == s[sp]
            elif p[pp+1] == "*":
                return self.matchstar(s, p, sp, pp, True) or self.matchstar(s, p, sp, pp, False)
            else:
                if s[sp] != p[pp]:
                    return False
                sp += 1
                pp += 1
        return sp == self.strlen and pp == self.patlen
        
    def matchstar(self, s, p, sp, pp, matchzero):
        if matchzero:
            pp += 2
            return self.match(s, p, sp, pp)
        else:
            if p[pp] != ".":
                if s[sp] != p[pp]:
                    return False
                else:
                    while sp < self.strlen and s[sp] == p[pp]:
                        sp += 1
                    pp += 2
                    return self.match(s, p, sp, pp)
            else:
                letter = s[sp]
        
    def isMatch(self, s: str, p: str) -> bool:
        sp = 0
        pp = 0
        self.strlen = len(s)
        self.patlen = len(p)
        if self.strlen == 0 or self.patlen == 0:
            return self.strlen == 0 and self.patlen == 0
        return self.match(s, p, 0, 0)