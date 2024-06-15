def commands():
    print("-------------------------------------")
    print("Commands:go [directions],get [item],quit")


def show_status(room, inventory):
    print("-------------------------------------")
    print(f"current_room :: {room['name']}")
    print(f"Inventory :: {inventory}")
    if "item" in room:
        print(f"{room['item']} found in room!!")


def playgame(room):
    current_room = room["hall"]
    inventory = []
    commands()

    while True:

        show_status(current_room, inventory)

        if current_room["name"] == "garden" and "key" in inventory and "potion" in inventory:
            print("*************************************")
            print("YOU WON THE GAME!!!!!")
            break

        if "item" in current_room and current_room["item"] == "monster":

            if "key" in inventory and "potion" in inventory:
                print("*************************************")
                print("You Defeted the Monster\nYOU WON THE GAME!!!!!")
                break

            else:
                print("*************************************")
                print("You got caught by the Monster!!!!!")
                break

        move = input("::").lower().split()

        if move[0] != "go" and move[0] != "get" and move[0] != "quit":
            print("-------------------------------------")
            print("INVALID INPUT!!!")

        if move[0] == "quit":
            print("-------------------------------------")
            print("you quit the game!!!")
            break

        elif move[0] == "get":

            if "item" in current_room and move[1] == current_room["item"]:
                inventory.append(current_room["item"])
                print("-------------------------------------")
                print("item added to inventory!")
                del current_room["item"]

            else:
                print("-------------------------------------")
                print("cannot add the item!!!")

        elif move[0] == "go":

            if move[1] in current_room:
                current_room = room[current_room[move[1]]]

            else:
                print("-------------------------------------")
                print("Cannot go that way!!!")


room = {
    "hall": {"name": "hall", "south": "kitchen", "east": "dining room", "item": "key"},
    "kitchen": {"name": "kitchen", "north": "hall", "item": "monster"},
    "dining room": {"name": "dining room", "west": "hall", "south": "garden", "item": "potion"},
    "garden": {"name": "garden", "north": "dining room"}
}

playgame(room)
