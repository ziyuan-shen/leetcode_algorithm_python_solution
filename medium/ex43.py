class Solution:
    def add(self, nums):
        ans = []
        cout = 0
        while nums[-1]:
            sumnum = 0
            for num in nums:
                if num:
                    sumnum += num.pop(0)
            sumnum += cout
            ans.append(sumnum % 10)
            cout = sumnum // 10
        if cout != 0:
            ans.append(cout)
        return ans
        
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        if num1 > num2:
            uppernum = num1
            lowernum = num2
        else:
            uppernum = num2
            lowernum = num1
        uppernum = [int(char) for char in uppernum][::-1]
        lowernum = [int(char) for char in lowernum][::-1]
        addnums = []
        for i in range(len(lowernum)):
            cout = 0
            addnums.append([0] * i)
            mul1 = lowernum[i]
            for j in range(len(uppernum)):
                mul2 = uppernum[j]
                product = mul1 * mul2 + cout
                addnums[-1].append(product % 10)
                cout = product // 10
            if cout != 0:
                addnums[-1].append(cout)
        return "".join([str(num) for num in self.add(addnums)])[::-1]