def show_title():
    print("=" * 50)
    print("   MYSTERY ISLAND: THE LOST LIGHTHOUSE")
    print("=" * 50)
    print()
    print("A storm wrecked your boat and you wake up on a beach.")
    print("The lighthouse is dark and the bridge is unsafe.")
    print("Restore the beacon so the rescue boat can see you.")
    print()
    print("HOW TO PLAY:")
    print("- Type the number of an option and press Enter.")
    print("- You start with 5 energy. Moving costs 1 energy.")
    print("- If your energy reaches 0, you lose.")
    print("- Type q at any menu to quit.")
    print()


def get_player_name():
    while True:
        name = input("Enter your name: ").strip()
        if name != "":
            return name
        print("Please fill in your name.")


def show_status(name, energy, location, inventory):
    print()
    print("--- STATUS ---")
    print("Name:", name)
    print("Energy:", energy)
    print("Location:", location)
    if inventory:
        print("Inventory:", ", ".join(inventory))
    else:
        print("Inventory: empty")


def get_choice(options):
    while True:
        for number, text in enumerate(options, start=1):
            print(f"{number}. {text}")
        answer = input("Choose: ").strip().lower()
        if answer == "q":
            return 0
        if answer.isdigit():
            choice = int(answer)
            if 1 <= choice <= len(options):
                return choice
        print("Please enter a number from 1 to", len(options), "or q to quit.")


def play_game(name):
    energy = 5
    location = "Beach"
    inventory = []
    tide_pool_done = False
    berries_done = False

    while energy > 0:
        print()
        print("=== " + location.upper() + " ===")
        print("Energy:", energy)

        if location == "Beach":
            choice = get_choice([
                "Search the broken boat",
                "Walk into the Jungle",
                "Examine the tide pools",
                "Show status",
            ])
            if choice == 0:
                return "quit"
            elif choice == 1:
                if "Rope" in inventory:
                    print("You already took the Rope.")
                else:
                    inventory.append("Rope")
                    print("You find a strong Rope under a torn sail.")
            elif choice == 2:
                location = "Jungle"
                energy = energy - 1
                print("You walk to the Jungle. Energy -1.")
            elif choice == 3:
                if tide_pool_done:
                    print("The tide pool is empty now.")
                else:
                    print("A silver shape flashes between the rocks.")
                    pick = get_choice([
                        "Grab it quickly",
                        "Search carefully",
                        "Leave it alone",
                    ])
                    if pick == 0:
                        return "quit"
                    elif pick == 1:
                        tide_pool_done = True
                        energy = energy - 1
                        print("A crab pinches you. It was just a shell. Energy -1.")
                    elif pick == 2:
                        tide_pool_done = True
                        energy = energy + 1
                        print("You find a fresh coconut. Energy +1.")
                    else:
                        print("You save your energy.")
            elif choice == 4:
                show_status(name, energy, location, inventory)

        elif location == "Jungle":
            choice = get_choice([
                "Go to the Cave",
                "Go to the Old Bridge",
                "Go back to the Beach",
                "Inspect the berries",
                "Show status",
            ])
            if choice == 0:
                return "quit"
            elif choice == 1:
                location = "Cave"
                energy = energy - 1
                print("You walk to the Cave. Energy -1.")
            elif choice == 2:
                location = "Old Bridge"
                energy = energy - 1
                print("You walk to the Old Bridge. Energy -1.")
            elif choice == 3:
                location = "Beach"
                energy = energy - 1
                print("You walk back to the Beach. Energy -1.")
            elif choice == 4:
                if berries_done:
                    print("You already tested the berries.")
                else:
                    print("Birds eat the blue berries but avoid the red ones.")
                    pick = get_choice([
                        "Eat the red berries",
                        "Eat the blue berries",
                        "Eat nothing",
                    ])
                    if pick == 0:
                        return "quit"
                    elif pick == 1:
                        berries_done = True
                        energy = energy - 1
                        print("The red berries make you sick. Energy -1.")
                    elif pick == 2:
                        berries_done = True
                        energy = energy + 1
                        print("The blue berries are sweet. Energy +1.")
                    else:
                        print("You leave the berries alone.")
            elif choice == 5:
                show_status(name, energy, location, inventory)

        elif location == "Cave":
            choice = get_choice([
                "Pick up the old Lantern",
                "Go back to the Jungle",
                "Read the wall markings",
                "Show status",
            ])
            if choice == 0:
                return "quit"
            elif choice == 1:
                if "Lantern" in inventory:
                    print("You already took the Lantern.")
                else:
                    inventory.append("Lantern")
                    print("You take the Lantern. It still has some oil.")
            elif choice == 2:
                location = "Jungle"
                energy = energy - 1
                print("You walk back to the Jungle. Energy -1.")
            elif choice == 3:
                print("The markings show a Rope by a bridge and a Lantern by a beacon.")
            elif choice == 4:
                show_status(name, energy, location, inventory)

        elif location == "Old Bridge":
            choice = get_choice([
                "Try to cross to the Lighthouse",
                "Go back to the Jungle",
                "Inspect the bridge",
                "Show status",
            ])
            if choice == 0:
                return "quit"
            elif choice == 1:
                if "Rope" in inventory:
                    location = "Lighthouse"
                    print("You tie the Rope and cross safely.")
                else:
                    energy = energy - 1
                    print("A plank breaks! You jump back. You need Rope. Energy -1.")
            elif choice == 2:
                location = "Jungle"
                energy = energy - 1
                print("You walk back to the Jungle. Energy -1.")
            elif choice == 3:
                print("The handline is missing. A strong Rope would help.")
            elif choice == 4:
                show_status(name, energy, location, inventory)

        elif location == "Lighthouse":
            choice = get_choice([
                "Try to light the beacon",
                "Inspect the beacon",
                "Cross back to the Old Bridge",
                "Show status",
            ])
            if choice == 0:
                return "quit"
            elif choice == 1:
                if "Lantern" in inventory:
                    return "win"
                else:
                    energy = energy - 1
                    print("The beacon will not light. You need a Lantern. Energy -1.")
            elif choice == 2:
                print("The beacon has oil but no flame. A Lantern could light it.")
            elif choice == 3:
                location = "Old Bridge"
                print("You use the Rope to cross back.")
            elif choice == 4:
                show_status(name, energy, location, inventory)

    return "lose"


def show_ending(result, name):
    print()
    if result == "win":
        print("*** YOU WIN! ***")
        print(name + " lights the beacon and the rescue boat arrives!")
    elif result == "lose":
        print("*** YOU LOSE! ***")
        print(name + " ran out of energy. The boat sails past the dark island.")
    else:
        print("*** GAME ENDED ***")
        print("You leave Mystery Island for now.")


def ask_play_again():
    while True:
        answer = input("\nPlay again? (y/n): ").strip().lower()
        if answer == "y":
            return True
        if answer == "n":
            return False
        print("Please type y or n.")


def main():
    show_title()
    name = get_player_name()
    while True:
        result = play_game(name)
        show_ending(result, name)
        if not ask_play_again():
            print("Thanks for playing. Goodbye!")
            break


if __name__ == "__main__":
    main()