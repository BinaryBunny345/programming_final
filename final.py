# CD, AP, JA, GB, Build a Game 
# #print("Start")

print("Welcome to Being a Ferret 101!!")

# GB, making question for information about player
player_name = input("What is your name?: ")

def ferret():
    # AP, starting of the story, telling the player their goal, the story, and instructions.
    print(f"Once upon a time, there was this really STUPID ferret named {player_name}, who loved walking through doors to different time stamps. This ferret {player_name} accidently got trapped in the 1800s because {player_name} wanted to see the signing of the Declaration Of Independence. Unfortunately, {player_name} doesn't have their history straight and didn't go to August 2nd, 1776, because they're STUPID. Just kidding. We love you. Good luck!!\nThou awakest within a most exceedingly antiquated chamber, most peculiar in fashion, as though plucked straight from the nineteenth century—wink, wink. Before thee stands a door. With great curiosity, thou dost approach and attempt to open it, only to discover that the blasted thing is firmly locked. OH, DEAR! Whatever, pray tell, shallst thou do now?!?\n")

    # JA, Variable for the first room/era
print("Upon entering the ancient house, thou art greeted by a humble room, its walls adorned with simple decorations and aged portraits. The wooden floors creak beneath thy feet, and the air is thick with the scent of old wood and parchment. At the very center of the room hangs the Declaration of Independence, proudly displayed as though it were a treasure of the highest importance. Gathered around it stand a company of distinguished gentlemen, dressed in fine coats, powdered wigs, and polished shoes. They speak amongst themselves in hushed, serious tones, their faces bearing the solemn expressions of men burdened with great responsibility. The room may lack grand riches and extravagant furnishings, yet it carries an air of history and importance, as though the very walls have witnessed the birth of a new nation.\n You push open the door and tumble directly into Independence Hall in the 1800s. The room is filled with polished wooden furniture, serious-looking gentlemen, and enough historical documents to give a librarian a heart attack. At the center of the room, displayed proudly on a pedestal, sits the DECLARATION OF INDEPENDENCE. It is surrounded by guards who look like they haven't smiled since the invention of the wheel. Your whiskers twitch. Your nose wiggles. Your three brain cells hold a meeting. One says, 'That looks important.'' Another says, 'That looks chewable.'The third has decided that the pedestal would make an excellent place for a nap. Your mission is to steal the Declaration without getting caught. Unfortunately, you are a ferret approximately the size of a loaf of bread, and you have the subtlety of a falling piano.\n")

Question1 = input("What do you want to do in the room. You can; sit still(Sit), search the room more thoroughly(Search), to run and try to snatch it from under them(Run): \n")
if Question1 == "Sit":
        print("You decide that standing perfectly still is an excellent strategy. You sit. You blink. You inspect your tail. Five minutes pass. Then ten. A guard finally notices the suspiciously furry object sitting in the middle of Independence Hall.'WHAT IS THAT THING?' he shouts. You puff up your fur and hiss. The guards surround you before you can perform your emergency escape wiggle.\n GAME OVER! You have been arrested for suspicious loaf-shaped behavior. Even the founding fathers are disappointed in you.")
        input(Question1)
if Question1 == "Search":
        print("You lower your body to the floor and begin investigating. Your tiny paws make almost no sound as you sneak beneath a wooden table. You spot two guards chatting near the pedestal. One complains about his aching feet. The other complains about his boring job. You have discovered their weakness: they are incredibly distracted. Unfortunately, your investigation is interrupted when you find a shiny button on the floor. You grab it in your teeth. It belongs to one of the guards. Oops.")
if Question1 == "Run":
    print("You launch yourself toward the pedestal at maximum ferret speed. Unfortunately, maximum ferret speed is not the same thing as maximum intelligence. You skid across the polished floor, crash into a chair, and send a stack of papers flying into the air. Every guard turns toward you at once. 'INTRUDER!' someone shouts. You attempt to hide behind a candlestick. It is not nearly large enough to hide a ferret.\nGAME OVER! You have officially made the worst first impression in American history.")
    
    # GB, Room Two, 1900s
def grandma():
    print("You tumble through the door and end up in an apartment, with antiques scattering the area and intricately patterned couches. It seems like a grandma owns this place, unsuprisingly")
    print("Goal: steal grandma's dentures from the counter")
    print("In the corner of your eye, you see a glimmer of saliva. On top of the counter, is GRANDMA'S DENTURES. You HAVE to steal them in order to progress. You begin creeping towards thye counter")
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
            print("Grandma: That's nice. I have dementia so I've forgotten everything you've said. Wait... why are you IN MY HOUSE.")
            granny_answer3 = input("Answer grandma: (1) To steal your dentures, remember? (2) No reason unc, I already told you")
            print("Grandma: GET OUT OF MY HOUSE!!!")
            print(f"{player_name}: APARTMENT, not house. lol...ok why are you chasing me. Somebody's mad")
            # function chase scene thing
    elif granny_choice1 == 3:
            print("alice")


   


    # AP, Room Four, 3000s
def future ():
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

scores_for_end_of_game.txt = ""

score = 0
has_declaration = False
has_dentures = False
has_lollypop = False
has_jetpack = False
has_declaration_wrong = False
stats_filename = "stats.txt"

if not os.path.exists(stats_filename):
        (0,0)

hangman_record = ""

with open(stats_filename, "r") as file:
        hangman_record = file.read()
        
hangman_scores = scores_for_end_of_game.split(",")