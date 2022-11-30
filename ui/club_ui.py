

from model.club_model import Club


class Club_UI:
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection

    def menu_output(self):
        print()
        print("############################")
        print()
        print("Club".rjust(18))
        print()


    def input_prompt(self):
        while True:
            self.menu_output()
            print()
            club = Club()
            club.name = input("Enter name of organizer: ")
            club.home_address = input("Enter Tournament name: ")
            club.phone_number = input("Enter number of rounds: ")