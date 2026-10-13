# CD, AP, JA, GB, Build a Game 
# #print("Start")

import os.path


print("Welcome to Being a Ferret 101!!")

# GB, making question for information about player
player_name = input("What is your name?: ")

# AP, starting of the story, telling the player their goal, the story, and instructions.
print(f"Once upon a time, there was this really STUPID ferret named {player_name}, who loved walking through doors to different time stamps. This ferret {player_name} accidently got trapped in the 1800s because {player_name} wanted to see the signing of the Declaration Of Independence. Unfortunately, {player_name} doesn't have their history straight and didn't go to August 2nd, 1776, because they're STUPID. Just kidding. We love you. Good luck!!\nThou awakest within a most exceedingly antiquated chamber, most peculiar in fashion, as though plucked straight from the nineteenth century—wink, wink. Before thee stands a door. With great curiosity, thou dost approach and attempt to open it, only to discover that the blasted thing is firmly locked. OH, DEAR! Whatever, pray tell, shallst thou do now?!?\n")

def first(player_name):
    # JA, Variable for the first room/era
    print("Upon entering the ancient house, thou art greeted by a humble room, its walls adorned with simple decorations and aged portraits. The wooden floors creak beneath thy feet, and the air is thick with the scent of old wood and parchment. At the very center of the room hangs the Declaration of Independence, proudly displayed as though it were a treasure of the highest importance. Gathered around it stand a company of distinguished gentlemen, dressed in fine coats, powdered wigs, and polished shoes. They speak amongst themselves in hushed, serious tones, their faces bearing the solemn expressions of men burdened with great responsibility. The room may lack grand riches and extravagant furnishings, yet it carries an air of history and importance, as though the very walls have witnessed the birth of a new nation.\n You push open the door and tumble directly into Independence Hall in the 1800s. The room is filled with polished wooden furniture, serious-looking gentlemen, and enough historical documents to give a librarian a heart attack. At the center of the room, displayed proudly on a pedestal, sits the DECLARATION OF INDEPENDENCE. It is surrounded by guards who look like they haven't smiled since the invention of the wheel. Your whiskers twitch. Your nose wiggles. Your three brain cells hold a meeting. One says, 'That looks important.'' Another says, 'That looks chewable.'The third has decided that the pedestal would make an excellent place for a nap. Your mission is to steal the Declaration without getting caught. Unfortunately, you are a ferret approximately the size of a loaf of bread, and you have the subtlety of a falling piano.\n")

    Question1 = input("What do you want to do in the room. You can: sit still(Sit), search the room more thoroughly(Search), to run and try to snatch it from under them(Run): \n").strip().lower()

    if Question1 == "sit":
        print("You decide that standing perfectly still is an excellent strategy. You sit. You blink. You inspect your tail. Five minutes pass. Then ten. A guard finally notices the suspiciously furry object sitting in the middle of Independence Hall.'WHAT IS THAT THING?' he shouts. You puff up your fur and hiss. The guards surround you before you can perform your emergency escape wiggle.\n GAME OVER! You have been arrested for suspicious loaf-shaped behavior. Even the founding fathers are disappointed in you.")
        return False
    if Question1 == "search":
        print("You lower your body to the floor and begin investigating. Your tiny paws make almost no sound as you sneak beneath a wooden table. You spot two guards chatting near the pedestal. One complains about his aching feet. The other complains about his boring job. You have discovered their weakness: they are incredibly distracted. Unfortunately, your investigation is interrupted when you find a shiny button on the floor. You grab it in your teeth. It belongs to one of the guards. Oops.")
    if Question1 == "run":
        print("You launch yourself toward the pedestal at maximum ferret speed. Unfortunately, maximum ferret speed is not the same thing as maximum intelligence. You skid across the polished floor, crash into a chair, and send a stack of papers flying into the air. Every guard turns toward you at once. 'INTRUDER!' someone shouts. You attempt to hide behind a candlestick. It is not nearly large enough to hide a ferret.\nGAME OVER! You have officially made the worst first impression in American history.")
        return False

    return True
    
    
    # GB, Room Two, 1900s
def grandma (player_name):
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

# CD, Room Three, 2000s
def current_era (player_name):
    print("Welcome to the 2000s room!\n")
    print("You tumble through the door and land on a crowded city street in the 2000s. Cars honk. People shout into flip phones. Someone is carrying approximately seventeen shopping bags. You sniff the air. Hot dogs. French fries. Perfume. And... CANDY. Your ears perk up. Across the sidewalk, a baby sits in a stroller, happily clutching a bright pink lollipop. You stare at the lollipop. The lollipop stares back. Well, it doesn't actually stare back, because it is candy, but you are taking this personally. Your mission is simple: steal the lollipop and get to the next door. Unfortunately, the baby's mother is standing right beside the stroller. You are about to discover that stealing candy from a baby is surprisingly difficult when you are a ferret the size of a sandwich.")

    baby_one = input("\nHow do you approach the stroller?\nDo you (sneak) behind it, (run) right towards the baby, or (distract) the mother: ").strip().lower()

    if baby_one == "sneak":
        print("You lower your body and slither beneath the stroller. Your flexible little body fits perfectly between the wheels. You peek upward. The lollipop is RIGHT THERE. You can practically taste victory. Unfortunately, the stroller begins moving. You grab the frame with your paws and cling on like a tiny furry passenger. You are now traveling down a crowded sidewalk beneath a baby carriage.\n")
    elif baby_one == "run":
        print("You charge toward the stroller with absolutely no plan. A pedestrian yelps. Someone drops a shopping bag. A man in a business suit jumps out of your way. You leap toward the lollipop, miss completely, and land in a pile of shopping bags. The baby's mother turns around. She spots you. Her expression suggests that she has never seen anything more suspicious in her entire life. GAME OVER! You have been caught attempting to rob an infant in broad daylight. Your criminal career has reached a new low.\n")

        return False
    elif baby_one == "distract":
        print("You spot a loose shopping bag and give it a mighty shove with your nose. It rolls across the sidewalk. 'HEY! MY BAG!' the mother shouts, turning away from the stroller. You puff up your fur and perform a tiny victory dance. Your distraction worked! You are a genius! A criminal genius! A criminal genius who is about to get distracted by a French fry.\n")


    print("You are beside the stroller. The mother is distracted, and the baby is happily waving the lollipop around. You extend one tiny paw. Your whiskers tremble. Your tail twitches. This is the greatest moment in ferret history. Then the baby notices you and smiles. Uh-oh. You have made eye contact with your target.\n")

    baby_two = input("Would you like to (jump) into the baby's lap, (wait) for the perfect opportunity, or (grab) the lollipop from the side: ").strip().lower()

    if baby_two == "wait":
        print("You crouch beside the stroller and wait. Ten seconds pass. Then twenty. You begin sniffing the wheels. The mother turns back toward the stroller. She spots you sitting beside it like a suspicious little potato. 'WHERE DID YOU COME FROM?' You attempt to run, but a crowd has gathered around you. GAME OVER! You have been defeated by the forces of responsible parenting.\n")

        return False
    elif baby_two == "grab":
        print("You sneak around the stroller and stretch your tiny body as far as it will go. Your front paws reach the lollipop while your back paws remain on the sidewalk. For one beautiful second, you are a perfectly extended ferret bridge. You grab the candy and drop back onto all four paws. The baby begins to cry, and the mother turns around. You have the lollipop. Now you just need to escape before the entire sidewalk becomes interested in your crimes.\n")
    elif baby_two == "jump":
        print("You leap into the baby's lap with the confidence of a creature who has never once considered gravity. The baby giggles and waves the lollipop directly in front of your nose. You gently grab it in your mouth. Unfortunately, the baby finds your tail fascinating and attempts to hold it. You wriggle, twist, and perform an emergency ferret wiggle to escape. You land safely on the sidewalk with the lollipop. Your dignity has taken a minor hit, but the mission is still alive.\n")

    print("\nYou spot a mysterious door at the far end of the sidewalk. It is standing in the middle of the street for absolutely no logical reason. At this point, you have decided not to question the architecture of time travel. The crowd is closing in. The baby is searching for their lollipop. A man is pointing at you and shouting something about a weasel. You clutch the lollipop and sprint toward the door. Your little legs move at approximately one million miles per hour, although you are probably only moving at a moderately impressive ferret speed.\n")

    baby_three = input("You have the lollipop! You can (run) through the door, (sit) and lick your new lollipop, or (steal) a little french fry you see on the sidewalk. What would you like to do: ").strip().lower()

    if baby_three == "run":
        print("You charge toward the door, squeeze through the gap, and disappear just as the mother reaches for your tail. ITEM COLLECTED: THE BABY'S LOLLIPOP! You have escaped the crowded street with your candy. You are now carrying the Declaration of Independence, Grandma's dentures, and a lollipop. Somehow, this is the most successful day of your life.\n")
    elif baby_three == "sit":
        print("You stop to admire your lollipop. You sniff it. You inspect it. You briefly consider whether it would fit beneath your tail. This is your mistake. The mother catches up, the crowd surrounds you, and someone finally picks you up. GAME OVER! You have been defeated by your own inability to stop investigating interesting objects.\n")
    elif baby_three == "steal":
        print("You spot a French fry on the sidewalk. Your mission is forgotten instantly. You grab the fry and begin dragging it toward a nearby hiding place. Unfortunately, you are so busy with your snack that you fail to notice the crowd closing in. A hand reaches down. You look up. Oh. GAME OVER! You had one job. ONE JOB. And you chose a French fry.\n")

        return False

    return True

# AP, Room Four, 3000s
def future (player_name):
    print("You now enter a room that looks future-like. You take a look around the room and see a calendar on the wall. It is currently June 9th, 3004, and it sure looks like it. You look at the walls and there is a picture of a really old dude with a jetpack next to it. This has got to be Elon Musk's great grand son.")
    print("Goal: steal a jetpack hanging on the wall.")
    print("What would you like to do?")
    future_choice1 = input("You can: Quickly try and grab the jetpack and run (1), wait (2), or search the room (3)")
    if future_choice1 == "2":
        print("You wait for 30 minutes and your leg falls asleep (Choose again)")
    if future_choice1 == "3":
        print("You search around the room, find a penny from 2996, and put it in your pocket. You later try to open the door across from you, and notice its locked. You have to find the hidden object un the room to unlock it. GO!")
    if future_choice1 == "1":
        print("You grab the jetpack off of the wall, and a shiny object falls out.")
        future_choice2 = input("Do you want to pick it up? Yes or no?:")
        if future_choice2 == "Yes":
            print("You pick it up and notice its a key. The key has five grooves on the bottom, and it looks made for someone specifically. ")
        else:
            print("You leave the shiny object and your tail his the on botton of the jetpack, I know very inconveinent, and you fly thorught the rich guys roof and fly into the clouds for forever.\nYou lost! You had {_}/4 items. Would you like to play again? (yes) or (no)")

# CD, final scores and calling functions

def record_record (wins, losses):
    with open("final_stats.txt", "w") as file:
        file.write(str(wins) + "," + str(losses))

stats_filename = "final_stats.txt"

if not os.path.exists(stats_filename):
    record_record(0,0)

score_record = ""

with open(stats_filename, "r") as file:
    score_record = file.read()
    
scores_scores = score_record.split(",")

wins = int(scores_scores[0])
losses = int(scores_scores[1])

new_losses = 0
new_wins = 0

ask_to_play_again = False

while True:
    if ask_to_play_again == True:
        new_losses += 1
        play_again = input("\nYou lost!\n\nDo you want to play again Y or N? ").strip().upper()
        if play_again == "N":
            break
        ask_to_play_again = False

    score = 0
    has_declaration = False
    has_dentures = False
    has_lollipop = False
    has_jetpack = False
    has_declaration_wrong = False

    proceed = first(player_name)
    if proceed == False:
        ask_to_play_again = True
        continue
    else:
        has_declaration = True

    proceed = grandma(player_name)
    if proceed == False:
        ask_to_play_again = True
        continue
    else:
        has_dentures = True

    proceed = current_era(player_name)
    if proceed == False:
        ask_to_play_again = True
        continue
    else:
        has_lollipop = True

    proceed = future(player_name)
    if proceed == False:
        ask_to_play_again = True
        continue
    else:
        has_jetpack = True

    break

if (has_jetpack and has_lollipop and has_dentures and has_declaration):
    new_wins += 1


print("")
if new_wins >= 1:
    print(f"YOU WON! Your new record is {wins + new_wins} wins and {losses + new_losses} losses.")
else:
    print(f"You lost YET AGAIN. Your record is {wins + new_wins} wins and {losses + new_losses} losses.")


wins += new_wins
losses += new_losses

record_record(wins, losses)