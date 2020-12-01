# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea(object):
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point(object):
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution(object):
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        x1, y1 = topRight.x, topRight.y
        x2, y2 = bottomLeft.x, bottomLeft.y
        if x1 == x2 and y1 == y2:
            return 1 if sea.hasShips(topRight, bottomLeft) else 0
        ans = 0
        if x1 != x2 and y1 != y2:
            subrecs = [[((x1+x2) //2, (y1+y2)//2), (x2, y2)], [((x1+x2)//2, y1), (x2, (y1+y2) // 2 + 1)], [(x1, (y1+y2) // 2), ((x1+x2) // 2 + 1, y2)], [(x1, y1), ((x1+x2) // 2 + 1, (y1+y2) // 2 + 1)]]
        elif x1 == x2:
            subrecs = [[(x1, (y1+y2) // 2), (x1, y2)], [(x1, y1), (x1, (y1+y2) // 2 + 1)]]
        elif y1 == y2:
            subrecs = [[((x1+x2) // 2, y1), (x2, y2)], [(x1, y1), ((x1+x2) // 2 + 1, y1)]]
        for rec in subrecs:
            tr = Point(rec[0][0], rec[0][1])
            bl = Point(rec[1][0], rec[1][1])
            if rec[0] == rec[1]:
                if sea.hasShips(tr, bl):
                    ans += 1
            else:
                if sea.hasShips(tr, bl):
                    ans += self.countShips(sea, tr, bl)
        return ans
            