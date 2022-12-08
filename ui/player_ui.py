from model.player_model import Player


class Player_UI:
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection

    def menu_output(self):
        """Menu for Players"""
        print()
        print("####################################")
        print()
        print("Player".rjust(18))
        print()
        print("c. Continue To Input Player Info")
        print("b. Go Back To Organizer Menu")


    def input_prompt(self):
        '''The function counts how many players the Organizer wants to input and inputs the information 
        for each players and gives role for 1 captain and rest players'''
        self.menu_output()
        print()
        command = input("Enter Command: ")
        if command == "b":
            return "b"
        elif command == "c":
            print()
            how_many = int(input("How many players?: "))
            while how_many < 4:
                print()
                print("Players for each team has to be at least 4! Please try again!\n")
                how_many = int(input("How many players?: "))
                print()
            else:
                for i in range(how_many):
                    print()
                    player = Player()
                    
                    
                    
                    player.name = input("Enter Name: ")
                    while True:
                        
                        try:
                            player.ss_number = input("Enter Social Security Number(0000000000): ")
                            if len(player.ss_number) == 10:
                                break
                            else:
                                print("Invalid ss number, try again")
                        except:
                            ValueError
                           
                    player.home_address = input("Enter Home Address: ")
                        
                    while True:
                        try:
                            player.phone_number = input("Enter phone number: ")
                            if len(player.phone_number) == 7:
                                break
                            else:
                                print("Not a valid phone number, try again")
                                
                        except:
                            ValueError
                            
                                
                    player.email_address = input("Enter Email Address: ")
                    while True:    
                        try:
                            player.role = input("Enter Players Role(Captain/Player): ")
                            if player.role == "Player".lower() or "Captain".lower():
                                break
                            else:
                                print("Not a valid role, try again")
                            
                        except:
                            ValueError
                            
                            
                        team_name = input("Enter Team Name: ")
                        team_name = team_name.lower()
                        team = self.logic_wrapper.get_team_by_name(team_name) 
                        while team is None:
                            print("No team found with that name")
                            team_name = input("Enter Team Name: ")
                            team_name = team_name.lower()
                            team = self.logic_wrapper.get_team_by_name(team_name) 

                        print()          
                        player.team_name = team.id
                        self.logic_wrapper.create_player(player)   
                    
        else:
            print()
            print("Invalid input, please try again!")
'''while True:
  try:
    number = int(input("Please enter an integer: "))
    break
  except ValueError:
    print("Oops! That was not a valid number. Try again...")

    while True:
    try:
        user_input = input("Enter your input: ")
        if len(user_input) == 7:
            break
        else:
            print("Invalid input - must be 7 characters long")
    except:
        print("Error - please enter a valid input")'''         

'''while True:
    try:
        myInput = input("Please enter a 7-digit number: ")
        if len(myInput) != 7:
            raise ValueError
    except ValueError:
        print("The number must have exactly 7 digits")
    else:
        break'''        