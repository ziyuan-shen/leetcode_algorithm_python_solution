class Solution:
    def isAdditive(self, first, second, seq):
        while seq:
            third = first + second
            if str(third) == seq[:len(str(third))]:
                seq = seq[len(str(third)):]
                first = second
                second = third
            else:
                break
        return not seq
            
    def isAdditiveNumber(self, num: str) -> bool:
        if len(num) < 3:
            return False
        for i in range(len(num) // 2):
            for j in range(i+1, len(num) // 3 * 2 + 1):
                if not ((i > 0 and num[0] == '0') or ((j-i) > 1 and num[i+1] == '0') or (num[j+1:j+2] == '0' and (num[:i+1] != '0' or num[i+1:j+1] != '0'))):
                    first = int(num[:i+1])
                    second = int(num[i+1:j+1])
                    third = first + second
                    if str(third) == num[j+1:j+1+len(str(third))]:
                        if self.isAdditive(first, second, num[j+1:]):
                            return True
        return False