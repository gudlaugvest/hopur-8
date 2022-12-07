

from model.club_model import Club


class Club_UI:
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection

    def menu_output(self):
        print()
        print("####################################\n")
        print("Club\n".rjust(19))
        print("c. Continue To Create Club")
        print("b. Go Back To Organizer Menu\n")

    def input_prompt(self):
        self.menu_output()
        command = input("Enter Command: ")
        if command == "b":
            return "b"
        elif command == "c":
            club = Club()
            print()
            club.name = input("Enter Name: ")
            club.home_address = input("Enter Home Address: ")
            club.phone_number = input("Enter Phone Number(0000000): ")
            while len(club.phone_number) != 7:
                print()
                print("Phone number incorrect! Please try again!")
                club.phone_number = input("Enter Phone Number(0000000): ")
            self.logic_wrapper.create_club(club)
        else:
            print()
            print("Invalid input, please try again!")