# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:  
    def getLevel(self,nestedList):
        if nestedList == []:
            return 0
        level = 1
        for nestedint in nestedList:
            if nestedint.isInteger():
                continue
            else:
                sublevel = self.getLevel(nestedint.getList())
                if sublevel + 1 > level:
                    level = sublevel + 1
        return level
    
    def getSum(self, nestedList, level):
        ans = 0
        for nestedint in nestedList:
            if nestedint.isInteger():
                ans += nestedint.getInteger() * level
            else:
                ans += self.getSum(nestedint.getList(), level - 1)
        return ans
    
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        level = self.getLevel(nestedList)
        return self.getSum(nestedList, level)
        