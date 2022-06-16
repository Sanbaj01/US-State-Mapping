import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states_dict = data.to_dict()

states_list = data.state.to_list()


guessed_list = []

while len(guessed_list) < 50:
    answer_state = screen.textinput(f"{len(guessed_list)}/50 states guessed", "Guess another state").title()
    if answer_state == "Exit":
        missing_states = [state for state in states_list if state not in guessed_list]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in states_list:
        guessed_list.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())


