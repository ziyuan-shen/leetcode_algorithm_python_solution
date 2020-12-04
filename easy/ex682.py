class Solution:
    def calPoints(self, ops: List[str]) -> int:
        records = []
        for op in ops:
            if op.isdigit() or (op[0] == "-" and op[1:].isdigit()):
                records.append(int(op))
            elif op == "+":
                records.append(records[-1] + records[-2])
            elif op == "D":
                records.append(records[-1] * 2)
            elif op == "C":
                records.pop()
        return sum(records)
                