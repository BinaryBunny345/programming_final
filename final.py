# CD, AP, JA, GB, Build a Game

#print("Start")
print("Welcome to Being a Ferret 101!!")


# GB, making question for information about player
player_name = input("What is your name?:")


# AP, starting of the story, telling the player their goal, the story, and instructions.
print(f"Once upon a time, there was this really STUPID ferret named {player_name}, who loved walking through doors to different time stamps. This ferret {player_name} accidently got trapped in the 1800s because {player_name} wanted to see the signing of the Declaration Of Independence. Unfortunately, {player_name} doesn't have their history straight and didn't go to August 2nd, 1776, because they're STUPID. Just kidding. We love you. Good luck!!\nThou awakest within a most exceedingly antiquated chamber, most peculiar in fashion, as though plucked straight from the nineteenth century—wink, wink. Before thee stands a door. With great curiosity, thou dost approach and attempt to open it, only to discover that the blasted thing is firmly locked. OH, DEAR! Whatever, pray tell, shallst thou do now?!?\n")

def era_2000():
        print("Welcome to the 2000s room!\n")
        print("Welcome to the You hear enter a room that has blue stripes on the walls and a small white crib by a window letting light stream through. A baby lays on it's stomach along with a little lollypop laying not far from their face. Your goal is to get that sugary little treat before the gremlin eats it all up!\n")
        print("Do you want to:\n (bolt) for the lollypop\n(wait) for the baby to waltz away\n(persuade) the baby to give you the candy?\nPlease type your answer in (parentheses):")
choice_one_room_2000 = input()


# JA, Variable for the first room/era
print("Upon entering the ancient house, thou art greeted by a humble room, its walls adorned with simple decorations and aged portraits. The wooden floors creak beneath thy feet, and the air is thick with the scent of old wood and parchment. At the very center of the room hangs the Declaration of Independence, proudly displayed as though it were a treasure of the highest importance. Gathered around it stand a company of distinguished gentlemen, dressed in fine coats, powdered wigs, and polished shoes. They speak amongst themselves in hushed, serious tones, their faces bearing the solemn expressions of men burdened with great responsibility. The room may lack grand riches and extravagant furnishings, yet it carries an air of history and importance, as though the very walls have witnessed the birth of a new nation.\n ")
Question1 = input("What do you want to do in the room. You can; sit still(1), or search the room more thoroughly(2):")
if Question1 == "1":
    print("You wait for 3 hours before nothing happens\n")
    input(Question1)
if Question1 == "2":
    print("You search around the room, uprooting coushions and throwing lamps, till you find a key in a desk drawer you go to the door and insert the key")
print("when you open the door it opens up into a big room, marble colums grew up at the corners. In front of you there is a door threshold\n ")
Question2 = input("What do you want to do in the room. You can; sit still(1), or peek out of the room(2):\n ")
if Question2 == "1":
    print("You wait for 3 hours before a 2 armed gaurds comes into the room. You got caught")
playagian = input("\nYou had {_}/4 of the Item's. Do you want to play again (Y/N):\n ").strip().lower()
if playagain != "y":
    print("thanks for playing")



# GB, Room Two, 1900s
print('You end up in an apartment, with antiques scattering the area and intricately patterned couches. It seems like a grandma owns this place.')
print("Goal: steal grandma's dentures from the counter")
print("You can: Quickly try and grab the dentures (1), wait (2), or search the apartment (3)")
            
granny_choice1 = input("What would you like to do?:").strip()
if granny_choice1 == 1:
    print("You squrry across the floor, before a person appears in front of you out of nowhere. The person grabs you, and as you oberve their face, you realize it's the grandma!")
    print("Before you can react, she takes you to her open window and throws you out, leaving you stuck here forever.")
elif granny_choice1 == 2:
    print("You wait for hours, and about to collapse from exhaustion, when a person comes up to you. They talk like a grandma.")
    print("Grandma: Hello.. Excuse me, who are you?")
    granny_answer1 = input("Answer grandma: (1) I'm a ferret (2) I'm your husband")
    print("Grandma: That's lovely. I remember when my children would visit, they don't anymore though. Anyways, why are you here?")
    granny_answer2 = input("Answer grandma: (1) To steal your dentures lol (2) No reason")
    print("um")
    granny_answer3 = input("Answer grandma: (1) (2)")
elif granny_choice1 == 3:
    print("alice")


# CD, Room Three, 2000s
    def era_2000():
        print("Welcome to the 2000s room!\n")
        print("Welcome to the You hear enter a room that has blue stripes on the walls and a small white crib by a window letting light stream through. A baby lays on it's stomach along with a little lollypop laying not far from their face. Your goal is to get that sugary little treat before the gremlin eats it all up!\n")
        print("Do you want to:\n (bolt) for the lollypop\n(wait) for the baby to waltz away\n(persuade) the baby to give you the candy?\nPlease type your answer in (parentheses):")
    choice_one_room_2000 = input()


# AP, Room Four, 3000s
print("You now enter a room that looks future-like. You take a look around the room and see a calendar on the wall. It is currently June 9th, 3004, and it sure looks like it. You look at the walls and there is a picture of a really old dude with a jetpack next to it. This has got to be Elon Musk's great grand son.")
print("Goal: steal a jetpack hanging on the wall.")
print("What would you like to do?")
future_choice1 = input("You can: Quickly try and grab the jetpack and run (1), wait (2), or search the room (3)")
if future_choice1 == "2":
    print("You wait for 30 minutes and your leg falls asleep (Choose again)")
    input(future_choice1)
if future_choice1 == "3":
    print("You search around the room, find a penny from 2996, and put it in your pocket. You later try to open the door across from you, and notice its locked. You have to find the hidden object un the room to unlock it. GO!")
if future_choice1 == "1":
    print("You grab the jetpack off of the wall, and a shiny object falls out.")
future_choice2 = input("Do you want to pick it up? Yes or no?:")
if future_choice2 == "Yes":
    print("You pick it up and notice its a key. The key has five grooves on the bottom, and it looks made for someone specifically. ")
else:
    print("You leave the shinny object and your tail his the on botton of the jetpack, I know very inconveinent, and you fly thorught the rich guys roof and fly into the clouds for forever.\nYou lost! You had {_}/4 items. Would you like to play again? (yes) or (no)")


# CD, final scorings

score = 0
has_declaration = False
has_dentures = False
has_lollypop = False
has_jetpack = False
has_declaration_wrong = False