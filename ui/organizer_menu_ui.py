from ui.club_ui import Club_UI
from ui.player_ui import Player_UI
from ui.team_ui import Team_UI
from ui.tournament_ui import Tournament_UI
from ui.match_ui import Match_UI

class Organizer_Menu_UI:
    def __init__(self, logic_wrapper):
        self.logic_wrapper = logic_wrapper


    def menu_output(self):
        print()
        print("############################")
        print()
        print("Organizer Menu".rjust(18))
        print()
        print("1. Club")
        print("2. Team")
        print("3. Player")
        print("4. Tournament")
        print("5. Matches")
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
                quit()
            elif command == "1":
                club = Club_UI(self.logic_wrapper)
                club.input_prompt()
            elif command == "2":
                team = Team_UI(self.logic_wrapper)
                team.input_prompt()
            elif command == "3":
                player_ui = Player_UI(self.logic_wrapper)
                player_ui.input_prompt()
            elif command == "4":
                tournament_ui = Tournament_UI(self.logic_wrapper)
                tournament_ui.input_prompt()
            elif command == "5":
                match_ui = Match_UI(self.logic_wrapper)
                match_ui.input_prompt()
            else:
                print()
                print("Invalid input, please try again!")
