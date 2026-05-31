import random

VALID_RUNS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def get_input(prompt, valid_values):
    while True:
        try:
            value = int(input(prompt))
            if value in valid_values:
                return value
            print("Invalid Input!")
        except ValueError:
            print("Invalid Input!")


def computer_choice(valid_values):
    return random.choice(valid_values)


def zero_challenge(batsman_name, bowler_name, human_is_batsman):
    print("\nZERO CHALLENGE!")
    print("Choose only 1 or 2")

    if human_is_batsman:
        bat = get_input(f"{batsman_name}, enter 1 or 2: ", [1, 2])
        bowl = computer_choice([1, 2])
    else:
        bat = computer_choice([1, 2])
        bowl = get_input(f"{bowler_name}, enter 1 or 2: ", [1, 2])

    print(f"{batsman_name}: {bat}")
    print(f"{bowler_name}: {bowl}")

    if bat == bowl:
        print("OUT!")
        return True
    else:
        print("SAFE!")
        return False


def play_innings(batsman_name, bowler_name, human_is_batsman, target=None, max_balls=None):
    score = 0
    balls = 0
    zero_count = 0
    highest_ball = 0

    while True:
        if max_balls is not None and balls == max_balls:
            break

        print("\n--------------------------------")

        if human_is_batsman:
            bat = get_input(f"{batsman_name}, enter runs (0-10): ", VALID_RUNS)
            bowl = computer_choice(VALID_RUNS)
        else:
            bat = computer_choice(VALID_RUNS)
            bowl = get_input(f"{bowler_name}, enter bowl (0-10): ", VALID_RUNS)

        balls += 1

        print(f"\nBall: {balls}" if max_balls is None else f"\nBall: {balls}/{max_balls}")
        print(f"{batsman_name}: {bat}")
        print(f"{bowler_name}: {bowl}")

        if bat == 0:
            zero_count += 1
            print(f"Zeros Used: {zero_count}/3")

            if zero_count == 4:
                print("OUT! Batsman used 0 four times.")
                break

        if bat == 0 and bowl == 0:
            out = zero_challenge(batsman_name, bowler_name, human_is_batsman)
            if out:
                break
            runs = 0

        elif bat == bowl:
            print("OUT!")
            break

        else:
            runs = bat
            score += runs
            highest_ball = max(highest_ball, runs)
            print(f"Runs Scored: {runs}")

        print(f"Score: {score}")

        if max_balls is not None:
            print(f"{score} runs from {balls} balls")

        if target is not None:
            if score >= target:
                print(f"{batsman_name} reached the target!")
                break
            need = target - score
            balls_left_text = ""
            if max_balls is not None:
                balls_left = max_balls - balls
                balls_left_text = f" from {balls_left} balls"
            print(f"Target: {target}")
            print(f"Need: {need} runs{balls_left_text}")

        print("--------------------------------")

    return {
        "score": score,
        "balls": balls,
        "zeros": zero_count,
        "highest_ball": highest_ball
    }


def toss():
    print("========== TOSS ==========")

    choice = input("Choose Odd or Even: ").strip().lower()
    while choice not in ["odd", "even"]:
        print("Invalid Input!")
        choice = input("Choose Odd or Even: ").strip().lower()

    user_num = get_input("Enter toss number (0-10): ", VALID_RUNS)
    comp_num = computer_choice(VALID_RUNS)

    total = user_num + comp_num
    result = "even" if total % 2 == 0 else "odd"

    print(f"You chose: {user_num}")
    print(f"Computer chose: {comp_num}")
    print(f"Total: {total} ({result})")

    if choice == result:
        print("You won the toss!")
        decision = input("Choose Bat or Bowl: ").strip().lower()
        while decision not in ["bat", "bowl"]:
            print("Invalid Input!")
            decision = input("Choose Bat or Bowl: ").strip().lower()
        return decision
    else:
        print("Computer won the toss!")
        decision = random.choice(["bat", "bowl"])
        print(f"Computer chose to {decision} first.")
        return "bowl" if decision == "bat" else "bat"


def play_super_over(super_over_number):
    print(f"\n========== SUPER OVER #{super_over_number} ==========")

    print("\nPlayer batting in Super Over")
    player = play_innings(
        "Player",
        "Computer",
        human_is_batsman=True,
        target=None,
        max_balls=6
    )

    target = player["score"] + 1
    print(f"\nComputer needs {target} runs to win.")

    computer = play_innings(
        "Computer",
        "Player",
        human_is_batsman=False,
        target=target,
        max_balls=6
    )

    if computer["score"] >= target:
        return "Computer", player, computer
    elif computer["score"] == player["score"]:
        print("SUPER OVER TIED!")
        return "Tie", player, computer
    else:
        return "Player", player, computer


def match_summary(player, computer, winner):
    print("\n==========================")
    print("MATCH SUMMARY")
    print("==========================")
    print(f"Player Score   : {player['score']}")
    print(f"Computer Score : {computer['score']}")
    print(f"Player Balls   : {player['balls']}")
    print(f"Computer Balls : {computer['balls']}")
    print(f"Player Zeros   : {player['zeros']}")
    print(f"Computer Zeros : {computer['zeros']}")
    print(f"Winner         : {winner}")
    print("==========================")


def main():
    print("================================")
    print("WELCOME TO HAND CRICKET")
    print("Human vs Computer")
    print("RULE: YOU CAN KEEP 0 ONLY THREE TIMES AS A BATSMAN!")
    print("================================")

    decision = toss()

    if decision == "bat":
        print("\nYou are batting first.")
        player = play_innings("Player", "Computer", human_is_batsman=True)

        target = player["score"] + 1
        print(f"\nTarget for Computer: {target}")

        computer = play_innings(
            "Computer",
            "Player",
            human_is_batsman=False,
            target=target
        )

    else:
        print("\nComputer is batting first.")
        computer = play_innings("Computer", "Player", human_is_batsman=False)

        target = computer["score"] + 1
        print(f"\nTarget for Player: {target}")

        player = play_innings(
            "Player",
            "Computer",
            human_is_batsman=True,
            target=target
        )

    if player["score"] > computer["score"]:
        winner = "Player"
    elif computer["score"] > player["score"]:
        winner = "Computer"
    else:
        print("\nMATCH TIED!")
        super_over_number = 1

        while True:
            winner, so_player, so_computer = play_super_over(super_over_number)

            if winner != "Tie":
                break

            super_over_number += 1

    match_summary(player, computer, winner)


main()