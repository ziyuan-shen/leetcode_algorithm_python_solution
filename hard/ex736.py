class Solution:
    def compute(self, expression, args):
        if expression[0] != "(":
            if expression[0].isdigit() or expression[0] == "-":
                return int(expression)
            return args[expression]
        expression = expression[1:-1]
        if expression[:3] == "let":
            elems = expression[4:]
            elems_list = []
            idx = 0
            while idx < len(elems):
                start = idx
                if elems[idx] != "(":
                    while idx < len(elems) and elems[idx] != " ":
                        idx += 1
                    elems_list.append(elems[start:idx])
                    idx += 1
                else:
                    stack = ["("]
                    idx += 1
                    while stack:
                        if elems[idx] == "(":
                            stack.append("(")
                        elif elems[idx] == ")":
                            stack.pop()
                        idx += 1
                    elems_list.append(elems[start:idx])
                    idx += 1
            new_args = args.copy()
            for i in range(0, len(elems_list)-1, 2):
                if elems_list[i+1][0] != "(":
                    if elems_list[i+1][0].isdigit() or elems_list[i+1][0] == "-":
                        new_args[elems_list[i]] = int(elems_list[i+1])
                    else:
                        new_args[elems_list[i]] = new_args[elems_list[i+1]]
                else:
                    new_args[elems_list[i]] = self.compute(elems_list[i+1], new_args.copy())
            return self.compute(elems_list[-1], new_args.copy())
        else:
            if expression[:3] == "add":
                elems = expression[4:]
            else:
                elems = expression[5:]
            if elems[0] != "(":
                idx = 0
                while elems[idx] != " ":
                    idx += 1
                if elems[0].isdigit() or elems[0] == "-":
                    elem1 = int(elems[:idx])
                else:
                    elem1 = args[elems[:idx]]
                idx += 1
                if elems[idx] != "(":
                    if elems[idx].isdigit() or elems[idx] == "-":
                        elem2 = int(elems[idx:])
                    else:
                        elem2 = args[elems[idx:]]
                else:
                    elem2 = self.compute(elems[idx:], args.copy())
            else:
                stack = ["("]
                idx = 1
                while stack:
                    if elems[idx] == "(":
                        stack.append("(")
                    elif elems[idx] == ")":
                        stack.pop()
                    idx += 1
                elem1 = self.compute(elems[:idx], args.copy())
                idx += 1
                if elems[idx] != "(":
                    if elems[idx].isdigit() or elems[idx] == "-":
                        elem2 = int(elems[idx:])
                    else:
                        elem2 = args[elems[idx:]]
                else:
                    elem2 = self.compute(elems[idx:], args.copy())
            if expression[:3] == "add":
                return elem1 + elem2
            else:
                return elem1 * elem2
            
    def evaluate(self, expression: str) -> int:
        return self.compute(expression, {})