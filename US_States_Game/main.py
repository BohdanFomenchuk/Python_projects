import turtle
import pandas

screen = turtle.Screen()
guess = turtle.Turtle()

screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
correct_number = 0

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
x_cor = data.x.to_list()
y_cor = data.y.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{correct_number}/50 States Correct",
                                    prompt="What's another state's name").title()
    if answer_state == 'Exit':
        missing_states = [state for state in states if state not in guessed_states]
        # for state in states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        states_to_learn = pandas.DataFrame(missing_states)
        states_to_learn.to_csv("states_to_learn")
        break
    if answer_state in states:
        guessed_states.append(answer_state)
        state_index = states.index(answer_state)
        guess.penup()
        guess.hideturtle()
        guess.goto(x_cor[state_index], y_cor[state_index])
        guess.write(answer_state)
        correct_number += 1

