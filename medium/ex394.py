class Solution:
    def decodeString(self, s: str) -> str:
        if '[' not in s:
            return s
        else:
            nums = []
            bracket_pairs = []
            idx = 0
            num_flag = True
            while idx < len(s):
                if num_flag:
                    if not s[idx].isdigit():
                        nums.append(1)
                        bracket_pairs.append([idx, idx])
                        idx += 1
                    else:
                        num = ""
                        while s[idx] != '[':
                            num += s[idx]
                            idx += 1
                        nums.append(int(num))
                        num_flag = False
                else:
                    left = idx + 1
                    stack = ['[']
                    idx += 1
                    while True:
                        if s[idx] == '[':
                            stack.append('[')
                            idx += 1
                        elif s[idx] == ']':
                            if len(stack) == 1:
                                right = idx - 1
                                idx += 1
                                break
                            else:
                                stack.pop(-1)
                                idx += 1
                        else:
                            idx += 1
                    num_flag = True
                    bracket_pairs.append([left, right])
            ans = ""
            for i in range(len(nums)):
                ans += nums[i] * self.decodeString(s[bracket_pairs[i][0]:bracket_pairs[i][1]+1])
            return ans