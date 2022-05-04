# How To Create Rock Paper Scissors In Python!
import random
print(f"Welcome To Rock Paper Scissors! Please Enter You're Choice: ")

while True:
    try:
        choice = ["Rock", "Paper", "Scissors"]
        answer_of_human = str(input()).capitalize()
        answer_of_bot = random.choice(choice)

        # Possibilities Of The Player Winning
        if "Rock" in answer_of_human and "Scissors" in answer_of_bot:
            print(f"You're Answer: {answer_of_human}")
            print(f"Bots Answer: {answer_of_bot}")
            print("You Won!")

        if "Paper" in answer_of_human and "Rock" in answer_of_bot:
            print(f"You're Answer: {answer_of_human}")
            print(f"Bots Answer: {answer_of_bot}")
            print("You Won!")

        if "Scissors" in answer_of_human and "Paper" in answer_of_bot:
            print(f"You're Answer: {answer_of_human}")
            print(f"Bots Answer: {answer_of_bot}")
            print("You Won!")

        # Possibilities Of The Bot Winning!

        if "Paper" in answer_of_human and "Scissors" in answer_of_bot:
            print(f"You're Answer: {answer_of_human}")
            print(f"Bots Answer: {answer_of_bot}")
            print("You Lost!")

        if "Scissors" in answer_of_human and "Rock" in answer_of_bot:
            print(f"You're Answer: {answer_of_human}")
            print(f"Bots Answer: {answer_of_bot}")
            print("You Lost!")

        if "Rock" in answer_of_human and "Scissors" in answer_of_bot:
            print(f"You're Answer: {answer_of_human}")
            print(f"Bots Answer: {answer_of_bot}")
            print("You Lost!")

        # Possibilities Of Tie!

        if "Rock" in answer_of_human and "Rock" in answer_of_bot:
            print(f"You're Answer: {answer_of_human}")
            print(f"Bots Answer: {answer_of_bot}") 
            print("It's A Tie!") 

        if "Paper" in answer_of_human and "Paper" in answer_of_bot:
            print(f"You're Answer: {answer_of_human}")
            print(f"Bots Answer: {answer_of_bot}") 
            print("It's A Tie!") 

        if "Scissors" in answer_of_human and "Scissors" in answer_of_bot:
            print(f"You're Answer: {answer_of_human}")
            print(f"Bots Answer: {answer_of_bot}") 
            print("It's A Tie!") 

    except:
        print("Please Enter A Valid Value!")