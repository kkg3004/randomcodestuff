#today i have created
#the most inefficient (and fun) way to print hello world
#there are a few lines yes
#275 to be exact
#so enjoy this stupid masterpiece of code
# - kai :)

#a lot of import stuff (thank you tkinter and others)
import random
import threading
import time
import tkinter as tk
from tkinter import messagebox

#spoilers ahead

#the start of it all
user_input = input("What's the Magic Word? (hint: function to write hello world): ")

#yes there's only five, sue me
riddles = ["What has hands, but cannot clap?", "What has to be broken before you can use it?", "What has a head, a tail, is brown, and has no legs?", "What has keys but can't open locks?", "What is black, white and read all over?"]

#i wonder what these are
answers = ["clock", "egg", "penny", "piano", "newspaper"]

#funny error popup
def error():
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("Error", "You failed.\nPlease restart HelloWorld.")
    root.destroy()

#the actual code
def HelloWorld(user_input):
    #checks if the user input is correct
    if user_input == "print":
        time.sleep(1)
        print("Correct.")
        time.sleep(0.5)
        #coin toss cuz why not
        print("Tossing coin...")
        time.sleep(1)
        if random.randint(0, 1) == 0:
            #hi
            print("Welcome to HelloWorld.")
            time.sleep(1)
            #captchas in 2026
            robot = input("Are you a robot? (yes/no): ")
            if robot.lower() == "no":
                time.sleep(1)
                #wow
                print("You are not a robot.")
                time.sleep(1)
                #cool loading thing
                print("Loading", end="", flush=True)
                for _ in range(10):
                    time.sleep(0.3)
                    print(".", end="", flush=True)
                print("\nLoaded successfully!")
                #nice
                time.sleep(1)
                #challenge 1
                print("Challenge Time!")
                time.sleep(1)
                cups = [1, 2, 3]
                ball_position = random.choice(cups)
                print(f"The ball is under cup {ball_position}.")
                #thanks :)
                time.sleep(2)
                print('Now "shuffling..."')
                #i thought it would be funny to fake the shuffling
                for _ in range(3):
                    time.sleep(1)
                    print("*shuffling intensifies*")
                time.sleep(1)
                user_guess = input("Which cup has the ball? (1/2/3): ")
                #its the same as last time
                if user_guess == str(ball_position):
                    print("You found the ball!")
                else:
                    print(f"Wrong! I told you the ball was under cup {ball_position}.")
                    #yeah
                    error()
                time.sleep(5)
                print("But wait. There's more.")
                #woah.
                time.sleep(1)
                #challenge 2
                print("You have to answer a riddle to proceed.")
                time.sleep(1)
                #yes it's a random riddle each time
                riddle_index = random.randint(0, len(riddles) - 1)
                riddle_answer = riddles[riddle_index]
                print(f"Riddle: {riddle_answer}")
                user_response = input("Your answer: ")
                #i still dont know how this works but it does
                if user_response.lower() == answers[riddle_index]:
                    print("Correct.")
                    time.sleep(1)
                    timeout = 3
                    #challenge 3 (quickitme event)
                    print("QUICK, WHAT'S THE MAGIC WORD?")
                    thread = threading.Thread(target=input, args=("",), daemon=True)
                    thread.start()
                    thread.join(timeout)
                    if thread.is_alive():
                        print("\nToo slow!")
                        #lol
                        error()
                    if user_response == "print":
                        print("Correct.")
                    time.sleep(1)
                    #challenge 4 random number time
                    random_number = random.randint(1, 100)
                    print(f"Random number generated: {random_number}")
                    print("Now, let's see if you can guess it.")
                    user_guess = input("Your guess (1-100): ")
                    #same silly fake as with the cups, but no clues
                    if user_guess == "41":
                        #unc lost his mind
                        print("Correct!")
                    else:
                        print(f"Incorrect. The correct number is {random_number - random.randint(1, 5)}.")
                        #this is also a lie
                        error()
                    time.sleep(1)
                    #challenge 5
                    print("History quiz!")
                    time.sleep(1)
                    print("What's the capital of France?")
                    user_answer = input("Your answer: ")
                    #oh oui oui oui
                    if user_answer.lower() == "paris":
                        print("Correct!")
                    else:
                        print("Incorrect.")
                        #how did you fail that
                        error()
                    time.sleep(1)
                    print("One more hard question.")
                    time.sleep(1)
                    #a little bit hard
                    print("Who took a dump on the floor of the White House in 1814?")
                    user_answer = input("Your answer: ")
                    #idk if this is real or not
                    if user_answer.lower() == "dolley madison":
                        print("Correct!")
                    else:
                        print("Incorrect.")
                        #i dont blame you for that
                        error()
                    time.sleep(1)
                    #final challenge
                    print("Final challenge.")
                    #hey you copied me
                    time.sleep(1)
                    print("What is the answer to life, the universe, and everything?")
                    #this one is just personal opinion
                    user_answer = input("Your answer: ")
                    if user_answer.lower() == "kanye west":
                        print("Correct.")
                        #ay
                    else:
                        print("It's personal preference anyways.")
                        #free pass for this
                    #finally its printing
                    time.sleep(3)
                    print("Printing")
                    for _ in range(10):
                        time.sleep(0.5)
                        print(".", end="", flush=True)
                    time.sleep(3)
                    #this took way too much trial and error (thanks macOS)
                    WIDTH, HEIGHT = 220, 100
                    SPEED_X, SPEED_Y = 4, 3

                    root = tk.Tk()
                    root.title("Hello World")
                    root.resizable(False, False)
                    root.overrideredirect(True)
                    root.attributes("-topmost", True)

                    def ignore_key(event):
                        del event

                    root.bind_all("<Key>", ignore_key)
                    root.focus_force()

                    label = tk.Label(
                        root,
                        text="hello world",
                        font=("Helvetica", 32, "bold"),
                        bg="#1e90ff",
                        fg="white",
                    )
                    label.pack(fill="both", expand=True)

                    def change_colors():
                        background = f"#{random.randrange(0x1000000):06x}"
                        red, green, blue = (
                            int(background[i:i + 2], 16) for i in (1, 3, 5)
                        )
                        luminance = 0.299 * red + 0.587 * green + 0.114 * blue
                        label.configure(
                            bg=background,
                            fg="black" if luminance > 140 else "white",
                        )

                    root.geometry(f"{WIDTH}x{HEIGHT}+100+100")
                    dx, dy = SPEED_X, SPEED_Y

                    def move_window():
                        nonlocal dx, dy
                        x, y = root.winfo_x(), root.winfo_y()
                        screen_w = root.winfo_screenwidth()
                        screen_h = root.winfo_screenheight()
                        min_y = 30
                        max_y = screen_h - HEIGHT
                        max_x = screen_w - WIDTH
                        next_x = x + dx
                        next_y = y + dy

                        if next_x <= 0:
                            dx = abs(SPEED_X)
                            next_x = 0
                            change_colors()
                        elif next_x >= max_x:
                            dx = -abs(SPEED_X)
                            next_x = max_x
                            change_colors()

                        if next_y <= min_y:
                            dy = abs(SPEED_Y)
                            next_y = min_y
                            change_colors()
                        elif next_y >= max_y:
                            dy = -abs(SPEED_Y)
                            next_y = max_y
                            change_colors()

                        root.geometry(
                            f"{WIDTH}x{HEIGHT}+{int(next_x)}+{int(next_y)}"
                        )
                        root.after(16, move_window)

                    def close_window(event):
                        del event
                        root.destroy()

                    root.bind_all("<Escape>", close_window)

                    def focus_window(event):
                        del event
                        root.focus_set()

                    label.bind("<Button-1>", focus_window)
                    move_window()
                    root.mainloop()
                #if u get it all wrong
                else:
                    print("Incorrect.")
                    error()
            else:
                print("You are a robot.")
                error()
        else:
            print("Oops. You failed the coin toss. Try again.")
            error()
    else:
        time.sleep(1)
        print("Incorrect. Please try again.")
        error()

#code start
HelloWorld(user_input)