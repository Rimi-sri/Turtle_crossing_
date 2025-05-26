from turtle import Turtle

Starting_POSITION = (0, -280)
Move_DISTANCE = 10
Finish_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        # Make the turtle face upwards
        self.goto(Starting_POSITION)
        self.setheading(90) # Set initial position
    
     
     

    def move(self):
        self.forward(Move_DISTANCE)


    def is_at_finish_line(self):

       if self.ycor() > Finish_LINE_Y:
           return True
       else:
            return False
       
            
     
    
      