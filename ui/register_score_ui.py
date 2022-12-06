
class Register_Score:
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection


    def menu_output(self):
        print()
        print("####################################")
        print()
        print("Register score".rjust(23))
        print()
        

    def input_prompt(self):
        #self.menu_output()
        #print()
        while True:
            pass
            self.menu_output()
            print()
            get_all_teams = self.logic_wrapper.get_all_teams()
            captain_id = input("Enter your id: ")
            # Nú þarf forritið að taka inn id hjá captain og fær þá leikina sem hann er captain í
            right_team = self.logic_wrapper.get_team_by_captain_id() # Ef til er klasi fyrir það
