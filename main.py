import turtle
import pandas
from new_state import New_state

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guessed_states = []

data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()


while len(guessed_states) < 50:
    answer = screen.textinput(title=f"Correct: {len(guessed_states)}/50", prompt="What's another State's Name?").title()
    if answer == "Exit":
        # missing_states = []
        # for state in states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        missing_states = [state for state in states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer in states:
        state_row = data[data["state"] == answer]
        state = New_state()
        state.write_in(answer, (int(state_row.x), int(state_row.y)))
        guessed_states.append(answer)

screen.exitonclick()