from turtle import Turtle
import random

random_colors = ["red", "orange", "yellow", "green", "blue", "purple", "gray", "white", "black"]

starting_moving_distance = 5
move_increment = 10

class CarManager:

    def __init__(self):
        # self.all_car will now store lists: [car_body_turtle, front_wheel_turtle, rear_wheel_turtle]
        self.all_car_components = []
        self.car_speed = starting_moving_distance

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            # 1. Create the main car body
            car_body = Turtle("square")
            car_body.color(random.choice(random_colors))
            car_body.penup()
            car_body.shapesize(stretch_wid=0.8, stretch_len=2) # Sleeker body
            
            # 2. Create front wheel
            front_wheel = Turtle("circle")
            front_wheel.color("black")
            front_wheel.penup()
            front_wheel.shapesize(stretch_wid=0.5, stretch_len=0.5) # Smaller circle for wheel

            # 3. Create rear wheel
            rear_wheel = Turtle("circle")
            rear_wheel.color("black")
            rear_wheel.penup()
            rear_wheel.shapesize(stretch_wid=0.5, stretch_len=0.5)

            # Determine initial position for the car body
            random_y = random.randint(-250, 250)
            start_x = 300 # Start off-screen to the right

            car_body.goto(start_x, random_y)

            # Position wheels relative to the car body
            # The body is 40 units long (2 * stretch_len * 20 default turtle size)
            # Wheels roughly at -15 and +15 relative to center of car body
            front_wheel.goto(start_x + 15, random_y - 10) # Adjust y slightly for visual alignment
            rear_wheel.goto(start_x - 15, random_y - 10)

            # Store all components together
            self.all_car_components.append([car_body, front_wheel, rear_wheel])
        
    def move_cars(self):
        # Iterate through each list of components (car_body, wheel1, wheel2)
        for car_components in self.all_car_components:
            car_body = car_components[0]
            front_wheel = car_components[1]
            rear_wheel = car_components[2]

            # Move each component
            car_body.backward(self.car_speed)
            front_wheel.backward(self.car_speed)
            rear_wheel.backward(self.car_speed)
        
    def increase_speed(self):
        self.car_speed += move_increment
        print(f"Car speed increased to: {self.car_speed}")