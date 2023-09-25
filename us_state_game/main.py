import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name")
data = pandas.read_csv("50_states.csv")
states = data.to_dict()
print(states)

# if answer_state in states:
#     turtle.goto()
#     turtle.write(answer_state)


def get_mouse_click_color(x, y):
    print(x, y)


turtle.onscreenclick(get_mouse_click_color)
turtle.mainloop()
