import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guessed_states = []

while len(guessed_states) < 50:
    answer = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="Enter a state's name or type Exit:"
    )

    if answer is None:
        break

    answer_state = answer.strip().title()

    # Exit the game and create file
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv", index=False)
        break

    # Check answer
    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)

        state_row = data[data.state == answer_state]
        x = int(state_row.x)
        y = int(state_row.y)

        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(x, y)
        t.write(answer_state)

turtle.mainloop()
