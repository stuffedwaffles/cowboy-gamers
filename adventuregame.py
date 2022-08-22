import ast
#assume your user is dumber than a rock
#ability to teleport to locations once youve been there - add a thing to character progress thats like teleport True or False- with the option telling you options to do, it checks this variable and if True adds a line with places to tp- you enter tp and then a name of place which corresponds to one of the locations and it sets your location to there
#cause of death
# ability to drop items


print()
cause_of_death = ""

def opening():
    #intstructionas 
    print("welcome to [insert name here]!")
    print("This is a classic text based adventure game where you will be able to enter choices based on what you are told about your environment.")
    print("You have an inventory where you can store as many items as you want and check them at any time by typing 'items in bag'. You can see the description of or use a specific item by entering the item name.")
    print()
    print("An example: You are told about a computer sitting on a shelf in the room you are in. Based on the options given to you, you get to make the choice of saying 'check under shelf' or 'check computer'. You can say 'items in bag' to check your inventory. If it is an option, you could also say something such as 'leave room'.")
    print("You can also leave the game at any time by entering quit.")
    print("Enjoy!")
    print()

def bedroom():
    print()
    print("The Bedroom")
    print()
    print(f"Last night, you went to sleep in your own home. \nToday, however, you wake up somewhere quite different. \nYou wake up in a dark room, with no memory of how you got there. You feel something next to you and move it to your lap. The object seems to be a backpack, one you recognize from years ago. Bits of light are scattered to your left, and you see that it comes from a small window that is slightly ajar, letting in a slight breeze along with the light. You feel a springy mattress beneath you as your back presses against the wall behind you. To your right stands a simple table with a drawer that you can barely make out in the dark. Directly in front of you, you see a rectangular outline of a door, which seems to be tightly shut. You can't see anything else.")
    print("Objects you can check: table, bed, window, door")
    print("You can check the items in your bag('items in bag'), try using an item in your bag('[item name]'), check anything else in the room('check [item]'), or explore the room('explore').")
    location = "bedroom"
    inventory['bag'] = bag
    if "bedroom" not in teleport_list:
        teleport_list.append("bedroom")
    available_locations = teleport(teleport, teleport_list)
    while True:
        character_progresses[character_name] = [inventory, location, teleport, teleport_list]
        with open(r'stuf\actual projects\cowboy gamers\progress.txt', 'w') as file:
            file.write(str(character_progresses))   
        print()
        choice = input("> ")     
        print()
        if "window" in choice:
            print("You walk to the window, pushing it slightly. You find that the window opens easily, creaking as you open it fully. From what you can see, you are a couple floors off the ground. You can climb out of the window, but you may want to check other things in the room before you leave.")
            print("Objects in the room you can check: table, bed, window, door")
            print("You can check the items in your bag('items in bag'), try using an item in your bag('[item name]'), check anything else in the room('check [item]'), explore the room('explore'), or climb out the window('climb out').")
            if teleport == True:
                print(f"You can also teleport to {available_locations} by typing '/tp [location name]'.")
        elif "bed" in choice:
            print("You look under the bed and find dust and a couple mice. They scurry into a hole. You get up, disappointed, and wipe the dust off of your pants.")
            print("Objects in the room you can check: table, bed, window, door")
            print("You can check the items in your bag('items in bag'), try using an item in your bag('[item name]'), check anything else in the room('check [item]'), or explore the room('explore').")
            if teleport == True:
                print(f"You can also teleport to {available_locations} by typing '/tp [location name]'.")
        elif "table" in choice:
            print("You first bend to check under the table, where you see nothing but mice and dust. In the drawer, however, you find something a bit more exciting: a note and a flashlight. You keep both in your inventory.")
            print("Objects in the room you can check: table, bed, window, door")
            print("You can check the items in your bag('items in bag'), try using an item in your bag('[item name]'), check anything else in the room('check [item]'), or explore the room('explore').")
            if teleport == True:
                print(f"You can also teleport to {available_locations} by typing '/tp [location name]'.")
            inventory['note'] = note
            inventory['flashlight'] = flashlight
        elif "door" in choice:
            print("You walk to the door, first trying the handle to see if it will open. Unfortunately, it doesn't. You feel a keyhole in the handle, meaning you might need to find a key to open the door. You peer inside the keyhole, and with the bit of light you have, you can make out some mechanisms inside- but they look a little bit suspicious. On the floor next to the door, you find a bowl of kidney beans. While they're barely cooked, you need food and they're your best bet.")
            print("Objects in the room you can check: table, bed, window, door")
            print("You can check the items in your bag('items in bag'), try using an item in your bag('[item name]'), check anything else in the room('check [item]'), or explore the room('explore').")
            if teleport == True:
                print(f"You can also teleport to {available_locations} by typing '/tp [location name]'.")
            inventory['kidney beans'] = beans
        elif "explore" in choice:
            print("You walk around the room, feeling the walls and floor. Next to the door, mounted on the wall, there is a painting. The painting is fairly old, featuring the legendary Gray Rushin in his prime years. The painting doesn't seem related to this mysterious situation, but you never know. You lift it off the wall and feel something hidden in the backing. You find a key inside the old and now torn backing. As you continue to walk, you also find a water bottle and a rope, both of which you keep in your bag. The rope could be useful later in getting down from heights.")
            inventory['key'] = key
            inventory['water'] = water
            inventory['rope'] = rope
            print("Objects in the room you can check: table, bed, window, door")
            print("You can check the items in your bag('items in bag'), try using an item in your bag('[item name]'), check anything else in the room('check [item]'), explore the room('explore'), or put the key in the door('unlock').")
            if teleport == True:
                print(f"You can also teleport to {available_locations} by typing '/tp [location name]'.")
        elif "unlock" in choice:
            print("You take the key out of your bag and try it in the door. As you turn the key, you hear a click, which you interpret as a success. However, you hear some vents turn on from somewhere in the room. Your eyes start to tear up and your throat closes. As you struggle to breathe, the world turns black. The last thing you hear is laughing.")
            cause_of_death = "chlorine gas"
            return 'game over'
        elif "climb out" in choice:
            print("You climb out the window, which is just big enough for you to fit through. As you stand up outside, you realize that you are on a ledge. The window swings shut behind you.")
            return 'ledge'
        elif "/tp" in choice and teleport == True:
            choice.replace("/tp", "")
            print(f"teleporting to {choice}")
            return choice
        elif choice in inventory.keys():
            print(inventory[choice])
        elif 'items in bag' in choice:
            for key_name in inventory.keys():
                print(key_name)
            print()
            print("See the description of or use any of these items by typing the item name.")
        elif "quit" in choice:
            return "quit"
        else:
            print("Please enter a valid option!")
            

def ledge():
    location = "ledge"
        
    print()
    print("On the Ledge")
    print()
    print("You stand on a small ledge just outside the window, about 10 feet off the ground. You cannot figure out a way to open the window behind you. There are other ledges and small metal decorations on the side of the house.")
    if teleport == True:
                print(f"You can also teleport to {available_locations} by typing '/tp [location name]'.")
    if "ledge" not in teleport_list:
        teleport_list.append("ledge")
    available_locations = teleport(teleport, teleport_list)
    if 'rope' in inventory.keys():
        inventory['rope'] = f"The rope is thick and frayed. You stretch it out and find that it is about 10 feet long, which is exactly what you need to get down the the ground. You throw one end to the ground and tie the other to a small decoration on the side of the building."
    else:
        print("You have no way to get down from the window or back into the room. Your only option is to jump. You secure the bag to your back, hoping it might provide some cushion, and jump, falling with your back towards the ground. As you pick up speed, you realize that this was not a good idea. You hit the ground with a loud thunk.")
        cause_of_death = "fall damage"
        return 'game over'
    while True:
        print()
        choice = input("> ")
        character_progresses[character_name] = [inventory, location, teleport, teleport_list]
        with open(r'stuf\actual projects\cowboy gamers\progress.txt', 'w') as file:
            file.write(str(character_progresses))        
        print()
        if choice in inventory.keys():
            print(inventory[choice])
            if choice == "rope":
                del inventory['rope']
                print("You slide down the rope and make it down safely, except for the slight rope burn now on your hands. ")
                return "outside"
        elif 'items in bag' in choice:
                for key_name in inventory.keys():
                    print(key_name)
                print()
                print("See the description of or use any of these items by typing the item name.")
        elif "quit" in choice:
            return "quit"
        else:
            print("Please enter a valid option!")

def outside():
    location = "outside"
    print()
    print("Outside the House")
    print()
    print("You turn around and see that you have come down on the left of a new and well cared for house. The house is colored blue with a white roof. A busy road, filled with parked cars and people giving you odd looks, stretches off into the distance. A neighborhood of houses that look exactly like the one you just came out of are lined up on the sides of the road. A forest of trees with yellow and red colored leaves surrounds the neighborhood. At one end of the street, you can make out what seems to be a town square. The sky is a bright blue scattered with clouds, and the air is cold.")
    print("This is strange to you, as last night, it seemed to be the middle of summer. The weather was warm and you had watched kids on summer break chase fireflies. Here, however, it is chilly and windy.")
    print("You can head down the road to the town square, although it may be better to check the house first.")
    print("Objects you can check: house, road")
    print("You can check the items in your bag('items in bag'), try using an item in your bag('[item name]'), or check an object around you('check [item]')")
    if "outside" not in teleport_list:
        teleport_list.append("outside")
    available_locations = teleport(teleport, teleport_list)

    while True:
        character_progresses[character_name] = [inventory, location, teleport, teleport_list]
        with open(r'stuf\actual projects\cowboy gamers\progress.txt', 'w') as file:
            file.write(str(character_progresses))  
        print()
        choice = input("> ")      
        print()
        
        if "house" in choice: 
            print("You walk carefully around the house, checking the first floor windows. They are all closed and you can't see inside. You see everything that would be in a normal house: gutters, a small porch with a swing, a chimney. However, when you walk around the back of the house, you see something that none of the other houses have: a shed. Odd noises come from inside the shed, so you leave it alone for now. You circle back around the house, having found nothing too exciting. You could head down the road, but before doing so, make sure you have everything you need from the house.")
            print("Objects you can check: shed, porch, house, road")
            print("You can check the items in your bag('items in bag'), try using an item in your bag('[item name]'), or check an object around you('check [item]')")
            if teleport == True:
                print(f"You can also teleport to {available_locations} by typing '/tp [location name]'.")
        elif "road" in choice:
            print("You leave the house behind, walking towards the town square. The street is not very crowded, and cars occasionally drive past. People are looking at you weirdly, so you look down and realize that you are wearing old and now ripped pajamas, wearing a frayed backpack filled up with random objects, and holding an axe. You ignore the people looking at you and stuff the axe in your bag. As you approach the town square, you start to hear music and cheering. This is strange, since at home, there were no events or holidays coming up. It's almost like you're in a completely different universe. You shake off the thought and keep walking, approaching the town.")
            return 'town square'

        elif "shed" in choice:
            print("You head back to the shed. The noises get louder, and as you approach, you hear what could be the whining of an animal. You recognize the sounds as coming from a dog, although you don't know how. As you approach the shed, the noises get louder. The door however, is locked tightly shut by a three-digit lock. You may have something in your inventory to help you open it.")
            print("Objects you can check: porch, house, road")
            print("You can check the items in your bag('items in bag'), try using an item in your bag('[item name]'), or check an object around you('check [item]")
            if teleport == True:
                print(f"You can also teleport to {available_locations} by typing '/tp [location name]'.")
            if 'key' in inventory.keys():
                inventory['key'] = "You take out the key, and realizing the shed lock is numbered, search for the number written on the back. You enter 257 into the numbered lock and are surprised to hear it click open."

        elif "porch" in choice:
            print("You head to the porch, gently climbing the stairs. As you reach to grab the handrail, it snaps under your touch and falls to the side. The noise echos through the neighborhood and people turn their heads, wondering what you are doing. On the porch, you see a swing that probably isn't safe to sit on. Under it, however, you find a note. The door is bolted shut and covered with planks of wood. A bowl of navy beans sits next to the door. You pick them up and add them to your inventory. You also add the note to your inventory.")
            inventory['note 2'] = note2
            inventory['navy beans'] = beans
            print("Objects you can check: shed, house, road")
            print("You can check the items in your bag('items in bag'), try using an item in your bag('[item name]'), or check an object around you('check [item]")
            if teleport == True:
                print(f"You can also teleport to {available_locations} by typing '/tp [location name]'.")
        elif "key" in choice and inventory['key'] == "You take out the key, and realizing the shed lock is numbered, search for the number written on the back. You enter 257 into the numbered lock and are surprised to hear it click open.":
            print(inventory['key'])
            print("The shed door swings open with a sprinkle of wood chips and a loud creak. You see that the noise was indeed coming from a dog. A golden retriever, chained to a post in the shed, watches you as you slowly move inside the shed. The dog's tail wags slowly. It's fur is dirty but not yet matted, and it seems like the dog was recently fed. You have enough space to circle the dog and find an axe to cut it free. You cut the chain on the dog and keep the axe in your inventory.")
            if 'navy beans' in inventory.keys() or 'kidney beans' in inventory.keys():
                print("Almost instantly, the dog jumps at you, grabbing your backpack. Things fall out until the dog finds the beans, devouring them. I guess they were useful after all. Then, surprisingly, the dog sits. It stares at you, waiting for your command. You slowly move towards the dog, checking the dusty collar around its neck. The nametag fittingly says 'Beans'. The dog's tail wags excitedly, hitting the ground over and over. You reach for it's head to see if you can pet it. The dog sniffs your hand and then flops on to the ground, belly up. After a short belly rub, you decide to leave the shed. To your surprise, the dog follows you out. When you stop, it stops and sits down. WHen you turn to the left, it gets up and starts walking left, but waits for you after getting a few feet ahead.")
                print()
                if input("Would you like to keep the dog and bring it with you on your adventure? He could be useful in fights or just as a companion. (y/n) ") == "y":
                    inventory['dog'] = dog
                    print("You smile at the dog and walk back towards the house. It follows you, tail wagging excessively all the way. Beans is now listed as an item in your inventory and you can see his description or use him by typing 'dog'.")
                else:
                    print("You lead the dog back to the shed and attach it back to the post with a rope you find in the shed. You wave goodbye, leaving behind your only companion that sadly watches you head back to the house.")
                try:
                    del inventory['navy beans']
                except KeyError:
                    del inventory['kidney beans']

            else:
                print("Almost instantly, the dog jumps at you, grabbing your backpack. When it finds nothing of interest, it leaps at you instead. You fall down due to the size and ferocity of the dog. As you start to black out from the pain of claws digging into your skin, you catch a glimpse of the collar. It reads 'Beans'. ")
                cause_of_death = "Beans the dog"
                return 'game over'
                
            print("Objects you can check: porch, house, road")
            print("You can check the items in your bag('items in bag'), try using an item in your bag('[item name]'), or check an object around you('check [item]")
            if teleport == True:
                print(f"You can also teleport to {available_locations} by typing '/tp [location name]'.")
        elif choice in inventory.keys():
            print(inventory[choice])
        elif 'items in bag' in choice:
            for key_name in inventory.keys():
                print(key_name)
            print()
            print("See the description of or use any of these items by typing the item name.")
        elif "quit" in choice:
            return "quit"
        else:
            print("Please enter a valid option!")
                    
def town_square():
    location = 'town square'
    print()
    print("In the Town")
    print()
    print("The sun is dipping below the horizon as you enter the town square. It is surrounded by many different buildings, and you see a clothes shop, a motel, a barber, and a pub. In the middle of the square, people are gathered, celebrating and playing music. Food stands and carnival games surround the outside of the square. A tall and confident man in a suit stands on a stage decorated with colorful banners, preparing to give a speech. People are gathered around the stage, cheering. You move closer to listen. 'Welcome to the yearly town carnival! I am your mayor, John Smith! I see many new and familiar faces. I'm excited to announce new things coming to our town this year. I can't tell you what they are just yet, but the new additions will be like nothing you've ever seen before. Thank you all for coming and enjoy the festivities!' To your disappointment, the mayor mentioned nothing about what year it is or where you are, although his voice sounds vaguely familiar. You try to remember where you've heard it before, but you can't remember anything beyond the room you woke up in.")
    print("You can head towards any of the buildings or explore the carnival more. Both may hold information about the year or the location.")
    print("Objects you can check: clothes shop, motel, barber, pub, carnival")
    print("You can check the items in your bag('items in bag'), try using an item in your bag('[item name]'), or check an object around you('check [item]")
    if "town square" not in teleport_list:
        teleport_list.append("town square")
    available_locations = teleport(teleport, teleport_list)
    while True:
        character_progresses[character_name] = [inventory, location, teleport, teleport_list]
        with open(r'stuf\actual projects\cowboy gamers\progress.txt', 'w') as file:
            file.write(str(character_progresses))   
        print()
        choice = input("> ")     
        print()
        if "clothes shop" in choice:
            pass
        elif "motel" in choice:
            pass
        elif "barber" in choice:
            pass
        elif "pub" in choice:
            pass
        elif "carnival" in choice:
            pass
        elif choice in inventory.keys():
            print(inventory[choice])
        elif 'items in bag' in choice:
            for key_name in inventory.keys():
                print(key_name)
            print()
            print("See the description of or use any of these items by typing the item name.")
        elif "quit" in choice:
            return "quit"
        else:
            print("Please enter a valid option!")

def game_over():
    print()
    print("Game Over! You died!")
    print(f'Cause of Death: {cause_of_death}')
    play_again = input("Play again? (y/n) ")
    inventory.clear()
    location = ""
    teleport = False
    teleport_list = []
    del character_progresses[character_name]
    with open(r'stuf\actual projects\cowboy gamers\progress.txt', 'w') as file:
            file.write(str(character_progresses)) 
    return play_again

        
#character!
print("If you have played this game previously, please enter your old character name so we can retrieve your location and inventory.")
character_name = input("Please enter a name for your character: ")
with open(r'stuf\actual projects\cowboy gamers\progress.txt', 'r') as f:
    file = f.read()
    character_progresses = eval(file)
print()

#all objects
bag = f"The bag is old and faded. It tears in some places as you lift it and examine it. You don't find anything unusual."
note = f"You take the note out of your pocket and read it. It reads: \nDear {character_name}, \n    Welcome to my lovely home! I think you'll find it quite comforting. \n    If you hadn't noticed, the door is locked. There is a key in this room, but be careful! \n    Theres also a couple booby traps! Your goal? Escape! \n    Good luck, my friend!"
note2 = f"    I see you escaped, {character_name}! You're quite clever, but you won't last long here. \n    Nobody in this town will last much longer, considering my plans for it. \n    Well, enjoy the time you have left!"
flashlight = f"You examine the black flashlight, turning it on with the flip of a switch on the back. The beam of light flickers, as if the batteries are about to die. You turn it off and put it away."
beans = f"You look at the beans, seeing that they are cold, slightly cooked, and damp. You take a bite, frowing at the taste. While these beans aren't filling nor good-tasting for you, they might be appetizing to an animal or other person."
key = f"The key is dusty and cold. As you turn it over in your hands, you feel engravings on the surface. There are three numbers- 257. They don't seem to be of much use here. The key, however, could open something."
water = f"You check the water. It seems clean, which is reassuring."
rope = f"The rope is thick and frayed. You stretch it out and find that it is about 10 feet long. It might be useful to get down from somewhere."
dog = f"Beans is a dusty medium sized golden retriever and has given you his loyalty due to you giving him beans. Beans watches you, with his tongue sticking out to one side and his tail wagging. As you pat him on the head, he shakes off a layer of dust and happily trots around your legs."


def teleport(teleport, teleport_list):
    if teleport == True:
        print("You can now teleport to places you have been. To do this, write 'tp [location name]. Available locations: bedroom, ledge, outside, town square")
        available_locations = ", ".join(teleport_list)
        print(f"Available locations for you to teleport: {available_locations}")
        return available_locations
    elif teleport == False:
        return None
        


while True:
    if character_name in character_progresses.keys():
        location = character_progresses[character_name][1]#location = the second thing in the list which is location name
        inventory = character_progresses[character_name][0]
        teleport = character_progresses[character_name][2]
        teleport_list = character_progresses[character_name][3]
        print()
        print(f"User found! You left off at location '{location}' with {[key_name for key_name in inventory.keys()]} in your inventory.")
        start_over = input("Would you like to go back to where you left off (y) or start over (n)? ")
        if start_over == "y":
            location = character_progresses[character_name][1]#location = the second thing in the list which is location name
            inventory = character_progresses[character_name][0]
            teleport = character_progresses[character_name][2]
            teleport_list = character_progresses[character_name][3]

        elif start_over == "n":
            inventory = {}
            location = "bedroom"
            teleport = False      
            teleport_list = []    
            character_progresses[character_name] = [inventory, location, teleport]
        else:
            print("Invalid.")
            continue
            
    else:
        inventory = {}
        location = "bedroom"
        teleport = False
        teleport_list = []          
        character_progresses[character_name] = [inventory, location]
    
    opening()
    print("hit enter to start")
    start = input("> ")
    print()

    if location == 'bedroom':
        location = bedroom()
    if location == "ledge":
        location = ledge()
    if location == "outside":
        location = outside()
    if location == "town square":
        location = town_square()




    elif location == "quit":
        character_progresses[character_name] = [inventory, location, teleport, teleport_list]
        with open('stuf\cowboy gamers\progress.txt', 'w') as file:
            file.write(str(character_progresses))   
        break

    elif location == 'game over':
            yes_or_no = game_over()
            if yes_or_no == 'y':
                continue
            else:
                break
    
            
            
            
            
        
        
    
    