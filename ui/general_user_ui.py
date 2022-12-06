from player_logic import Player_Logic

class General_User_UI:
    def __init__(self, logic_wrapper):
        self.logic_wrapper = logic_wrapper


    def menu_output(self):
        print()
        print("####################################")
        print()
        print(" Menu".rjust(20))
        print()
        print("1. Get list of players and teams")
        print("2. Get list of matches and scores")
        print("3. Get list of unplayed matches")
        print("4. Get status of tournament")
        print("b. Go back")
        print("q. Quit")


    def input_prompt(self):
        while True:
            self.menu_output()
            print()
            command = input("Enter your command: ")
            command = command.lower()
            if command == "b":
                break
            elif command == "q":
                quit()
            elif command == "1":
                logic_class = Player_Logic()
                result = logic_class.get_list_of_player_and_teams()
                for elem in result:
                    print(elem)
                
            elif command == "2":
                pass
            elif command == "3":
                pass
            elif command == "4":
                pass
            else:
                print()
                print("Invalid input, try again!")