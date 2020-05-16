import random

class Node:
    def __init__(self, key, level):
        self.key = key
        self.forward = [None] * (level+1)

class Skiplist:

    def __init__(self):
        self.max_lvl = 4
        self.p = 0.5
        
        self.header = self.createNode(self.max_lvl - 1, -1)
        # current level of skip list
        self.level = 0
        
    def createNode(self, lvl, key):
        n = Node(key, lvl)
        return n
    
    def randomLevel(self):
        lvl = 0
        while random.random() < self.p and lvl < self.max_lvl - 1:
            lvl += 1
        return lvl

    def search(self, target: int) -> bool:
        ''' 
        start from highest level of skip list 
        move the current reference forward while key  
        is greater than key of node next to current 
        Otherwise inserted current in update and  
        move one level down and continue search 
        '''
        current = self.header
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < target:
                current = current.forward[i]
        current = current.forward[0]
        return current and current.key == target

    def add(self, num: int) -> None:
        update = [None] * self.max_lvl
        current = self.header
        
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < num:
                current = current.forward[i]
            update[i] = current
        current = current.forward[0]
        rlevel = self.randomLevel()
        if rlevel > self.level:
            for i in range(self.level+1, rlevel+1):
                update[i] = self.header
            self.level = rlevel
        n = self.createNode(rlevel, num)
        for i in range(rlevel+1):
            n.forward[i] = update[i].forward[i]
            update[i].forward[i] = n

    def erase(self, num: int) -> bool:
        update = [None] * self.max_lvl
        current = self.header
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < num:
                current = current.forward[i]
            update[i] = current
        current = current.forward[0]
        if current != None and current.key == num:
            ''' 
            start from lowest level and rearrange references  
            just like we do in singly linked list 
            to remove target node 
            '''
            for i in range(self.level+1):
                ''' 
                If at level i, next node is not target  
                node, break the loop, no need to move  
                further level 
                '''
                if update[i].forward[i] != current:
                    break
                update[i].forward[i] = current.forward[i]
            # Remove levels having no elements
            while self.level > 0 and self.header.forward[self.level] == None:
                self.level -= 1
            return True
        else:
            return False

# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)