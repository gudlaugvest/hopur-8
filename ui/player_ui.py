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
            #villucheck
            while True:
                try:
                    how_many = int(input("How many players?: "))
                    if how_many >= 4:    
                        for i in range(how_many):
                            print()
                            player = Player()
                            player.name = input("Enter Player name: ")
                            while True:
                                try:
                                    player.ss_number = input("Enter Social Security Number(0000000000): ")
                                    if len(player.ss_number) == 10:
                                        break
                                    else:
                                        print()
                                        print("Invalid ss number, try again")
                                except:
                                    ValueError
                                    
                            player.home_address = input("Enter Home Address: ")
                            while True:
                                try:
                                    player.phone_number = input("Enter Phone Number: ")
                                    if len(player.phone_number) == 7:
                                        break
                                    else:
                                        print()
                                        print("Not a valid phone number, try againn")
                                            
                                except:
                                    ValueError
                            player.email_address = input("Enter Email Address: ")
                            while True:    
                                try:
                                    player.role = input("Enter Players Role(Captain/Player): ")
                                    if player.role == "Player".lower():
                                        break
                                    elif player.role =="Captain".lower():
                                        break
                                    else:
                                        print()
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
                            player.team_id = team.id
                            self.logic_wrapper.create_player(player)   

                    else:
                        print()
                        print("Players for each team has to be at least 4! Please try again!")
                except:
                    ValueError
                    print() 
                    ("Invalid input, can't be a string") 

 
     
        else:
            print()
            print("Invalid input, please try again!")

