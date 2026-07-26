class Snake:

    def __init__(self):

        self.body=[

            (5,5),

            (4,5),

            (3,5)

        ]

        self.direction=(1,0)

    def move(self):

        x,y=self.body[0]

        dx,dy=self.direction

        self.body.insert(

            0,

            (

                x+dx,

                y+dy

            )

        )

        self.body.pop()
