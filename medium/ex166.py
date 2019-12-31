class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        sign = "-" if numerator * denominator < 0 else ""
        numerator = abs(numerator)
        denominator = abs(denominator)
        if numerator == 0:
            return "0"
        integer = 0
        remainder = numerator
        if numerator >= denominator:
            integer, remainder = numerator // denominator, numerator % denominator
            if remainder == 0:
                return sign + str(integer)
        fraction = ""
        nume_list = [remainder]
        while True:
            quotient, remainder = remainder * 10 // denominator, remainder * 10 % denominator
            fraction += str(quotient)
            if remainder == 0:
                return sign + str(integer) + "." + fraction
            if remainder in nume_list:
                break
            else:
                nume_list.append(remainder)
        idx = nume_list.index(remainder)
        return sign + str(integer) + "." + fraction[:idx] + "(" + fraction[idx:] + ")"