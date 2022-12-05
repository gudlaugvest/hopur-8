

from model.club_model import Club


class Club_UI:
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection

    def menu_output(self):
        print()
        print("############################\n")
        print("Club\n".rjust(18))
        print("c. Continue")
        print("b. Go back\n")

    def input_prompt(self):
        self.menu_output()
        command = input("Enter command: ")
        if command == "b":
            return "b"
        elif command == "c":
            club = Club()
            club.name = input("Enter name: ")
            club.home_address = input("Enter home address: ")
            club.phone_number = input("Enter phone number: ")
            self.logic_wrapper.create_club(club)