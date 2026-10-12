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
