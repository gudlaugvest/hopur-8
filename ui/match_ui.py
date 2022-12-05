from logic.logic_wrapper import Logic_Wrapper

class Match_UI:

    def __init__(self, logic_wrapper : Logic_Wrapper):
        self.logic_wrapper = logic_wrapper
        

    def menu_output(self):
        print()
        print("############################")
        print()
        print("Match Menu".rjust(18))
        print()
        print("1. Create Match")
        print("2. Update Match")
        print("b. Go Back")

    def input_prompt(self):
        while True:
            self.menu_output()
            print()
            command = input("Enter your command: ")
            command = command.lower()
            if command == "b":
                break
            elif command == "q":
                return "q"
            elif command == "1":
                self.create_match_menu()
            elif command == "2":
                self.update_match_menu()
            else:
                print()
                print("Invalid input, please try again!")
    
    def create_match_menu(self):
        print()
        print("############################")
        print()
        print("Create Match".rjust(18))
        print()
        

        home_team = input("Enter home team: ")
        away_team = input("Enter away team: ")
        type_of_game = input("Enter type of game: ")
        date_of_match = input("Enter date of match: ")

        self.logic_wrapper.create_match(home_team, away_team, type_of_game, date_of_match)
    

    

    def update_match_menu(self):
        
        print()
        print("############################")
        print()
        print("Update Match".rjust(18))
        print()
        print("Enter id of the match you want to change")

        match_id = input("Enter match id: ")
        correct_match = self.logic_wrapper.get_match_result(match_id)
        print(correct_match)
        print()
        print("What do you want to change?")


        

        
        
        #self.logic_wrapper.update_match(home_team, away_team, type_of_game, date_of_match)

            
    