from os import system
clear = lambda :system("cls")

def start_game():
    number_of_players = int(input("please enter number of players: "))
    color_list = ["Green" , "Blue" , "Red" , "Yellow" , "Purple" , "Orange"]
    player_color_list = []
    player_name_list = []

    for i in range(number_of_players):
        dic = {"name":"none","color":"none"}
        name = input("please enter your name: ")
        # dic["name"] = name
        player_name_list.append(name)
        clear()


        for indx , value in enumerate(color_list):      
            print(indx,value)

        while True:
            color_index = int(input(f"{name} please choose a color from above (color index): \n"))
            if color_index < len(color_list) and isinstance(color_index,int):
                break
            print(f"please enter a valid number between 0 to {len(color_list)-1}")

        # dic["color"] = color_list[color_index]
        player_color_list.append(color_list[color_index])
        color_list.pop(color_index)
        clear()
        # players_information.append(dic)

        print(f"{name} welcome to the game your chosen color is {color_list[color_index]}")

    return player_color_list , player_name_list




def menu():
    while True:
        print("welcome to game")
        print("press 'S' to start a new game ")
        print("press 'D' to see rules")
        print("press 'Q' to exit")

        inp = input()

        if inp.upper() == "S":
            start_game()
            clear()
            print("press any key to continue")
        if inp.upper() == "D":
            print("""Colt Super Express is the far cheaper, quicker, smaller box version of its big brother Colt Express.
                   You all play as bandits and are trying to shoot the other players and knock them off the train, so you 
                  can keep all the booty yourself! This version uses cards to represent the train, rather than 3D train cars.
                   The box also comes with two expansions, as standard. These shake up the gameplay but are not recommended 
                  until you are familiar with the base game. Which shouldn’t take too long, as the game is simple and plays quickly.
                    Colt Super Express is a game for 3 to 7 players and plays within 15 minutes. I think, therefore, it qualifies as a party game, 
                  although it isn’t your typical Scrawl, Just One, or Cranium. This is serious looting business, with guns and player 
                  elimination. The main mechanism in Colt Super Express is programmable movement. During the Schemin’ phase, players will
                   decide which order they wish to play their actions. You choose three of your cards to play and place these down on the 
                  table in the order you wish to perform them. The four action choices are: turn around, move to the next train car, move up 
                  onto the roof, or back into the train car and shoot.""")
        if inp.upper() == "Q": 
            break
        input("press any key to continue")
        clear()


menu()