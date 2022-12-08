

from model.club_model import Club


class Club_UI:
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection

    def menu_output(self):
        """Print out Club Menu with options on what the user wants to do next"""
        print()
        print("####################################\n")
        print("Club\n".rjust(19))
        print("c. Continue To Create Club")
        print("b. Go Back To Organizer Menu\n")

    def input_prompt(self):
        """Get user input"""
        self.menu_output()
        command = input("Enter Command: ")
        if command == "b":
            return "b"
        elif command == "c":
            club = Club()
            print()
            club.name = input("Enter Name: ")
            club.home_address = input("Enter Home Address: ") 
            while True:
                try:
                    club.phone_number = input("Enter Phone Number(0000000): ")
                    if len(club.phone_number) == 7:
                        
                        break
                    else:
                        raise ValueError
                except ValueError:
                    print()
                    print ("Invalid phone number, try again")

            self.logic_wrapper.create_club(club)
        else:
            print("Invalid input, please try again!")