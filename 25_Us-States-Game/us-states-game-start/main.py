from turtle import Turtle,Screen
import pandas

screen = Screen()
turtle = Turtle()

image = 'blank_states_img.gif'
screen.addshape(image)
screen.title("Name Of State")
turtle.shape(image)

score = 0

data = pandas.read_csv("50_states.csv")
state_names = data["state"].to_list()

count = 0
guessed_state = []
missing_state = []

while count < 50:
    answer_state = screen.textinput(title=f"{count}/50 Guess Correct", prompt="What is another state name?").title()

    if answer_state in state_names:
        t = Turtle()
        t.penup()
        t.hideturtle()
        state = data[data.state == answer_state]

        t.goto(int(state.x), int(state.y))
        t.write(answer_state)
        guessed_state.append(answer_state)
        count += 1

    if answer_state == "Exit":
        for state in state_names:
            if state not in guessed_state:
                missing_state.append(state)
        # learn_data = pandas.DataFrame(missing_state)
        # learn_data.to_csv("learn.csv")
        # result = [i for i in state_names if i not in guessed_state]

        break




screen.exitonclick()