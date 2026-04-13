import random

def main():
    def setup_player():
        """
        Prompts the user to create their player profile.

        Returns:
            dict: A dictionary containing player stats with the following keys:
                - "name" (str): Player's name (entered by user)
                - "health" (int): Starting health, set to 10
                - "inventory" (list): Starts as an empty list
        Example:
            >>> setup_player()
            Enter your name: Ailene
            {'name': 'Ailene', 'health': 10, 'inventory': []}
        """
        # TODO: Ask the user for their name using input()
        name = input("Enter your name: ")

        # TODO: Initialize a dictionary with keys: "name", "health", and "inventory"
        player = {
           # "name": name,
           # "health": 10,
           # "inventory": []
        }

        # TODO: Return the dictionary
        return {
            "name": name,
            "health": 10,
            "inventory": []
        }
    # Test the setup_player function
    print(setup_player())

    def create_treasures():
        """
        Creates a dictionary of treasures, where each treasure has a value.

        Returns:
            dict: Example:
                {
                    "gold coin": 5,
                    "ruby": 10,
                    "ancient scroll": 7,
                    "emerald": 9,
                    "silver ring": 4
                }
        Tip:
            You can customize treasures or randomize the values using random.randint(3, 12).
        """
        # TODO: Create a dictionary of treasure names and integer values
        # TODO: Return the dictionary

        return {
            "gold coin": random.randint(3, 12),
            "ruby": random.randint(3, 12),
            "ancient scroll": random.randint(3, 12),
            "emerald": random.randint(3, 12),
            "silver ring": random.randint(3, 12)
        }

    #Test the create_treasures function
    #print(create_treasures())

    def display_options(room_number):
        """
        Displays available options for the player in the current room.

        Args:
            room_number (int): The current room number.

        Output Example:
            You are in room 3.
            What would you like to do?
            1. Search for treasure
            2. Move to next room
            3. Check health and inventory
            4. Quit the game
        """
        # TODO: Print the room number and the 4 menu options listed above
    def display_options(room_number):
        print(f"\n--- Room {room_number} ---")
        print("Choose an action:")
        print("1. Search for treasure")
        print("2. Move to next room")
        print("3. Check health and inventory")
        print("4. Quit game")

    def search_room(player, treasures):

        # TODO: Randomly assign outcome = random.choice(["treasure", "trap"])
        outcome = random.choice(["treasure", "trap"])


        # TODO: Write an if/else to handle treasure vs trap outcomes
        # TODO: Print a warning
        # TODO: Update player dictionary accordingly
        # TODO: Print messages describing what happened
        
        if outcome == "treasure":
            treasure = random.choice(list(treasures.keys()))
            player["inventory"].append(treasure)
            print(f"You found a {treasure}! It has been added to your inventory.")
        else:
            damage = random.randint(5, 20)
            player["health"] -= damage
            print(f"You triggered a trap! Your health is now {player['health']}.")

            #print(f"Your health is now {player['health']}.")

    def check_status(player):
        """
        Displays the player’s current health and inventory.

        Args:
            player (dict): Player stats including health and inventory.

        Example Output:
            Health: 8
            Inventory: ruby, gold coin
        or:
            Health: 10
            Inventory: You have no items yet.
        """
        # TODO: Print player health
        # TODO: If the inventory list is not empty, print items joined by commas
        # TODO: Otherwise print “You have no items yet.”
        
        print(f"\nHealth: {player['health']}")
        if player["inventory"]:
            print("Inventory:")
            for item in player["inventory"]:
                print(f" - {item}")
        else:
            print("You have no items yet.")



    def end_game(player, treasures):
        """
        Ends the game and displays a summary.

        Args:
            player (dict): Player stats.
            treasures (dict): Treasure dictionary for item value lookup.

        Output:
            Prints player’s final health, inventory contents, and total score value.
        """
        # TODO: Calculate total score by summing the value of collected treasures
        # TODO: Print final health, items, and total value
        # TODO: End with a message like "Game Over! Thanks for playing."

        print(f"Final Health: {player['health']}")

        if player["inventory"]:
            print("Treasures Collected:")
            total_value = 0
            for item in player["inventory"]:
                print(f" - {item} (worth {treasures[item]})")
                total_value += treasures[item]
            print(f"Total Treasure Value: {total_value}")
        else:
            print("You collected no treasures.")

        print("Thanks for playing Dungeon Adventure!")
        print("\n=== GAME OVER ===")




    def run_game_loop(player, treasures):
        """
        Main game loop that manages the rooms and player decisions.

        Args:
            player (dict): Player stats.
            treasures (dict): Treasure dictionary.

        Flow:
            - There are 5 rooms (use for loop range(1, 6))
            - Inside each room, use a while loop for player actions:
                1. Search room
                2. Move to next room
                3. Check status
                4. Quit
            - Health below 1 ends the game early.
        """
        # TODO: Loop through 5 rooms (1–5)
        # TODO: Inside each room, prompt player choice using input()
        # TODO: Use if/elif to handle each choice (1–4)
        # TODO: Break or return appropriately when player quits or dies
        # TODO: Call end_game() after all rooms are explored

        room = 1
        total_rooms = 5

        while room <= total_rooms and player["health"] > 0:
            display_options(room)
            choice = input("Enter your choice: ")

            if choice == "1":
                search_room(player, treasures)

            elif choice == "2":
                print("You cautiously move forward...")
                room += 1

            elif choice == "3":
                check_status(player)

            elif choice == "4":
                print("\nYou chose to leave the dungeon early.")
                break

            else:
                print("Invalid choice. Try again.")

        else:
            print("Invalid choice. Try again.")

        end_game(player, treasures)



    # -----------------------------------------------------
    # GAME ENTRY POINT (Leave this section unchanged)
    # -----------------------------------------------------
    player = setup_player()
    treasures = create_treasures()
    run_game_loop(player, treasures)

if __name__ == "__main__":
    main()
