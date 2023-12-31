# importing the modules
import turtle
import pandas

# creating the screen object
screen = turtle.Screen()

# changing the title of the project
screen.title("U.S. States Game")

# storing the image path to a new variable named as image
image = "blank_states_img.gif"

# adding the shape as image using new variable
screen.addshape(image)

# displaying the shape
turtle.shape(image)

# reading the csv file using pandas module
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
while len(guessed_states) < 50:
# taking the input from the user and it popup the another screen
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    # printing the user input to the console
    print(answer_state)


    # If answer_state is one of the states in all the states of the 50_states.csv
    # If they got right:
    # Create a turtle to write the name of the state at the state's x and y coordinate
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data =  pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)



