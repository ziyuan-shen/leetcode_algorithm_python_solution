class Solution:
    def numberToWords_one(self, num):
        one_dic = {0: '', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}
        return one_dic[num]
    
    def numberToWords_two(self, num):
        ten_dic = {10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
        tenth_dic = {20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninety'}
        if num < 20:
            return ten_dic[num]
        else:
            return tenth_dic[num-num%10] + (' ' if num%10 != 0 else '') + self.numberToWords_one(num%10)
        
    def numberToWords_three(self, num):
        if num%100 < 10:
            return self.numberToWords_one(num//100) + ' Hundred' + (' ' if num%100 != 0 else '') + self.numberToWords_one(num%100)
        else:
            return self.numberToWords_one(num//100) + ' Hundred' + ' ' + self.numberToWords_two(num%100)
        
    def numberToWords_oneTothree(self, num):
        if num < 10:
            return self.numberToWords_one(num)
        elif num < 100:
            return self.numberToWords_two(num)
        else:
            return self.numberToWords_three(num)
        
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        billion = self.numberToWords_oneTothree(num//1000000000) + ' Billion' if num//1000000000 != 0 else ''
        million = self.numberToWords_oneTothree((num%1000000000)//1000000) + ' Million' if (num%1000000000)//1000000 != 0 else ''
        thousand = self.numberToWords_oneTothree((num%1000000)//1000) + ' Thousand' if (num%1000000)//1000 != 0 else ''
        one = self.numberToWords_oneTothree(num%1000)
        ans = billion
        if ans == '' or million == '':
            ans += million
        else:
            ans += (' ' + million)
        if ans == '' or thousand == '':
            ans += thousand
        else:
            ans += (' ' + thousand)
        if ans == '' or one == '':
            ans += one
        else:
            ans += (' ' + one)
        return ans