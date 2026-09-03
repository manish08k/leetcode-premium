class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.snake = [[0,0]]
        self.N_ROWS = height
        self.N_COLS = width
        self.food_list = food
        self.food = self.food_list[0]
        self.food_counter = 0
        self.score = 0
        self.direction_row = {"L": 0, "R": 0, "U": -1, "D": 1}
        self.direction_col = {"L": -1, "R": 1, "U":0, "D":0}
    def out_of_bounds(self, row, col):

        if row >= self.N_ROWS or row < 0 or col >= self.N_COLS or col < 0:
            return True

        for elem in self.snake[0:-1]:
            if elem == [row, col]:
                return True
        return False

    def got_food(self, row, col):
        if self.food == [row,col]:
            self.food_counter +=1
            self.score +=1
            if self.food_counter >= len(self.food_list):
                self.food = None
            else:
                self.food = self.food_list[self.food_counter]
            return True
        return False
        

    def move(self, direction: str) -> int:

        snake_head = self.snake[0]

        
        row, col = snake_head
        new_row, new_col = row + self.direction_row[direction], col+self.direction_col[direction]

        if self.out_of_bounds(new_row, new_col):
            return -1

        if self.got_food(new_row, new_col):
            self.snake = [[new_row, new_col]] + self.snake
            return self.score
        
        self.snake = [[new_row, new_col]] + self.snake
        self.snake.pop(-1)
        return self.score
