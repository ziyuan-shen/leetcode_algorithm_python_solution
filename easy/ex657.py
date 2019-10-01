class Solution:
    def judgeCircle(self, moves: str) -> bool:
        mov_dic = {'R': 0, 'L': 0, 'U': 0, 'D': 0}
        for i in range(len(moves)):
            mov_dic[moves[i]] += 1
        if (mov_dic['R'] == mov_dic['L']) and (mov_dic['U'] == mov_dic['D']):
            return True
        else:
            return False
