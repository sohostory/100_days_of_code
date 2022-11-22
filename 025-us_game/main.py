import pandas
import turtle
from answers import Answers

screen = turtle.Screen()
screen.title("U.S. STate Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
turtle.penup()
answers = Answers()



correct_guesses = 0
correct_answers = []
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
answer_state = screen.textinput(title="Guess the State", prompt="What's a state's name?").title()

while correct_guesses < 50:
    if answer_state == "Exit":
        with open("to_learn.csv", mode="w") as file:
            for state in all_states:
                file.write(f"{state}\n")
        break
    try:
        correct_state = data[data.state == answer_state]
        x = float(correct_state.x)
        y = float(correct_state.y)
        state_name = str(correct_state.state)
        answers.update_answers(answer_state, x, y)
        correct_guesses += 1
        correct_answers += answer_state
    except:
        pass
    all_states.remove(answer_state)
    answer_state = screen.textinput(title=f"{correct_guesses}/50 States Correct", prompt="What's another state's name?").title()