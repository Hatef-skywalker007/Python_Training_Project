players = []


def add_player():

    name = input("Player name: ")

    player = {
        "name": name,
        "score": 0
    }

    players.append(player)

    print("Player added!")


def show_players():

    if not players:
        print("No players.")

    for player in players:
        print(
            player["name"],
            "-",
            player["score"]
        )


def add_score():

    name = input("Player name: ")
    score = int(input("Score: "))

    for player in players:

        if player["name"] == name:
            player["score"] += score
            print("Score updated!")
            return

    print("Player not found.")


def show_top_player():

    if not players:
        print("No players.")

        return

    top_player = max(
        players,
        key=lambda player: player["score"]
    )

    print(
        "Top player:",
        top_player["name"],
        top_player["score"]
    )


while True:

    print("\n===== GAME MANAGER =====")

    print("1. Add Player")
    print("2. Show Players")
    print("3. Add Score")
    print("4. Show Top Player")
    print("5. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_player()

    elif choice == "2":
        show_players()

    elif choice == "3":
        add_score()

    elif choice == "4":
        show_top_player()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")