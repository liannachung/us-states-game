from turtle import Turtle

class New_state(Turtle):
    def __int__(self):
        super().__init__()
        self.hideturtle()

    def write_in(self, name, position):
        self.penup()
        self.hideturtle()
        self.goto(position)
        self.write(name, align="center", font=("Arial", 8, "normal"))

