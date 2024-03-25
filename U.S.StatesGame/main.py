import turtle
import pandas

score = 0

screen = turtle.Screen()
screen.title("U.S. States Game")
image = 'blank_states_img.gif'
screen.addshape(image)

data = pandas.read_csv('50_states.csv')
states_list = data['state'].to_list()
guessed_states = []

turtle.shape(image)

while len(guessed_states) < 50:
    answer = screen.textinput(title=f"Guessed {score}/50 States", prompt="Guess a state").title()
    if answer == "Exit":
        missing_states = [state for state in states_list if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('states_to_learn.csv')
        break
    if answer in states_list:
        guessed_states.append(answer)
        score += 1
        tim = turtle.Turtle()
        tim.penup()
        tim.hideturtle()
        state_data = data[data.state == answer]
        tim.goto(int(state_data.x), int(state_data.y))
        tim.write(f"{answer}")

# screen.exitonclick()
