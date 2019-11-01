class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        paragraph = paragraph.lower()
        dic = {}
        start_idx, end_idx = 0, 0
        max_word = ''
        max_count = 0
        while start_idx < len(paragraph):
            while start_idx < len(paragraph) and not paragraph[start_idx].isalpha():
                start_idx += 1
            end_idx = start_idx
            while end_idx < len(paragraph) and paragraph[end_idx].isalpha():
                end_idx += 1
            word = paragraph[start_idx:end_idx]
            if word not in banned:
                if word in dic:
                    dic[word] += 1
                else:
                    dic[word] = 1
                if dic[word] > max_count:
                    max_count = dic[word]
                    max_word = word
            start_idx = end_idx + 1
        return max_word
            