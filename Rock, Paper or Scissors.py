def rounds_game(rounds):
    rounds = int(rounds)
    number_of_players = input("How much players want to play? ")
    if number_of_players == "1":
        for i in range(rounds):
            import random
            user_choice = input("Enter your choice(Rock, Paper or Scissors) ")
            cp_choice = random.choice(["Rock","Paper","Scissors"])
            if user_choice == "Scissors" and cp_choice == "Paper" or user_choice == "Paper" and cp_choice == "Rock" or user_choice == "Rock" and cp_choice == "Scissors":
                print(f"So you won that point, you chose {user_choice} and I chose {cp_choice}.")
            elif user_choice == "Rock" and cp_choice == "Paper" or user_choice == "Scissors" and cp_choice == "Rock" or user_choice == "Paper" and cp_choice == "Scissors":
                print(f"I knew I'm gonna beat you, you chose {user_choice} and I chose {cp_choice}.")
            else:
                print(f"It's a tie, we both chose {user_choice}")
        return "Thanks for playing with me"
    else:
        import getpass
        user1 = input("What is your name? ")
        user2 = input("What is your name? ")
        for i in range(rounds):
            user1_choice = getpass.getpass("Enter your choice(Rock, Paper or Scissors) ")
            user2_choice = getpass.getpass("Enter your choice(Rock, Paper or Scissors) ")
            if user1_choice == "Scissors" and user2_choice == "Paper" or user1_choice == "Paper" and user2_choice == "Rock" or user1_choice == "Rock" and user2_choice == "Scissors":
                print(f"congratulation {user1} won, {user1} chose {user1_choice} and {user2} chose {user2_choice}")
            elif user1_choice == "Rock" and user2_choice == "Paper" or user1_choice == "Scissors" and user2_choice == "Rock" or user1_choice == "Paper" and user2_choice == "Scissors":
                print(f"congratulation {user2} won, {user1} chose {user1_choice} and {user2} chose {user2_choice}")
            else:
                print(f"It's a tie, {user1} chose {user1_choice} and {user2} chose {user2_choice}")
        return "I hope you enjoy with my game"

def best_out_of_game(points):
    points = int(points)
    user1_points = 0
    user2_points = 0
    number_of_players = input("How much players want to play? ")
    if number_of_players == "1":
        import random
        while user1_points < points and user2_points < points:
            user_choice = input("Enter your choice(Rock, Paper or Scissors) ")
            cp_choice = random.choice(["Rock","Paper","Scissors"])
            if user_choice == "Scissors" and cp_choice == "Paper" or user_choice == "Paper" and cp_choice == "Rock" or user_choice == "Rock" and cp_choice == "Scissors":
                user1_points += 1
                print(f"So you won that point, you chose {user_choice} and I chose {cp_choice}.")
                print(f"now you have {user1_points} points and I have {user2_points} points")
            elif user_choice == "Rock" and cp_choice == "Paper" or user_choice == "Scissors" and cp_choice == "Rock" or user_choice == "Paper" and cp_choice == "Scissors":
                user2_points += 1
                print(f"I knew I'm gonna beat you, you chose {user_choice} and I chose {cp_choice}.")
                print(f"now you have {user1_points} points and I have {user2_points} points")
            else:
                print(f"It's a tie, we both chose {user_choice}")
        else:
            return "Thanks for playing with me"
    else:
        import getpass
        user1 = input("What is your name? ")
        user2 = input("What is your name? ")
        while user1_points < points and user2_points < points:
            user1_choice = getpass.getpass("Enter your choice(Rock, Paper or Scissors) ")
            user2_choice = getpass.getpass("Enter your choice(Rock, Paper or Scissors) ")
            if user1_choice == "Scissors" and user2_choice == "Paper" or user1_choice == "Paper" and user2_choice == "Rock" or user1_choice == "Rock" and user2_choice == "Scissors":
                user1_points += 1
                print(f"congratulation {user1} won, {user1} chose {user1_choice} and {user2} chose {user2_choice}")
                print(f"now {user1} have {user1_points} points and {user2} have {user2_points} points")
            elif user1_choice == "Rock" and user2_choice == "Paper" or user1_choice == "Scissors" and user2_choice == "Rock" or user1_choice == "Paper" and user2_choice == "Scissors":
                user2_points += 1
                print(f"congratulation {user2} won, {user1} chose {user1_choice} and {user2} chose {user2_choice}")
                print(f"now {user1} have {user1_points} points and {user2} have {user2_points} points")
            else:
                print(f"It's a tie, {user1} chose {user1_choice} and {user2} chose {user2_choice}")
        else:
            return "I hope you enjoy with my game"

def game_vs_computer():
    import random
    while input("If you want to play press y if not press q: ") != "q":
        user_choice = input("Enter your choice(Rock, Paper or Scissors) ")
        cp_choice = random.choice(["Rock","Paper","Scissors"])
        if user_choice == "Scissors" and cp_choice == "Paper" or user_choice == "Paper" and cp_choice == "Rock" or user_choice == "Rock" and cp_choice == "Scissors":
            print(f"So you won that point, you chose {user_choice} and I chose {cp_choice}.")
        elif user_choice == "Rock" and cp_choice == "Paper" or user_choice == "Scissors" and cp_choice == "Rock" or user_choice == "Paper" and cp_choice == "Scissors":
            print(f"I knew I'm gonna beat you, you chose {user_choice} and I chose {cp_choice}.")
        else:
            print(f"It's a tie, we both chose {user_choice}")
    else:
        return "Thanks for playing with me"

def game_for_2():
    import getpass
    user1 = input("What is your name? ")
    user2 = input("What is your name? ")
    while input("If you want to play press y if not press q: ") != "q":
        user1_choice = getpass.getpass("Enter your choice(Rock, Paper or Scissors) ")
        user2_choice = getpass.getpass("Enter your choice(Rock, Paper or Scissors) ")
        if user1_choice == "Scissors" and user2_choice == "Paper" or user1_choice == "Paper" and user2_choice == "Rock" or user1_choice == "Rock" and user2_choice == "Scissors":
            print(f"congratulation {user1} won, {user1} chose {user1_choice} and {user2} chose {user2_choice}")
        elif user1_choice == "Rock" and user2_choice == "Paper" or user1_choice == "Scissors" and user2_choice == "Rock" or user1_choice == "Paper" and user2_choice == "Scissors":
            print(f"congratulation {user2} won, {user1} chose {user1_choice} and {user2} chose {user2_choice}")
        else:
            print(f"It's a tie, {user1} chose {user1_choice} and {user2} chose {user2_choice}")
    else:
        return "I hope you enjoy with my game"
    
def the_game(game_type):
    if game_type == "1":
        return game_vs_computer()
    elif game_type =="2":
        return game_for_2()
    elif game_type == "3":
        return rounds_game(input("How much rounds do you want to play? "))
    elif game_type == "4":
        return best_out_of_game(input("How much points is the maximum? "))
    else:
        pass

print(the_game(input("Enter which game you want to play:\f1 - vs the computer\f2 - vs a friend\f3 - rounds game\f4 - game with points\f")))