from logic.logic_wrapper import Logic_Wrapper
from model.match_results_model import Match_Result_Model

class Match_UI:

    def __init__(self, logic_wrapper : Logic_Wrapper):
        self.logic_wrapper = logic_wrapper
        

    def menu_output(self):
        """Print out Match Menu and options that user picks on what to do next"""
        print()
        print("####################################")
        print()
        print("Match Menu".rjust(22))
        print()
        print("1. Create Match")
        print("2. Update Match")
        print("b. Go Back")

    def input_prompt(self):
        """Get user input on what option they picked"""
        while True:
            self.menu_output()
            print()
            command = input("Enter Command: ")
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
        """Prints out header and gets user input on creating a match"""
        print()
        print("####################################")
        print()
        print("Create Match".rjust(23))
        print()
        
        match_ = Match_Result_Model()
        match_.home_team = input("Enter Home Team: ")
        match_.away_team = input("Enter Away Team: ")
        match_.type_of_game = input("Enter Type Of Game: ")
        match_.date = input("Enter date of match: ")



        self.logic_wrapper.create_match_result(match_)
    

    

    def update_match_menu(self):
        """Prints out header and gets user input on updating a match"""
        print()
        print("####################################")
        print()
        print("Update Match".rjust(23))
        print()
        print("Enter id of the match you want to change")
        print()

        the_match = None
        match_id = input("Enter match id: ")
        match_list = self.logic_wrapper.get_all_match_results()
        for match in match_list:
            if match.id == match_id:
                the_match = match
        if the_match == None:
            print("No match found with match id:{}".format(match_id))
            return
        #if match_id in self.logic_wrapper.get_all_match_results():
        #match_list = self.logic_wrapper.get_all_match_results(match_id)
        
        
        print()
        new_date = input("Enter new date(dd.mm.yyyy): ")
        
        the_match.date = new_date
        self.logic_wrapper.update_match(the_match)
        

        
    
        #self.logic_wrapper.update_match(match_list)           