import random
import time
#i have been tasked to recreate the game mastermind in python
#everything is put in here 
#list of things:
#gui (using pygame)
#actual code (background logic for the game)
def generate_code():
    return [random.randint(1, 6) for _ in range(4)]
def get_player_guess():
    while True:
        guess = input("Enter 4 digits (1-6) separated by spaces: ")
        guess_list = []
        valid = True
        
        for num in guess.strip().split():
            if not num.isdigit():
                valid = False
                break
            n = int(num)
            if n < 1 or n > 6:
                valid = False
                break
            guess_list.append(n)
        if guess == "secret hack":
            print("Activating secret hack client...")
            time.sleep(2)
            secret_code = generate_code()
            if random.random() < 0.5:
                print("Hack client activated successfully!")
                time.sleep(1)
                code = input("Enter other secret command for verification: ")
                if code == "kai is cool":
                    time.sleep(1)
                    print("Verification successful. Revealing the secret code...")
                    time.sleep(1)
                    print(f"The secret code is: fuh naw im not telling you")
            else:
                print("Hack client failed to activate.")
                time.sleep(1)
            continue
        elif guess == "skip":
            print("Skipping attempt..")
            time.sleep(1)
            return [1,1,1,1]  # special code for skipping
        
        if not valid or len(guess_list) != 4:
            print("Please enter exactly 4 numbers between 1 and 6.")
            continue
            
        return guess_list
def check_guess(secret_code, guess):
    exact_matches = sum(1 for i in range(4) if secret_code[i] == guess[i])
    # Count total matches including wrong positions
    secret_counts = {}
    guess_counts = {}
    for s, g in zip(secret_code, guess):
        secret_counts[s] = secret_counts.get(s, 0) + 1
        guess_counts[g] = guess_counts.get(g, 0) + 1
    
    color_matches = sum(min(secret_counts.get(n, 0), guess_counts.get(n, 0)) for n in range(1, 7))
    wrong_position = color_matches - exact_matches
    wrong_num = sum(1 for i in range(4) if secret_code[i] != guess[i]) - wrong_position

    return exact_matches, wrong_position, wrong_num, guess
#win+lose conditions
def play_mastermind():
    print("Welcome to Mastermind!")
    time.sleep(1.0)
    print("Try to guess the 4-digit code (numbers 1-6)")
    time.sleep(1.0)
    print("You'll get hints on which number is correct, in the wrong position or wrong.")
    time.sleep(1.0)
    
    secret_code = generate_code()
    attempts = 0
    max_attempts = 6
    
    while attempts < max_attempts:
        attempts += 1
        print(f"\nAttempt {attempts}/{max_attempts}")

        guess = get_player_guess()
        exact, wrong_pos, wrong_num, i = check_guess(secret_code, guess)
        
        if exact == 4:
            print(f"Congratulations! You cracked the code in {attempts} attempts!")
            return
        if i == 1234:
            print("Easter Egg Found! You discovered the secret code 1234!")
            return

        print(f"Correct position: {exact}")
        print(f"Correct number, wrong position: {wrong_pos}")
        print(f"Wrong number: {wrong_num}")
    
    print(f"You lost! The code was {secret_code}")
#play game 
play_mastermind()
time.sleep(1)
import subprocess
print("now, let's do something fun with vscode...")
time.sleep(2)
print("I have...")
time.sleep(2)
print("a little surprise for you...")
time.sleep(3)
print("💣")
time.sleep(2)
print("his name is bob :)")
time.sleep(2)
print("will he blow up?")
time.sleep(2)
print("let's find out...")
time.sleep(3)
print("not really")
time.sleep(2)
print("but he will close vscode")
time.sleep(2)
print("he is a very good technician")
time.sleep(3)
print("go bob do something")
time.sleep(1)
def close_vscode(grace_period=3):
    procs = ["Code.exe", "Code - Insiders.exe"]
    # try graceful close first
    for p in procs:
        subprocess.run(["taskkill", "/IM", p], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(grace_period)
    # force kill any remaining instances
    for p in procs:
        subprocess.run(["taskkill", "/IM", p, "/F"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
 
close_vscode()