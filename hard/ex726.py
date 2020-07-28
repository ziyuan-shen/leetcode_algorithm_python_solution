from collections import defaultdict
class Solution:
    def countAtoms(self, formula):
        dic = defaultdict(int)
        idx = 0
        while idx < len(formula):
            if formula[idx] == "(":
                stack = ["("]
                sub_formula_end_idx = idx + 1
                while sub_formula_end_idx < len(formula) and stack:
                    if formula[sub_formula_end_idx] == "(":
                        stack.append("(")
                    elif formula[sub_formula_end_idx] == ")":
                        stack.pop()
                    sub_formula_end_idx += 1
                sub_formula_dic = self.countAtoms(formula[idx+1:sub_formula_end_idx-1])
                if sub_formula_end_idx < len(formula) and formula[sub_formula_end_idx].isdigit():
                    sub_formula_num_end_idx = sub_formula_end_idx + 1
                    while sub_formula_num_end_idx < len(formula) and formula[sub_formula_num_end_idx].isdigit():
                        sub_formula_num_end_idx += 1
                    sub_formula_num = int(formula[sub_formula_end_idx:sub_formula_num_end_idx])
                    for atom, count in sub_formula_dic.items():
                        dic[atom] += count * sub_formula_num
                    idx = sub_formula_num_end_idx
                else:
                    for atom, count in sub_formula_dic.items():
                        dic[atom] += count
                    idx = sub_formula_end_idx
            else:
                name_end_idx = idx + 1
                while name_end_idx < len(formula) and formula[name_end_idx].islower():
                    name_end_idx += 1
                if name_end_idx < len(formula):
                    if formula[name_end_idx].isdigit():
                        num_end_idx = name_end_idx + 1
                        while num_end_idx < len(formula) and formula[num_end_idx].isdigit():
                            num_end_idx += 1
                        dic[formula[idx:name_end_idx]] += int(formula[name_end_idx:num_end_idx])
                        idx = num_end_idx
                    else:
                        dic[formula[idx:name_end_idx]] += 1
                        idx = name_end_idx
                else:
                    dic[formula[idx:]] += 1
                    idx = name_end_idx
        return dic
        
    def countOfAtoms(self, formula: str) -> str:
        dic = self.countAtoms(formula)
        ans = ''
        for atom in sorted(dic.keys()):
            if dic[atom] == 1:
                ans += atom
            else:
                ans += atom
                ans += str(dic[atom])
        return ans