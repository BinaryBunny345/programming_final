# CD, AP, JA, GB, Build a Game 
# #print("Start")

import os.path


print("Welcome to Being a Ferret 101!!")

# GB, making question for information about player
player_name = input("What is your name?: ").capitalize()

# AP, starting of the story, telling the player their goal, the story, and instructions.
print(f"\nOnce upon a time, there was this really STUPID ferret named {player_name}, who loved walking through doors to different time stamps. This ferret {player_name} accidently got trapped in the 1800s because {player_name} wanted to see the signing of the Declaration Of Independence. Unfortunately, {player_name} doesn't have their history straight and didn't go to August 2nd, 1776, because they're STUPID. Just kidding. We love you. Good luck!!\nThou awakest within a most exceedingly antiquated chamber, most peculiar in fashion, as though plucked straight from the nineteenth century—wink, wink. Before thee stands a door. With great curiosity, thou dost approach and attempt to open it, only to discover that the blasted thing is firmly locked. OH, DEAR! Whatever, pray tell, shallst thou do now?!?\n")

def first(player_name):
    # JA, Variable for the first room/era
    print(f"Upon entering the ancient house, thou art greeted by a humble room, its walls adorned with simple decorations and aged portraits. The wooden floors creak beneath thy feet, and the air is thick with the scent of old wood and parchment. At the very center of the room hangs the Declaration of Independence, proudly displayed as though it were a treasure of the highest importance. Gathered around it stand a company of distinguished gentlemen, dressed in fine coats, powdered wigs, and polished shoes. They speak amongst themselves in hushed, serious tones, their faces bearing the solemn expressions of men burdened with great responsibility. The room may lack grand riches and extravagant furnishings, yet it carries an air of history and importance, as though the very walls have witnessed the birth of a new nation.\n You push open the door and tumble directly into Independence Hall in the 1800s. The room is filled with polished wooden furniture, serious-looking gentlemen, and enough historical documents to give a librarian a heart attack. At the center of the room, displayed proudly on a pedestal, sits the DECLARATION OF INDEPENDENCE. It is surrounded by guards who look like they haven't smiled since the invention of the wheel. Your whiskers twitch. Your nose wiggles. Your three brain cells hold a meeting. One says, 'That looks important.'' Another says, 'That looks chewable.'The third has decided that the pedestal would make an excellent place for a nap. Your mission is to steal the Declaration without getting caught. Unfortunately, you are a ferret approximately the size of a loaf of bread, and you have the subtlety of a falling piano.\n")

    Question1 = input("What do you want to do in the room. You can: sit still(Sit), search the room more thoroughly(Search), to run and try to snatch it from under them(Run): ").strip().lower()

    if Question1 == "sit":
        print(f"You decide that standing perfectly still is an excellent strategy. You sit. You blink. You inspect your tail. Five minutes pass. Then ten. A guard finally notices the suspiciously furry object sitting in the middle of Independence Hall.'WHAT IS THAT THING?' he shouts. You puff up your fur and hiss. The guards surround you before you can perform your emergency escape wiggle.\n GAME OVER! You have been arrested for suspicious loaf-shaped behavior. Even the founding fathers are disappointed in you.\n")
        return False
    if Question1 == "search":
        print(f"You lower your body to the floor and begin investigating. Your tiny paws make almost no sound as you sneak beneath a wooden table. You spot two guards chatting near the pedestal. One complains about his aching feet. The other complains about his boring job. You have discovered their weakness: they are incredibly distracted. Unfortunately, your investigation is interrupted when you find a shiny button on the floor. You grab it in your teeth. It belongs to one of the guards. Oops.\n")
    if Question1 == "run":
        print(f"You launch yourself toward the pedestal at maximum ferret speed. Unfortunately, maximum ferret speed is not the same thing as maximum intelligence. You skid across the polished floor, crash into a chair, and send a stack of papers flying into the air. Every guard turns toward you at once. 'INTRUDER!' someone shouts. You attempt to hide behind a candlestick. It is not nearly large enough to hide a ferret.\nGAME OVER! You have officially made the worst first impression in American history.\n")
        return False
    
    print(f"\n")

    Question2 = input("What would you like to do now? Would you like to (sneak) behind the pedestal, (distract) the gaurds, or try to (charm) them: ").strip().lower()
    if Question2 == "sneak":
        print(f"You flatten your long, noodle-shaped body and squeeze beneath the pedestal. Your whiskers brush against the wood. You can hear the guards arguing above you. You carefully climb the side, grab the Declaration in your tiny paws, and pull it toward yourself. For one glorious moment, everything is perfect. Then you sneeze. Dust flies everywhere. You freeze, clutching the most important document in the room. A guard slowly turns around.\n")
    if Question2 == "distract":
        print(f"You spot a loose chair and decide to put your advanced ferret problem-solving skills to work. You push the chair with your nose until it crashes into a table. CLATTER! Every guard turns toward the noise. You immediately perform the ferret war dance in the opposite direction, bouncing sideways like a furry lunatic. The guards stare at you in complete confusion. You have successfully distracted them through the power of nonsense. Honestly, even you are impressed.\n")
    if Question2 == "charm":
        print(f"You approach the nearest guard and look up at him with enormous, innocent eyes. You tilt your head. You twitch your whiskers. You make a tiny chittering sound. The guard smiles. 'Well, aren't you a cute little creature?' SUCCESS! Unfortunately, he immediately picks you up and begins explaining the entire history of the United States to you. You have approximately no interest in this lecture.\n")

    print("The guards are distracted, and the Declaration is within reach. You scramble onto the pedestal, grab the document, and stuff it into your secret hiding place. It does not fit. You try again. It still does not fit. Eventually, you manage to drag the Declaration toward the door. Your tiny legs are working overtime, your whiskers are trembling, and your dignity has left the building. You reach the door just as a guard shouts, 'STOP THAT FERRET!' You squeeze through the doorway at the last possible second. ITEM COLLECTED: THE DECLARATION OF INDEPENDENCE! You have successfully stolen a founding document. Somewhere, a history teacher just felt a disturbance in the universe. You do not care. You have a shiny new door to investigate.\n")

    return True
    
    # GB, Room Two, 1900s
def grandma(player_name):
    print(f"You tumble through the door and end up in an apartment, with antiques scattering the area and intricately patterned couches. It seems like a grandma owns this place, unsuprisingly.\n In the corner of your eye, you see a glimmer of saliva. On top of the counter, is GRANDMA'S DENTURES. You HAVE to steal them in order to progress. You begin creeping towards the counter, when you hear a voice echoing from the nearby hallway.\n")
    print(f"Grandma: WHO'S IN MY HOUSE???\n Oh no. It's the owner of this place, Grandma!\n")
    print(f"Goal: steal grandma's dentures from the counter\n")
    print(f"Grandma is coming, quick! You can: Quickly try and grab the dentures (Grab), hide beneath the sofa (Hide), or pretend to be a pet (Pet): ")
                    
    granny_choice1 = input("What do you do?: ").strip().lower()

    if granny_choice1 == "grab":
        print("You squrry across the floor, and make a leap of fate towards the counter!...You miss. Badly. You bounce off the counter, knocking off the dentures along with you. This would be perfect, but before you can react, Grandma appears in the kitchen doorway. She examines you and her dentures on the floor, taking it all in. Suddenly, she snaps.")
        print("Grandma: OH NO YOU DON'T, YOU PEST!!!")
        print("She grabs you and throw you out the window, ending your quest for good.")
        return False
    elif granny_choice1 == "hide":
        print("You flatten yourself against the floor and squeeze beneath the sofa")
    elif granny_choice1 == "pet":
        print("You remember all your previous training and lock in. You sit innocently in the middle of the room, looking adorable as always.")
        print("Grandma: I didn't know I had a pet... Well I forget a lot of things. Aw, what a precious little animal!")
        print("She picks you up and starts scratching your head, which feels AMAZING. You almost forget your mission, before coming back to reality an realizing your goal. You bathe in the affection before she sets you down and disappears down the hallway.")
        
    print("Grandma")

    print("Hurry! You can: Distract Grandma (Distract), wait (Wait), or make a run for the dentures (Run).")
    granny_choice2 = input("You have to decide something ASAP: ").strip().lower()

    if granny_choice2 == "distract":
        print("hello")
    elif granny_choice2 == "wait":
        print("You decide")
    elif granny_choice2 == "run":
        print("")


# CD, Room Three, 2000s
def current_era (player_name):
    print(f"\nWelcome to the 2000s room!\n")
    print("You tumble through the door and land on a crowded city street in the 2000s. Cars honk. People shout into flip phones. Someone is carrying approximately seventeen shopping bags. You sniff the air. Hot dogs. French fries. Perfume. And... CANDY. Your ears perk up. Across the sidewalk, a baby sits in a stroller, happily clutching a bright pink lollipop. You stare at the lollipop. The lollipop stares back. Well, it doesn't actually stare back, because it is candy, but you are taking this personally. Your mission is simple: steal the lollipop and get to the next door. Unfortunately, the baby's mother is standing right beside the stroller. You are about to discover that stealing candy from a baby is surprisingly difficult when you are a ferret the size of a sandwich.")

    baby_one = input("\nHow do you approach the stroller?\nDo you (sneak) behind it, (run) right towards the baby, or (distract) the mother: ").strip().lower()

    if baby_one == "sneak":
        print(f"You lower your body and slither beneath the stroller. Your flexible little body fits perfectly between the wheels. You peek upward. The lollipop is RIGHT THERE. You can practically taste victory. Unfortunately, the stroller begins moving. You grab the frame with your paws and cling on like a tiny furry passenger. You are now traveling down a crowded sidewalk beneath a baby carriage.\n")
    elif baby_one == "run":
        print(f"You charge toward the stroller with absolutely no plan. A pedestrian yelps. Someone drops a shopping bag. A man in a business suit jumps out of your way. You leap toward the lollipop, miss completely, and land in a pile of shopping bags. The baby's mother turns around. She spots you. Her expression suggests that she has never seen anything more suspicious in her entire life. GAME OVER! You have been caught attempting to rob an infant in broad daylight. Your criminal career has reached a new low.\n")

        return False
    elif baby_one == "distract":
        print(f"You spot a loose shopping bag and give it a mighty shove with your nose. It rolls across the sidewalk. 'HEY! MY BAG!' the mother shouts, turning away from the stroller. You puff up your fur and perform a tiny victory dance. Your distraction worked! You are a genius! A criminal genius! A criminal genius who is about to get distracted by a French fry.\n")


    print(f"You are beside the stroller. The mother is distracted, and the baby is happily waving the lollipop around. You extend one tiny paw. Your whiskers tremble. Your tail twitches. This is the greatest moment in ferret history. Then the baby notices you and smiles. Uh-oh. You have made eye contact with your target.\n")

    baby_two = input("Would you like to (jump) into the baby's lap, (wait) for the perfect opportunity, or (grab) the lollipop from the side: ").strip().lower()

    if baby_two == "wait":
        print(f"You crouch beside the stroller and wait. Ten seconds pass. Then twenty. You begin sniffing the wheels. The mother turns back toward the stroller. She spots you sitting beside it like a suspicious little potato. 'WHERE DID YOU COME FROM?' You attempt to run, but a crowd has gathered around you. GAME OVER! You have been defeated by the forces of responsible parenting.\n")

        return False
    elif baby_two == "grab":
        print(f"You sneak around the stroller and stretch your tiny body as far as it will go. Your front paws reach the lollipop while your back paws remain on the sidewalk. For one beautiful second, you are a perfectly extended ferret bridge. You grab the candy and drop back onto all four paws. The baby begins to cry, and the mother turns around. You have the lollipop. Now you just need to escape before the entire sidewalk becomes interested in your crimes.\n")
    elif baby_two == "jump":
        print(f"You leap into the baby's lap with the confidence of a creature who has never once considered gravity. The baby giggles and waves the lollipop directly in front of your nose. You gently grab it in your mouth. Unfortunately, the baby finds your tail fascinating and attempts to hold it. You wriggle, twist, and perform an emergency ferret wiggle to escape. You land safely on the sidewalk with the lollipop. Your dignity has taken a minor hit, but the mission is still alive.\n")

    print(f"\nYou spot a mysterious door at the far end of the sidewalk. It is standing in the middle of the street for absolutely no logical reason. At this point, you have decided not to question the architecture of time travel. The crowd is closing in. The baby is searching for their lollipop. A man is pointing at you and shouting something about a weasel. You clutch the lollipop and sprint toward the door. Your little legs move at approximately one million miles per hour, although you are probably only moving at a moderately impressive ferret speed.\n")

    baby_three = input("You have the lollipop! You can (run) through the door, (sit) and lick your new lollipop, or (steal) a little french fry you see on the sidewalk. What would you like to do: ").strip().lower()

    if baby_three == "run":
        print(f"You charge toward the door, squeeze through the gap, and disappear just as the mother reaches for your tail. ITEM COLLECTED: THE BABY'S LOLLIPOP! You have escaped the crowded street with your candy. You are now carrying the Declaration of Independence, Grandma's dentures, and a lollipop. Somehow, this is the most successful day of your life.\n")
    elif baby_three == "sit":
        print(f"You stop to admire your lollipop. You sniff it. You inspect it. You briefly consider whether it would fit beneath your tail. This is your mistake. The mother catches up, the crowd surrounds you, and someone finally picks you up. GAME OVER! You have been defeated by your own inability to stop investigating interesting objects.\n")
    elif baby_three == "steal":
        print(f"You spot a French fry on the sidewalk. Your mission is forgotten instantly. You grab the fry and begin dragging it toward a nearby hiding place. Unfortunately, you are so busy with your snack that you fail to notice the crowd closing in. A hand reaches down. You look up. Oh. GAME OVER! You had one job. ONE JOB. And you chose a French fry.\n")

        return False

    return True

# AP, Room Four, 3000s
def future_era (player_name):
    print("Welcome to the 2000s room!\n")
    print("You burst through the door and land in a futuristic nightclub in the year 3000. Neon lights flash across the walls. Music pounds through the floor. Robots, humans, and suspiciously tall aliens crowd the dance floor. You sniff the air. Expensive perfume. Metallic robot oil. Something that might be cheese. You briefly consider abandoning your mission to investigate the cheese situation. Then you spot it. A magnificent jetpack resting beside a very large man near the edge of the dance floor. THE JETPACK. Your eyes widen. Your whiskers twitch. Your three brain cells suddenly unite in perfect agreement: THAT THING IS OURS. Unfortunately, the man standing beside it appears to be its owner. He is enormous. You are a ferret. This is not an ideal matchup.")

    future_one = input("\nHow do you get closer to the jetpack?\nDo you (blend) into the crowd, (run) right towards the jetpack, or (pretend) to dance: ").strip().lower()

    if future_one == "blend":
        print(f"You squeeze between dancing legs and weave through the crowd. Your long body is practically designed for navigating spaces that should be too small for you. You dart beneath a table, emerge beside a robot, and accidentally steal a shiny bracelet from its wrist. The robot looks down. 'THEFT DETECTED.' You immediately drop the bracelet and sprint away. Subtlety is not your strongest skill.\n")
    elif future_one == "run":
        print(f"You charge directly toward the jetpack, performing the fastest ferret sprint known to civilization. Unfortunately, you crash into a dancing alien, bounce off a robot, and slide across the floor directly in front of the jetpack's owner. The man looks down at you. You look up at him. Your ears flatten. 'IS THAT A FERRET?'' he shouts. GAME OVER! You have been spotted by the largest man in the club. Somewhere, your three brain cells are submitting their resignations.\n")

        return False
    elif future_one == "pretend":
        print(f"You enter the dance floor and begin bouncing sideways to the music. You puff up your fur, wiggle your tail, and perform the ferret war dance with absolutely no rhythm. The crowd goes wild. Someone cheers. A robot begins recording you. You have become the club's most unexpected entertainment. While everyone is distracted by your terrible dancing, you sneak closer to the jetpack.\n")


    print(f"You are only a few feet from the jetpack when the owner turns around. 'HEY! WHAT ARE YOU DOING NEAR MY JETPACK?' You freeze. Your nose twitches. Your tail goes completely still. You have approximately three seconds to make a decision. Three seconds, one jetpack, and a very large man who does not appear interested in sharing.\n")

    future_two = input("Would you like to (hide) beneath a table, (steal) something shiny to distract him, or (pretend) to be someones pet: ").strip().lower()

    if future_two == "hide":
        print(f"You dive beneath a nearby table and squeeze yourself behind a pile of discarded napkins. The man stomps past. You can hear him muttering about security and suspicious animals. You remain completely still. Your nose twitches. You spot a shiny screw beneath the table. NO. Focus. The jetpack. The jetpack is the mission. The screw can wait.\n")

    elif future_two == "steal":
        print(f"You spot a glowing bracelet on a nearby table and snatch it in your teeth. You sprint across the dance floor. The man immediately spots the bracelet and charges after you. 'COME BACK HERE!' You have successfully distracted him from the jetpack. Unfortunately, you have also given him a reason to chase you. Your strategy has a few minor flaws.\n")
    elif future_two == "pretend":
        print(f"You sit beside a group of clubgoers and look as adorable as physically possible. One person gasps. 'OH MY GOSH, LOOK AT THE FERRET!' Several people begin taking pictures. Someone offers you a tiny snack. For one glorious moment, you are the most popular creature in the club. Unfortunately, the jetpack's owner spots you through the crowd and begins marching in your direction. Fame is temporary. Your criminal record is forever.\n")

    print(f"\nThe owner turns away for one final moment. The jetpack is within reach. You sprint forward, scramble over a discarded chair, and launch yourself toward the controls. Your paws slide across the metal surface. You find the START BUTTON. You stare at it. The button stares back. Well, it doesn't actually stare back, because it is a button, but you are taking this personally. Behind you, the man shouts, 'HEY! GET AWAY FROM THAT!' You have one chance. One button. One very confused ferret.\n")

    future_three = input("You can (press) the start button immediately, (stop) to inspect the controls, or (drag) the jetpack away without starting it. What would you like to do: ").strip().lower()

    if future_three == "press":
        print(f"You slam your tiny paw onto the glowing button. The jetpack ROARS to life. Lights flash. Alarms sound. The club's music abruptly cuts out. The owner lunges toward you, but you are already airborne. Your tail streams behind you like a furry victory flag. ITEM COLLECTED: THE JETPACK! YOU DID IT. YOU ABSOLUTE MENACE.\n")
    elif future_three == "stop":
        print(f"You pause to inspect the buttons. One is red. One is blue. One has a tiny picture of a rocket. You sniff the controls. You lick one. You tap another with your nose. Behind you, the owner slowly approaches. 'What are you doing?' You finally press the correct button, but you are too late. He grabs the jetpack before it can lift off. GAME OVER! You have been defeated by your own curiosity. A tragic ending for a creature who once stole a founding document.\n")
        return False

    elif future_three == "drag":
        print(f"You grab the jetpack's straps in your teeth and begin pulling. The jetpack does not move. You pull harder. You brace your tiny paws against the floor. It moves approximately one centimeter. The owner turns around. 'ARE YOU SERIOUS?' You attempt one final mighty tug. Your paws slip, and you slide backward across the floor. GAME OVER! You have learned an important lesson: a ferret cannot simply drag away a jetpack through sheer determination. Probably.\n")

        return False

    return True

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

    proceed = future_era(player_name)
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
