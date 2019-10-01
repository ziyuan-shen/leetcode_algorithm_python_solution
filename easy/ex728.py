class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        return_value = []
        for i in range(left, right+1):
            test = True
            for j in range(len(str(i))):
                digit = int(str(i)[j])
                if digit==0 or i % digit != 0:
                    test=False
                    break
            if test == True:
                return_value.append(i)
        return return_value