class Collision:

    def wall(

        self,

        head,

        width,

        height

    ):

        x,y=head

        return (

            x<0

            or

            y<0

            or

            x>=width

            or

            y>=height

        )

    def self_hit(

        self,

        snake

    ):

        return snake.body[0] in snake.body[1:]
