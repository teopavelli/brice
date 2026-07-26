import random

def random_cell(

    width,

    height

):

    return (

        random.randint(

            0,

            width-1

        ),

        random.randint(

            0,

            height-1

        )

    )
