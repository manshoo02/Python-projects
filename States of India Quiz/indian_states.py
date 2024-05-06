import turtle
import pandas
screen = turtle.Screen()
screen.title("Indian States")
image = "States of India Quiz\India-state.gif"
screen.addshape(image)
turtle.shape(image)

states = 28
data = pandas.read_csv("States of India Quiz\states_data.csv")
all_states = data.state.to_list()
print(all_states)
guessed_states = []
while len(guessed_states) < 50:
    answer = screen.textinput(title=f"{len(guessed_states)}/28 States Guessed", prompt="Guess the state.").title()
    if answer == "Exit":
        missing = []
        for state in all_states:
            if state not in guessed_states:
                missing.append(state)
        print("States to learn :")
        print(missing)
        break
    if answer in all_states:
        guessed_states.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer]
        t.goto(int(state_data.x) , int(state_data.y))
        t.write(answer)
            
screen.exitonclick()









