from turtle import Turtle

FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.point = 0
        self.hideturtle()
        self.penup()
        self.goto(-210,250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-210, 250)
        self.color("yellow")
        self.write(f"Level: {self.level}", align="center", font=FONT)


    
    def increase_level(self):
        self.level += 1
        self.point += 100
        self.update_scoreboard()


    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write("GAME OVER", align="center", font= ("Arial", 40, "bold"))
       