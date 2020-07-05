# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    degree_to_move = {0: (0, 1), 90: (1, 0), 180: (0, -1), 270: (-1, 0)}
    def dfs(self, visited, node, robot, degree):
        visited.add(node)
        robot.clean()
        for _ in range(4):
            robot.turnLeft()
            degree = (degree + 90) % 360
            if robot.move():
                next_node = (node[0] + self.degree_to_move[degree][0], node[1] + self.degree_to_move[degree][1])
                if next_node not in visited:
                    self.dfs(visited, next_node, robot, degree)
                robot.turnLeft()
                robot.turnLeft()
                robot.move()
                robot.turnLeft()
                robot.turnLeft()
        
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        self.dfs(set(), (0, 0), robot, 0)