from engine.snake import Snake
from engine.food import Food

class Game:

    def __init__(self):

        self.snake = Snake()

        self.food = Food().spawn(

            25,

            20

        )

        self.score = 0
