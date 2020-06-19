class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.width = width
        self.height = height
        self.foods = food
        if self.foods:
            self.food = self.foods.pop(0)
        else:
            self.food = []
        self.snake = [[0, 0]]
        self.score = 0

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        """
        head = self.snake[0]
        if direction == "U":
            new_head = [head[0] - 1, head[1]]
        elif direction == "D":
            new_head = [head[0] + 1, head[1]]
        elif direction == "L":
            new_head = [head[0], head[1] - 1]
        else:
            new_head = [head[0], head[1] + 1]
        if new_head == self.food:
            self.snake.insert(0, new_head)
            if self.foods:
                self.food = self.foods.pop(0)
            else:
                self.food = []
            self.score += 1
        else:
            self.snake.pop()
            if new_head in self.snake:
                return -1
            elif new_head[0] >= 0 and new_head[0] < self.height and new_head[1] >= 0 and new_head[1] < self.width:
                self.snake.insert(0, new_head)
            else:
                return -1
        return self.score


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)