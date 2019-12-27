class Solution:
    def insertDic(self, dic, letter, left_letter = None, right_letter = None):
        dics = []
        if left_letter == None or left_letter not in dic:
            left_boundary = 0
        else:
            left_boundary = dic.index(left_letter) + 1
        if right_letter == None or right_letter not in dic:
            right_boundary = len(dic) + 1
        else:
            right_boundary = dic.index(right_letter) + 1
        for i in range(left_boundary, right_boundary):
            dic = dic.copy()
            dic.insert(i, letter)
            dics.append(dic)
        return dics

    def formDictionary(self, words, dic):
        for i in range(len(words)):
            for j in range(len(words[i])):
                if len(words[i]) == 1:
                    if words[i] in dic:
                        continue
                    else:
                        dics = self.insertDic(dic, words[i])
                        for new_dic in dics:
                            final_dic = self.formDictionary(words, new_dic)
                            if final_dic != None:
                                return final_dic
                        #return None
                else:
                    if j == 0:
                        if words[i][j] in dic:
                            if words[i][j+1] != words[i][j] and words[i][j+1] in dic and dic.index(words[i][j]) > dic.index(words[i][j+1]):
                                return None
                            continue
                        else:
                            right_boundary = words[i][j+1] if words[i][j+1] != words[i][j] else None
                            dics = self.insertDic(dic, words[i][j], right_letter = right_boundary)
                            for new_dic in dics:
                                final_dic = self.formDictionary(words, new_dic)
                                if final_dic != None:
                                    return final_dic
                            #return None
                    elif j == len(words[i]) - 1:
                        if words[i][j] in dic:
                            if words[i][j-1] != words[i][j] and words[i][j-1] in dic and dic.index(words[i][j]) < dic.index(words[i][j-1]):
                                return None
                            continue
                        else:
                            left_boundary = words[i][j-1] if words[i][j-1] != words[i][j] else None
                            dics = self.insertDic(dic, words[i][j], left_letter = left_boundary)
                            for new_dic in dics:
                                final_dic = self.formDictionary(words, new_dic)
                                if final_dic != None:
                                    return final_dic
                            #return None
                    else:
                        if words[i][j] in dic:
                            if words[i][j+1] != words[i][j] and words[i][j+1] in dic and dic.index(words[i][j]) > dic.index(words[i][j+1]):
                                return None
                            if words[i][j-1] != words[i][j] and words[i][j-1] in dic and dic.index(words[i][j]) < dic.index(words[i][j-1]):
                                return None
                            continue
                        else:
                            right_boundary = words[i][j+1] if words[i][j+1] != words[i][j] else None
                            left_boundary = words[i][j-1] if words[i][j-1] != words[i][j] else None
                            dics = self.insertDic(dic, words[i][j], left_letter = left_boundary, right_letter = right_boundary)
                            for new_dic in dics:
                                final_dic = self.formDictionary(words, new_dic)
                                if final_dic != None:
                                    return final_dic
                            #return None
        for i in range(len(words)):
            for j in range(len(words[i])):
                if words[i][j] not in dic:
                    return None
        return dic

    def alienOrder(self, words):
        if words == []:
            return ""
        new_word = ""
        for word in words:
            new_word += word[0]
        words.append(new_word)
        ans = self.formDictionary(words, [])
        if ans==None:
            return ""
        return "".join(ans)

s = Solution()
print(s.alienOrder(["wrt","wrf","er","ett","rftt"]))
#print(s.alienOrder(["x", "z", "x"]))