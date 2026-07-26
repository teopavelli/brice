from ui.renderer import Renderer

from ui.score import Score

from engine.game import Game

game = Game()

renderer = Renderer()

root, canvas = renderer.create()

renderer.draw(

    canvas,

    game.snake,

    game.food

)

Score().show(

    game.score

)

root.mainloop()
