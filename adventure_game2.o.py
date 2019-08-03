import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        else:
            print_pause("Sorry I don't understand.")
    return response


def intro():
    print_pause("You awake in the center of a small town in the"
                " Pacific Northwest.")
    print_pause("You are a monster hunter by"
                " profession.")
    print_pause("You were contacted by a group of concerned citizens"
                " regarding the mysterious disappearance of townspeople.")
    print_pause("The last thing you remember is driving into town.")
    print_pause("Standing up and looking around, you realize"
                " your car and all your gear are nowhere in sight.")
    print_pause("Taking a quick inventory of your pockets you"
                " come to the sobering conclusion that the only"
                " weapon you have is a small pocket knife.")
    print_pause("Hardly enough to tackle any serious threat.")
    1


def park(items):
    print_pause("Across the street, you see a small park.")
    if "stake" in items:
        print_pause(" There is nothing else you can do here.")
    else:
        print_pause("You go over and carve yourself a good, strong stake"
                    " using your pocket knife.")
        print_pause("You feel better knowing you have a weapon in"
                    " in case you run into trouble before you find"
                    " your gear.")
        items.append("stake")
    print_pause("You head back to the street.")
    main_street(items)


def pawn_shop(items):
    print_pause("Next to town hall you see a pawn shop.")
    print_pause("You go inside.")
    print_pause("It is as empty as the rest of the town.")
    print_pause("You begin looking around for something"
                " that will work as a weapon.")
    if "knife" in items:
        print_pause("There are no more weapons here.")
    else:
        print_pause("Unfortunately there are no guns"
                    " but you do find a large carving knife"
                    " that appears to be silver.")
        items.append("knife")
    print_pause("You head back to the street.")
    main_street(items)


def random_monster():
    monster_list = ["vampire", "werewolf"]
    random.choice([monster_list])


def town_hall(items):
    print_pause("You cross the street towards the town hall.")
    print_pause("You enter through the front doors, and"
                " follow the sign for the mayors office.")
    print_pause("Maybe there will be a clue regarding the"
                " missing town people.")
    print_pause("You open the door and are confronted by"
                " a dark shape.")
    monster = random.choice(["vampire", "werewolf"])

    if monster == "vampire":
        if "stake" in items:
            print_pause("The vampire gives a chilling laugh"
                        " and leaps at you.")
            print_pause("You bring up the stake, and as the"
                        " the vampire falls on you he is impaled"
                        " through the chest and lies still.")
            print_pause("On his body you find a note from an"
                        " accomplice stating the townspeople have"
                        " all been gathered at the old iron works"
                        " outside of town.")
            print_pause("You head there and find the missing townspeople"
                        " , your car and all your gear.")
            print_pause("You are victorious!")
            play_again()
        else:
            print_pause("The vampire gives a chilling laugh"
                        " and leaps at you.")
            print_pause("You have no weapon that is effective"
                        " against a vampire and he quickly over"
                        "comes you.")
            print_pause("Your vision grows dim as you feel the blood"
                        " leaving your body.")
            play_again()
    elif monster == "werewolf":
        if "knife" in items:
            print_pause("The werewolf gives a bloodcurdling howl"
                        " and charges you.")
            print_pause("You bring up the knife and run it through"
                        " his chest as he leaps at you.")
            print_pause("On his body you find a note from an"
                        " accomplice stating the townspeople have"
                        " all been gathered at the old iron works"
                        " outside of town.")
            print_pause("You head there and find the missing townspeople"
                        " , your car and all your gear.")
            print_pause("You are victorious!")
            play_again()
        else:
            print_pause("The werewolf gives a bloodcurdling howl"
                        " and charges you.")
            print_pause("You have no weapon that is effective"
                        " against a werewolf and he quickly over"
                        " comes you.")
            print_pause("Your vision grows dim as you feel the blood"
                        " leaving your body.")
            play_again()


def main_street(items):
    print_pause("Looking around you see a park, a pawn shop, and the town"
                " hall.")
    print_pause("Where would you like to go?")
    choice = input("1. Park\n"
                   "2. Pawn Shop\n"
                   "3. Town Hall\n")
    if choice == '1':
        park(items)
    elif choice == '2':
        pawn_shop(items)
    elif choice == '3':
        town_hall(items)
    else:
        print_pause("Sorry, I don't understand.")


def play_game():
    items = []
    intro()
    main_street(items)


def play_again():
    response = valid_input("Would you like to play again?\n"
                           "Please say 'yes' or 'no'.\n",
                           "yes", "no")
    if "no" in response:
        print_pause("Goodbye, Thank you for playing!")
    elif "yes" in response:
        print_pause("Very well...")
        play_game()


        
play_game()
