class Solution:
    def __init__(self):
        self.operatordict = {}
    
    def getOperators(self, length):
        if length in self.operatordict:
            return self.operatordict[length]
        ans = ["+", "-", "*"]
        for _ in range(length - 1):
            new = []
            for elem in ans:
                for i in range(3):
                    if i == 0:
                        new.append(elem + "+")
                    if i == 1:
                        new.append(elem + "-")
                    if i == 2:
                        new.append(elem + "*")
            ans = new
        self.operatordict[length] = ans
        return ans
        
    def evalExpression(self, expression):
        stack = [int(expression[0])]
        i = 1
        while i < len(expression):
            elem = expression[i]
            i += 1
            if elem == '+' or elem == '-':
                stack.append(elem)
            elif elem == "*":
                left = stack.pop()
                right = int(expression[i])
                i += 1
                stack.append(left * right)
            else:
                stack.append(int(elem))
        ans = stack.pop(0)
        while stack:
            elem = stack.pop(0)
            if elem == "+":
                ans += stack.pop(0)
            else:
                ans -= stack.pop(0)
        return ans
        
    def addOperators(self, num: str, target: int) -> List[str]:
        if not num:
            return []
        length = len(num)
        numsplit = ["0", "1"]
        for _ in range(length-2):
            new_numsplit = []
            for elem in numsplit:
                for i in range(2):
                    new_numsplit.append(elem + str(i))
            numsplit = new_numsplit
        numlists = []
        for split in numsplit:
            numlist = []
            start = 0
            for idx, elem in enumerate(split):
                if elem == "1":
                    numlist.append(num[start:idx+1])
                    start = idx + 1
            numlist.append(num[start:])
            flag = True
            for subnum in numlist:
                if len(subnum) > 1 and subnum[0] == "0":
                    flag = False
                    break
            if flag:
                numlists.append(numlist)
        ans = []
        for numlist in numlists:
            if len(numlist) == 1:
                if int(numlist[0]) == target:
                    ans.append(numlist[0])
            else:
                operators = self.getOperators(len(numlist) - 1)
                for operator in operators:
                    expression = ["" for _ in range(2 * len(numlist) - 1)]
                    for i in range(2 * len(numlist) - 1):
                        if i % 2 == 0:
                            expression[i] = numlist[i // 2]
                        else:
                            expression[i] = operator[i // 2]
                    if self.evalExpression(expression) == target:
                        ans.append("".join(expression))
        return ans
                    
