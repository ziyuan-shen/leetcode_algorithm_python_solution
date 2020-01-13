class Solution:
    def intToRoman(self, num: int) -> str:
        num, one = num // 10, num % 10
        num, ten = num // 10, num % 10
        num, hundred = num // 10, num % 10
        thousand = num % 10
        onedic = {0: "", 1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX"}
        tendic = {0: "", 1: "X", 2: "XX", 3: "XXX", 4: "XL", 5: "L", 6: "LX", 7: "LXX", 8: "LXXX", 9: "XC"}
        hundreddic = {0: "", 1: "C", 2: "CC", 3: "CCC", 4: "CD", 5: "D", 6: "DC", 7: "DCC", 8: "DCCC", 9: "CM"}
        thousanddic = {0: "", 1: "M", 2: "MM", 3: "MMM"}
        return thousanddic[thousand] + hundreddic[hundred] + tendic[ten] + onedic[one]