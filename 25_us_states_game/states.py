from turtle import Turtle
import pandas

class States(Turtle):
    def __init__(self):
        self.get_states()
    
    def get_states(self):
        self.states = pandas.read_csv("50_states.csv")

    def guess_state(self, guess):
        state = self.states[self.states.state == guess]
        if state.empty:
            return False
        else:
            state_name = str(state.state.values[0])
            x_cor = int(state.x.item())
            y_cor = int(state.y.item())
            self.print_state(state_name, x_cor, y_cor)
            return True
        
    def print_state(self, state_name, x_cor, y_cor):
        
        new_state = Turtle()
        new_state.hideturtle()
        new_state.penup()
        new_state.goto(x_cor, y_cor)
        new_state.write(arg=state_name, align="center")

