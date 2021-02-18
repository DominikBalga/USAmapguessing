import turtle
import pandas
import time

screen = turtle.Screen()
screen.title("USA States Guessing game")
screen.tracer(0)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.listen()


def csv_missedstates():
    """creating csv for missed states"""
    missedstates = [record["state"] for record in data_dict]
    df = pandas.DataFrame(data=missedstates)
    df.to_csv("missed_states.csv")


def convert(seconds):
    """converting seconds to minutes"""
    seconds = seconds % (24 * 3600)
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%02d:%02d" % (minutes, seconds)


def type_state(x, y):
    """used to command typer to type the state"""
    typer.goto(x, y)
    typer.write(arg=f"{record['state']}", align="center", font=("Times", 8, "bold"))


# setting up time for while loop
starting_time = time.time()
# time limit in seconds
time_limit = 600

# writing turtle
typer = turtle.Turtle()
typer.penup()
typer.hideturtle()
# timing turtle
timer = turtle.Turtle()
timer.penup()
timer.hideturtle()
# Getting the coordinates of states
# def get_mouse_click_cor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_cor)
# importing csv and converting to usable dictionary
data = pandas.read_csv("50_states.csv")
data_dict = data.to_dict(orient="record")
guessed_states = 0
seconds_passed = 0
# asking for states and playing game
while guessed_states < 50:
    screen.update()
    state_number = -1
    # setting up timer
    seconds_passed = round(time.time() - starting_time)
    if seconds_passed > time_limit:
        csv_missedstates()
        break
    time_left = convert(time_limit - seconds_passed)
    timer.clear()
    timer.goto(200, 270)
    timer.write(arg=f"time left : {time_left}", align="center", font=("Times", 30, "bold"))
    # checking for answers
    answer = screen.textinput(title=f"states guessed:{guessed_states}/50", prompt="Please guess a U.S state or type exit if you give up ").lower()
    if answer == "exit":
        csv_missedstates()
        timeused = seconds_passed
        break
    for record in data_dict:
        state_number += 1
        lower = record["state"].lower()
        if lower == answer:
            guessed_states += 1
            data_dict.pop(state_number)
            type_state(record["x"], record["y"])
        else:
            continue
if guessed_states == 50:
    typer.goto(0, 0)
    typer.write(arg=f"YOU GUESSED THEM ALL", align="center", font=("Times", 30, "bold"))
elif seconds_passed > time_limit:
    typer.goto(0, 0)
    typer.write(arg=f"TIME'S UP", align="center", font=("Times", 30, "bold"))
else:
    typer.goto(0, 0)
    typer.write(arg=f"You left the game, file with states saved", align="center", font=("Times", 30, "bold"))

screen.exitonclick()
