class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def full_adder(cin, a, b):
            sum_result = (cin + a + b) % 2
            cout = (cin + a + b) // 2
            return sum_result, cout
        length = max(len(a), len(b))
        a = a.zfill(length)
        b = b.zfill(length)
        cout = 0
        result = ''
        for i in range(length-1, -1, -1):
            sum_result, cout = full_adder(int(a[i]), int(b[i]), cout)
            result = str(sum_result) + result
        if cout == 1:
            result = '1' + result
        return result