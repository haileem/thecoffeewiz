# Hailee Martino
# Term Project
# Section 0101

import pygame
import time


def recommendation():
    '''
    recommendation() takes the user through a series of questions that lead to a coffee recommendation based on their answers

    Parameters
    ----------
    N/A

    Returns
    -------
    rec: string
        recommendation based on user's answers to questions
    '''
    ans = input("Are you a regular coffee drinker (y/n)? ")
    if ans == 'y':
        ans = input("Do you drink coffee for the taste(a), caffeine(b), or both(c) (a/b/c)? ")
        if ans == 'a':
            ans = input("Are you feeling a hot or cold coffee (h/c)? ")
            if ans == 'h':
                rec = 'cappuccino'
                print("I recommend a cappuccino! A cappuccino is a classic coffee drink with espresso and milk and a thick layer of foam. It is a very balanced and tasty combination.")
            elif ans == 'c':
                rec = 'cold brew'
                print("I recommend a cold brew! A cold brew is simply coffee brewed cold. It is natually smoother and less acidic.")
        elif ans == 'b':
            ans = input("Are you feeling a hot or cold coffee (h/c)? ")
            if ans == 'h':
                rec = 'drip coffee'
                print("I recommend a drip coffee! Drip coffee is the simplest form of coffee and its typically ready fastest, depending on if it's been brewed. Consider drinking it black if you just need some caffeine.")
            elif ans == 'c':
                rec = 'iced red eye'
                print("I recommend an iced red eye! A red eye is a bold drink containing iced coffee and espresso. This drink is definitely strong but it is sure to get you your caffeine.")
        elif ans == 'c':
            ans = input("Are you feeling a hot or cold drink (h/c)? ")
            if ans == 'h':
                rec = 'cortado'
                print("I recommend a cortado! A cortado is a small drink made with equal parts espresso and steamed milk. The milk is able to cut the strong flavor of the espresso without diminishing its flavor.")
            elif ans == 'c':
                rec = 'iced latte'
                print("I recommend an iced latte! A latte is a delicious milk based drink with espresso. It can be enjoyed with flavors or extra shots added depending on your taste. Consider getting an extra shot for that extra caffeine!")
    elif ans == 'n':
        ans = input("Do you like coffee (y/n)? ")
        if ans == 'y':
            ans = input("What are you doing today? Hanging out with friends(a), Running errands(b), Studying at the library(c), Relaxing at home(d). (a/b/c/d)? ")
            if ans == 'a':
                ans = input("Are you feeling a hot or cold drink (h/c)? ")
                if ans == 'h':
                    rec = 'flat white'
                    print("I recommend a flat white! A flat white is similar to a latte except its milk is steamed to a more smooth, silky texture and less frothy. This drink is perfectly sweet and simple for an outing with friends.")
                elif ans == 'c':
                    rec = 'iced latte'
                    print("I recommend an iced latte! A latte is a delicious milk based drink with espresso. It can be enjoyed with flavors or extra shots added depending on your taste. I especially recommend an iced vanilla latte!")
            elif ans == 'b':
                ans = input("Are you feeling a hot or cold drink (h/c)? ")
                if ans == 'h':
                    rec = 'espresso'
                    print("I recommend an espresso! Espresso is the most concentrated coffee and is often used in other drinks but can be enjoyed on its own. Espresso is perfect for when you need a quick caffeine lift.")
                elif ans == 'c':
                    rec = 'iced americano'
                    print("I recommend an iced americano! An americano is a simple drink made with espresso and water.")
            elif ans == 'c':
                ans = input("Are you feeling a hot or cold drink (h/c)? ")
                if ans == 'h':
                    rec = 'hot americano'
                    print("I recommend a hot americano! An americano is a simple drink made with espresso and water. This is good for studying because it isn't too dehydrating and it gives you some caffeine to get through your study session.")
                elif ans == 'c':
                    rec = 'cold brew'
                    print("I recommend a cold brew! A cold brew is simply coffee brewed cold. It is natually smoother and less acidic. This drink is refreshing and high in caffeine.")
            elif ans == 'd':
                ans = input("Are you feeling a hot or cold drink (h/c)? ")
                if ans == 'h':
                    rec = 'hot latte'
                    print("I recommend a hot latte! A latte is a delicious milk based drink with espresso. It can be enjoyed with flavors or extra shots added depending on your taste. This is a very cozy drink to enjoy when you are relaxing.")
                elif ans == 'c':
                    rec = 'iced coffee'
                    print("I recommend an iced coffee! A iced coffee is simply chilled drip coffee. What's special about iced coffee is how flavors and milks stand out. So don't be afraid to experiment!")
        elif ans == 'n':
            rec = 'hot chocolate'
            print("No worries, I recommend a hot chocolate instead!")
    return rec

def description(coffeetype):
    '''
    description() takes a coffeetype as the input and generates its corresponding description
    
    Parameters
    ----------
    coffeetype: string

    Returns
    -------
    dict[coffeetype]: string
        value (definition) of key (coffeetype) in the dictionary
    '''
    #open the text file  
    with open('coffeeinfo.txt', 'r') as f: 
        #read the text file into a list of lines 
        lines = f.readlines() 
 
    #create an empty dictionary 
    dict = {} 
 
    #loop through the lines in the text file  
    for line in lines: 
        #split the line on ':' 
        key, value = line.split(':') 
        #add the key, value pair to the dictionary 
        dict[key] = value 
   
    #print the description corresponding to the coffee type
    print(dict[coffeetype]) 
    pass

def type_text(screen, text, color, font, pos):
    '''
    type_text() takes text descriptors and prints the text by each character, as if it was typed 
    
    Parameters
    ----------
    screen: pygame.display.set_mode()
    text: string
    color: tuple
    font: pygame.font.SysFont
    pos: tuple

    Returns
    -------
    N/A
    '''
    #set up the initial empty text
    typed_text = ''
    
    #iterate through each character in the string
    for char in text:
        typed_text += char
        
        #display text
        rendered_text = font.render(typed_text, True, color)
        screen.blit(rendered_text, pos)
        
        #update display
        pygame.display.flip()
        pygame.time.delay(30) 

def instructions(coffeetype):
    '''
    instructions() takes coffeetype as an input and outputs its corresponding instructions to make 
    
    Parameters
    ----------
    coffeetype: string

    Returns
    -------
    dict[coffeetype]: string
        value (instructions) of key (coffeetype) in the dictionary
    '''
    #create an empty dictionary
    dict = {}

    #open the text file
    with open('coffeeinstructions.txt', 'r') as file:
        lines = file.readlines()

        key = None
        values = []

        #assign keys to words before : and values to words after :
        for line in lines:
            line = line.strip()
            if line.endswith(':'):
                if key:
                    dict[key] = values
                key = line[:-1]
                values = []
            elif line:
                values.append(line)

        #save the coffee type's instructions
        if key:
            dict[key] = values

    return dict.get(coffeetype, [])

def image(coffeetype):
    '''
    image() takes coffeetype as an input and outputs its image file name 
    
    Parameters
    ----------
    coffeetype: string

    Returns
    -------
    filename: string
    '''
    #remove spaces from coffee name
    coffeename = coffeetype.replace(" ", "")
    #rename filename corresponding to actually names
    filename = coffeename + '.jpg'
    return filename

def main():
    '''
    main() runs when Term Project.py is run
    '''
    print("\nWelcome to the Coffee Wiz")
    time.sleep(1)
    print("Before we make a drink, I would like give you a coffee recommendation based on my questions and your answers.")
    time.sleep(3)
    print("I'll ask some questions to get an idea of what you'll like.\n")
    time.sleep(3)

    # Giving Recommendation
    rec=recommendation()

    descriptionoptions = ['drip coffee', 'iced coffee', 'cold brew', 'espresso', 'americano', 'latte', 'cappuccino', 'flat white', 'cortado', 'red eye']
    makeoptions = ['drip coffee', 'iced coffee', 'cold brew', 'espresso', 'hot americano', 'iced americano', 'hot latte', 'iced latte', 'cappuccino', 'flat white', 'cortado', 'hot red eye', 'iced red eye', 'hot chocolate']

    # User's Coffee Choice
    while True:
        ans=input("\nWould you like to create our coffee recommendation(a) or something different(b) (a/b)? ")
        if ans=='a':
            #grabbing user's coffeechoice
            coffeechoice = rec
            print(f"\nGreat! We'll get started on your {coffeechoice}.\n")
            break
        elif ans=='b':
            # Descriptions of Coffee
            print("\nNo problem!")
            while True:
                ans = input("Would you like to know more about a type of coffee? (y/n): ")
                if ans == 'y':
                    print("\nCoffee Types:\n")
                    for option in descriptionoptions:
                        print(f" {option}")
                    while True:
                        ans = input("Which coffee would you like to know more about? (type exactly as shown): ")
                        if ans in descriptionoptions:
                            description(ans)
                            while True:
                                ans = input("Would you like another description? (y/n): ")
                                if ans == 'y':
                                    break
                                elif ans == 'n':                 
                                    break
                                else:
                                    print("Invalid input. Please type y or n.")
                            if ans == 'n':
                                break
                        else:
                            print("Invalid input. Please type coffee type exactly as shown.")
                    break

                elif ans == 'n':
                    print("Okay.")
                    break
                else:
                    print("Invalid input. Please type y or n.")

            #grabbing user's coffeechoice
            print("\nCoffee Types:")
            for option in makeoptions:
                print(f" {option}")
            while True:
                ans = input("\nWhich coffee would you like to make? (type exactly as shown): ")
                if ans in makeoptions:
                    coffeechoice = ans
                    break
                else:
                    print("Invalid input. Please type coffee type exactly as shown.")
            break
        else:
            print("Invalid input. Please type a or b.")
    
    #transition to cafe
    time.sleep(1)
    print("\n...Opening the Cafe...\n")
    time.sleep(3)

    # Initializing Pygame
    pygame.init()

    # Colors
    white = (255,255,255)
    black = (0,0,0)

    # Fonts
    font1 = pygame.font.SysFont('Comic Sans MS', 18)
    font2 = pygame.font.SysFont(None, 18)

    # Screens and Backgrounds
    screen = pygame.display.set_mode((466, 582))
    background = pygame.image.load('background.png').convert()
    notepad = pygame.image.load('notepad.png').convert()

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Introducing the user to the cafe
        screen.blit(background, (0,0))
        type_text(screen, "Welcome to the cafe!", white, font1, (40,180))
        pygame.time.delay(1000)
        type_text(screen, "This is where we will make your coffee.", white, font1, (40,210))
        pygame.time.delay(2000)

        # Describing the user's coffee choice
        screen.blit(background, (0,0))
        type_text(screen, "Your choice was a "+ coffeechoice +".", white, font1, (40,180))
        pygame.time.delay(1000)
        type_text(screen, "Let's take a look at how to make one.", white, font1, (40,210))
        pygame.time.delay(2000)

        # Printing coffeemade instructions
        screen.blit(background, (0,0))
        screen.blit(notepad, (32,150))
        type_text(screen, "How to make a " + coffeechoice + ":", black, font2, (58,215))

        #looping through each step from instructions function
        steps = instructions(coffeechoice)
        for i in range(len(steps)):
            type_text(screen, steps[i], black, font2, (58,240+(i*20)))
        pygame.time.delay(3000)

        # Displaying coffeemade result
        screen.blit(background, (0,0))
        coffee = pygame.image.load(image(coffeechoice)).convert()
        coffee = pygame.transform.scale(coffee, (150,150))

        screen.blit(coffee, (160,300))
        type_text(screen, "Your coffee is done!", white, font1, (40,180))
        pygame.time.delay(1000)
        type_text(screen, "We hope you enjoyed your time at the cafe.", white, font1, (40,210))
        pygame.time.delay(5000)

        # Stop game loop
        running = False

    pygame.quit()

    while True:
        ans = input("\nWould you like to try another coffee? (y/n) ")
        if ans == 'y':
            print("\n...Restarting Coffee Wiz...\n")
            time.sleep(3)
            main()
        elif ans == 'n':
            print("\nThank you for using the Coffee Wiz. Goodbye!")
            break
        else:
            print("\nThat was not a valid input. Goodbye!")
            break

if __name__ == "__main__":
    main()