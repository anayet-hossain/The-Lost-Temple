
def game_over():
    print("Game Over. Thanks for playing!")
    replay = input("Do you want to play again? (yes/no)").lower()
    if replay == "yes":
        start_game()
    else:
        print("Goodbye!")

def start_game():
    name = input("Hello, Player. What may I call you?").capitalize()
    print(f"Hello, {name}. Welcome to the Game. This is a story-based adventure game. In this game, you will be inside a story and you will be given certain choices to continue the story, and the story will continue based on your choice. Good Luck, {name}.")

    print("The Lost Temple")
    choice_1 = input("You find an ancient, dusty map hidden in the attic of your late grandfather's house. The map depicts a dense jungle with a red 'X' marked at its center, along with the words 'The Lost Temple of Zephyrus' scrawled in the margins. Here, you have 2 choices. 1. Follow the map and set out on an adventure to find the Lost Temple (Type follow) or 2. Ignore the map and continue exploring the attic (Type ignore)").lower()

    if choice_1 == "follow":
        choice_2 = input("You pack your gear and set off on a journey deep into the jungle. After days of trekking through thick vines and battling swarms of insects, you come to a fork in the path. One trail looks well-trodden and safe, while the other is overgrown and dark, with strange noises emanating from within. Here, You have 2 choices. 1. Take the well-trodden path (Type path) or 2. Venture down the dark, overgrown trail (Type trail)").lower()
        if choice_2 == "path":
            choice_3 = input("You take the safe path and eventually arrive at a tranquil river with crystal-clear water. There's a rickety old bridge crossing the river, but it doesn't look sturdy. You notice an old raft nearby, half-submerged in the water. Here, you have 2 choices. 1. Cross the river using the bridge (Type bridge) or 2. Repair the raft and use it to cross the river (Type repair).").lower()
            if choice_3 == "bridge":
                choice_4 = input("You decide to cross the river using the rickety bridge. As you carefully step onto the first plank, the wood creaks ominously. Halfway across, the bridge begins to sway violently. Here, you have 2 choices. 1. Sprint to the other side as fast as you can (Type sprint) or 2. Drop down and cling to the bridge ropes until it stabilizes (Type cling).").lower()
                if choice_4 == "sprint":
                    choice_5 = input("You sprint across the collapsing bridge, barely making it to the other side as the last plank falls into the river below. Beyond the river, you find a hidden grove filled with ancient statues and a stone altar at its center. The map shows that this is the final destination. Here, you have 2 choices. 1. Place the map on the altar and complete the ritual (Type ritual) or 2. Search the grove for hidden treasures before performing the ritual (Type search).").lower()
                    if choice_5 == "ritual":
                        print("Victory Ending: You successfully unlock the secrets of the Lost Temple, finding treasure or hidden knowledge.")
                        game_over()
                    elif choice_5 == "search":
                        print("Victory Ending: You successfully unlock the secrets of the Lost Temple, finding treasure or hidden knowledge.")
                        game_over()
                    else:
                        print("Sorry, this is an invalid input.")
                        game_over()
                elif choice_4 == "cling":
                    choice_5 = input("You cling to the ropes until the bridge stabilizes, but as you reach the other side, you hear a soft voice calling from the river. A spirit rises from the water, thanking you for your bravery and offering you a choice: gain a powerful artifact or ask a question about your journey. Here, you have 2 choices. 1. Accept the artifact and end your journey (Type accept) or 2. Ask the spirit a question about the Lost Temple (Type ask). ").lower()
                    if choice_5 == "accept":
                        print("Victory Ending: You successfully unlock the secrets of the Lost Temple, finding treasure or hidden knowledge.")
                        game_over()
                    elif choice_5 == "ask":
                        print("Wisdom Ending: Choosing knowledge or understanding over immediate rewards or power.")
                        game_over()
                    else:
                        print("Sorry, this is an invalid input.")
                        game_over()
                else:
                    print("Sorry, this is an invalid input.")
                    game_over()
            elif choice_3 == "repair":
                choice_4 = input("You repair the raft and begin to paddle across the river. Halfway through, the water beneath you starts to ripple, and a massive serpent emerges, its scales glistening in the sunlight. Here, you have 2 choices. 1. Use your paddle to fight off the serpent (Type fight) or 2. Abandon the raft and swim to shore (Type swim).").lower()
                if choice_4 == "fight":
                    choice_5 = input("You bravely fight off the serpent with your paddle, eventually scaring it away. As it retreats, you notice a glittering object in the water where it had emerged. It's a golden key with the same symbol as the one on the map. Here, you have 2 choices. 1. Take the key and continue to the temple (Type take) or 2. Use the key to unlock a hidden compartment in your raft (Type hidden).").lower()
                    if choice_5 == "take":
                        print("Victory Ending: You successfully unlock the secrets of the Lost Temple, finding treasure or hidden knowledge.")
                        game_over()
                    elif choice_5 == "hidden":
                        print("Survival Ending: Escaping from danger or completing the adventure without necessarily uncovering all secrets.")
                        game_over()
                    else:
                        print("Sorry, this is an invalid input.")
                        game_over()
                elif choice_4 == "swim":
                    choice_5 = input("You swim to shore, leaving the raft and serpent behind. As you drag yourself onto the land, you find yourself on a hidden shore with a large stone door embedded in a cliff. The keyhole on the door matches the symbol on the map. Here, you have 2 choices. 1. Enter the door and discover the temple's secret (Type discover) or 2. Explore the shore for clues before entering (Type shore).").lower()
                    if choice_5 == "discover":
                        print("Victory Ending: You successfully unlock the secrets of the Lost Temple, finding treasure or hidden knowledge.")
                        game_over()
                    elif choice_5 == "shore":
                        print("Wisdom Ending: Choosing knowledge or understanding over immediate rewards or power.")
                        game_over()
                    else:
                        print("Sorry, this is an invalid input.")
                        game_over()
                else:
                    print("Sorry, this is an invalid input.")
                    game_over()
            else:
                print("Sorry, this is an invalid input.")
                game_over()
        elif choice_2 == "trail":
            choice_3 = input("You venture down the dark trail and soon come upon the entrance to a cave. The howls and eerie whispers from within send shivers down your spine. At the cave entrance, you find a torch and a rusty sword. Here, You have 2 choices. 1. Light the torch and enter the cave (Type torch) or 2. Arm yourself with the sword and proceed cautiously (Type arm).").lower()
            if choice_3 == "torch":
                choice_4 = input("Torch in hand, you enter the cave. The light flickers, casting eerie shadows on the walls. Deeper inside, you encounter a group of shadowy figures guarding a stone door, their eyes glowing red in the darkness. Here, you have 2 choices. 1. Use the torch to ward off the shadowy figures (Type ward) or 2. Try to sneak past the figures without being noticed (Type sneak).").lower()
                if choice_4 == "ward":
                    choice_5 = input("You use the torch to ward off the shadowy figures, but as you approach the stone door, a final guardian appears, a towering figure made of shadows. It challenges you to a riddle, promising passage if you solve it. Here, you have 2 choices. 1. Solve the riddle and pass through the door (Type solve) or 2. Fight the guardian with your torch (Type fight).").lower()
                    if choice_5 == "solve":
                        print("Victory Ending: You successfully unlock the secrets of the Lost Temple, finding treasure or hidden knowledge.")
                        game_over()
                    elif choice_5 == "fight":
                        print("Power Ending: Gaining power or dominance through strength or combat.")
                        game_over()
                    else:
                        print("Sorry, this is an invalid input.")
                        game_over()
                elif choice_4 == "sneak":
                    choice_5 = input("You sneak past the shadowy figures, reaching the stone door unnoticed. The map shows a combination of symbols needed to open it. Here, you have 2 choices. 1. Solve the combination and open the door (Type open) or 2. Search for clues on the door before attempting to open it (Type clues).").lower()
                    if choice_5 == "open":
                        print("Victory Ending: You successfully unlock the secrets of the Lost Temple, finding treasure or hidden knowledge.")
                        game_over()
                    elif choice_5 == "clues":
                        print("Wisdom Ending: Choosing knowledge or understanding over immediate rewards or power.")
                        game_over()
                    else:
                        print("Sorry, this is an invalid input.")
                        game_over()
                else:
                    print("Sorry, this is an invalid input.")
                    game_over()
            elif choice_3 == "arm":
                choice_4 = input("Armed with the rusty sword, you proceed into the cave, ready to face whatever dangers lurk within. Deeper inside, you encounter a group of shadowy figures guarding a stone door, their eyes glowing red in the darkness. Here, you have 2 choices. 1. Charge at the figures with the sword (Type charge) or 2. Wait and observe them before taking action (Type observe).").lower()
                if choice_4 == "charge":
                    choice_5 = input("You charge at the shadowy figures, and they dissolve into mist as your sword passes through them. Beyond the stone door, you find the temple's inner sanctum, filled with ancient relics. Here, you have 2 choices. 1. Take the relics and leave the temple (Type relics) or 2. Study the relics and uncover their true purpose (Type study).").lower()
                    if choice_5 == "relics":
                        print("Power Ending: Gaining power or dominance through strength or combat.")
                        game_over()
                    elif choice_5 == "study":
                        print("Wisdom Ending: Choosing knowledge or understanding over immediate rewards or power.")
                        game_over()
                    else:
                        print("Sorry, this is an invalid input.")
                        game_over()
                elif choice_4 == "observe":
                    choice_5 = input("You observe the shadowy figures, realizing they are an illusion meant to scare intruders away. You find the mechanism to dispel the illusion and open the stone door. Beyond it lies the Lost Temple's treasure chamber. Here, you have 2 choices. 1. Take the treasure and leave the temple (Type treasure) or 2. Explore the chamber for hidden secrets before leaving (Type explore).").lower()
                    if choice_5 == "treasure":
                        print("Victory Ending: You successfully unlock the secrets of the Lost Temple, finding treasure or hidden knowledge.")
                        game_over()
                    elif choice_5 == "explore":
                        print("Wisdom Ending: Choosing knowledge or understanding over immediate rewards or power.")
                        game_over()
                    else:
                        print("Sorry, this is an invalid input.")
                        game_over()
                else:
                    print("Sorry, this is an invalid input.")
                    game_over()
            else:
                print("Sorry, this is an invalid input.")
                game_over()
        else:
            print("Sorry, this is an invalid input.")
            game_over()
    elif choice_1 == "ignore":
        choice_2 = input("You decide to ignore the map and continue exploring the attic. As you dig through old boxes, you come across a dusty journal filled with sketches and notes about strange creatures and ancient rituals. Here, you have 2 choices. 1. Read the journal and uncover its secrets (Type read) or 2. Set the journal aside and continue searching the attic (Type search).").lower()
        if choice_2 == "read":
            choice_3 = input("You read the journal and learn about a hidden portal to another world located somewhere in the attic. The journal hints at a ritual to open the portal. Here, you have 2 choices. 1. Perform the ritual and open the portal (Type ritual) or 2. Close the journal and forget about the portal (Type forget).").lower()
            if choice_3 == "ritual":
                choice_4 = input("You perform the ritual, and the attic starts to shake as a glowing portal appears before you. On the other side, you see a world unlike anything you've ever known. Here, you have 2 choices. 1. Step through the portal and explore the new world (Type step) or 2. Close the portal and keep the knowledge to yourself (Type close).").lower()
                if choice_4 == "step":
                    print("Victory Ending: You successfully unlock the secrets of the Lost Temple, finding treasure or hidden knowledge.")
                    game_over()
                elif choice_4 == "close":
                    print("Wisdom Ending: Choosing knowledge or understanding over immediate rewards or power.")
                    game_over()
                else:
                    print("Sorry, this is an invalid input.")
                    game_over()
            elif choice_3 == "forget":
                print("Neutral Ending: Ending the adventure without significant achievements or failures.")
                game_over()
            else:
                print("Sorry, this is an invalid input.")
                game_over()
        elif choice_2 == "search":
            choice_3 = input("As you continue searching the attic, you find a hidden compartment under the floorboards. Inside, there's a strange, ancient tablet covered in indecipherable symbols. Here, you have 2 choices. 1. Take the tablet and decipher its message (Type decipher) or 2. Leave the tablet and continue searching (Type leave).").lower()
            if choice_3 == "decipher":
                choice_4 = input("You take the tablet and, after hours of research, decipher its message. It reveals the location of the Lost Temple, with instructions to find a secret artifact hidden within. Here, you have 2 choices. 1. Follow the tablet's instructions and find the artifact (Type artifact) or 2. Keep the tablet's secret to yourself and continue with your life (Type life).").lower()
                if choice_4 == "artifact":
                    print("Victory Ending: You successfully unlock the secrets of the Lost Temple, finding treasure or hidden knowledge.")
                    game_over()
                elif choice_4 == "life":
                    print("Wisdom Ending: Choosing knowledge or understanding over immediate rewards or power.")
                    game_over()
                else:
                    print("Sorry, this is an invalid input.")
                    game_over()
            elif choice_3 == "leave":
                print("Neutral Ending: Ending the adventure without significant achievements or failures.")
                game_over()
            else:
                print("Sorry, this is an invalid input.")
                game_over()
        else:
            print("Sorry, this is an invalid input.")
            game_over()
    else:
        print("Sorry, this is an invalid input.")
        game_over()

start_game()
