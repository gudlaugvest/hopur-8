class Organizer_Menu_UI:
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection


    def menu_output(self):
        print()
        print("############################")
        print()
        print("".rjust(18))
        print()
        print("1. Club")
        print("2. Team")
        print("3. Player")
        print("4. Get info on tournament")
        print("5. Postpone matches")
        print("b. Go Back")



    def input_prompt(self):
        while True:
            self.menu_output()
            print()
            command = input("Enter your command: ")
            command = command.lower()
            if command == "b":
                return "b"
            elif command == "q":
                return "q"
            elif command == "1":
                club = Club_UI()
            elif command == "2":
                result = self.player_logic.get_all_players()
                for element in result:
                    print("name: {}, id_number: {}, home_address: {}, phone_number: {}, email_address: {}, team: {}".format(element.name, element.id_number, element.home_address, element.phone_number, element.email_address, element.team))
            else:
                print("Invalid input, try again!")