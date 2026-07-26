from tkinter import *

from assets.colors import *

from settings import *

class Renderer:

    def create(self):

        root=Tk()

        canvas=Canvas(

            root,

            width=BOARD_WIDTH*CELL_SIZE,

            height=BOARD_HEIGHT*CELL_SIZE,

            bg=BACKGROUND

        )

        canvas.pack()

        return root,canvas

    def draw(

        self,

        canvas,

        snake,

        food

    ):

        canvas.delete("all")

        for x,y in snake.body:

            canvas.create_rectangle(

                x*CELL_SIZE,

                y*CELL_SIZE,

                (x+1)*CELL_SIZE,

                (y+1)*CELL_SIZE,

                fill=SNAKE

            )

        x,y=food

        canvas.create_oval(

            x*CELL_SIZE,

            y*CELL_SIZE,

            (x+1)*CELL_SIZE,

            (y+1)*CELL_SIZE,

            fill=FOOD

        )
