class Solution:
    def toBinary(self, num):
        ans = bin(num)[2:]
        if len(ans) <= 8:
            return ans.rjust(8, "0")
        else:
            return ans[-8:]
        
    def valid(self, data):
        if not data:
            return True
        if data[0][0] == "0":
            data.pop(0)
            return self.valid(data)
        elif data[0][:3] == "110":
            if len(data) >= 2 and data[1][:2] == "10":
                data.pop(0)
                data.pop(0)
                return self.valid(data)
            else:
                return False
        elif data[0][:4] == "1110":
            if len(data) >= 3 and data[1][:2] == "10" and data[2][:2] == "10":
                for _ in range(3):
                    data.pop(0)
                return self.valid(data)
            else:
                return False
        elif data[0][:5] == "11110":
            if len(data) >= 4 and data[1][:2] == "10" and data[2][:2] == "10" and data[3][:2] == "10":
                for _ in range(4):
                    data.pop(0)
                return self.valid(data)
            else:
                return False
        return False
    
    def validUtf8(self, data: List[int]) -> bool:
        data = [self.toBinary(num) for num in data]
        return self.valid(data)