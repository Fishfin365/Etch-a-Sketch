from turtle import Turtle, mainloop


class Etch(Turtle):
    def __init__(self):
        super().__init__()  # calls the init of Turtle; making this object a Turtle object
        self.screen = self.getscreen()
        self.color('blue')
        self.shape('turtle')
        self.pensize(2)
        self.distance = 5
        self.turn = 10
        self.isFilling = False
        self.screen.onkey(self.fwd, "Up")
        self.screen.onkey(self.bkwd, "Down")
        self.screen.onkey(self.leftTurn, "Left")
        self.screen.onkey(self.rightTurn, "Right")
        self.screen.onkey(self.colorRed, "r")
        self.screen.onkey(self.colorBlue, "b")
        self.screen.onkey(self._up, "u")
        self.screen.onkey(self._down, "d")
        self.screen.onkey(self.colorFill, "f")
        self.speed("fastest")
        self.screen.listen()
        self.main()

    def colorFill(self):
        self.isFilling = not self.isFilling

        if self.isFilling:
            self.begin_fill()
        else:
            self.end_fill()

    def _up(self):
        self.up()

    def _down(self):
        self.down()

    def colorRed(self):
        self.color("red")

    def colorBlue(self):
        self.color("blue")

    def fwd(self):
        self.forward(self.distance)

    def bkwd(self):
        self.backward(self.distance)

    def leftTurn(self):
        self.left(self.turn)

    def rightTurn(self):
        self.right(self.turn)

    @staticmethod
    def main():
        mainloop()


# A way of running the program with an instance of the object Etch
if __name__ == '__main__':
    etch = Etch()
