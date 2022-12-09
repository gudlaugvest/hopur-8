PLAYER_SSN = 'SSN'
PLAYER_NAME = 'NAME'
ROLE = 'ROLE'
TEAM_NAME = 'TEAM'

from ui.game_ui import Game_UI

class Register_Score:

    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection


    def menu_output(self):
        print()
        print("####################################")
        print()
        print("Register Score".rjust(23))
        print()
        

    def input_prompt(self):

        self.menu_output()
        print()          
        
        print("Team Captains:")
        all_teams = self.logic_wrapper.get_all_teams()
        captainlist = []
        for team in all_teams:
            captain = self.logic_wrapper.get_captain(team.id)
            captainlist.append(captain.ss_number)
            print("Captain ssn: {:<6} | Captain Name: {:<6} | Team: {:<6}".format(captain.ss_number, captain.name, captain.team_id))
        print()

        captain_id = input("Enter Captain id: ")
        while captain_id not in captainlist:
            print("Þetta er ekki gilt captain id, reyndu aftur")
            captain_id = input("Enter Captain id: ")

        # Biðjum um captain_id og þá fáum við lista af öllum sem eru í liðinu hans
        print()
        print("Players in this team".rjust(23))
        print()

        captain_team = self.logic_wrapper.get_team_by_captain_id(captain_id)
        players = self.logic_wrapper.get_all_players()
        for player in players:
            if player.team_id == captain_team.id:
                print("Player ssn: {:<6} | Player Name: {:<6} | Role: {:<12}| Team: {:<6}".format(player.ss_number, player.name, player.role, captain_team.name))
          
        # Finna hvaða leik þetta lið er að keppa í og birta upp eins og t.d.
        print()
        print()
        print("Matches that the team is playing: ")
        matches = self.logic_wrapper.get_all_match_results()
        matchlist = []
        for match in matches:
            if match.home_team_id == captain_team.id:
                matchlist.append(match.id)
                home_team_name = self.logic_wrapper.get_team_name_by_team_id(match.home_team_id)
                away_team_name = self.logic_wrapper.get_team_name_by_team_id(match.away_team_id)
                print("Match id: {:<6} | Home Team: {:<6} :versus: Away Team: {:<6}".format(match.id, home_team_name, away_team_name))
        print()
        
        
        match_id = input("Enter match-id for your game: ")
        while match_id not in matchlist:
            print("Þetta er ekki gilt match id, reyndu aftur")
            match_id = input("Enter match-id for your game: ")
        print()
        print("Players in this match".rjust(23))
        print()
        match = self.logic_wrapper.get_match_by_id(match_id)
        while match is None:
            print("Invalid match id")
            match_id = input("Enter match-id for your game: ")
            match = self.logic_wrapper.get_match_by_id(match_id)
            
        players = self.logic_wrapper.get_all_players()
        
        
        
        print("{:<24} {:<24} {:<24} {:<24}".format(PLAYER_SSN, PLAYER_NAME, ROLE, TEAM_NAME))
        
        print("Players in home team")
        print()
        hometeamplayers = []
        for player in players:
            if player.team_id == match.home_team_id:
                hometeamplayers.append(player.ss_number)
                print("{:<24} {:<24} {:<24} {:<24}".format(player.ss_number, player.name, player.role, player.team_id))
        print()
        
        print("Players in Away team")
        print()
        awayteamplayers = []
        for player in players:
            if player.team_id == match.away_team_id:
                awayteamplayers.append(player.ss_number)
                print("{:<24} {:<24} {:<24} {:<24}".format(player.ss_number, player.name, player.role, player.team_id))
        print()
        
        game = Game_UI(self.logic_wrapper)
        game.input_prompt(match_id) # Kalla á ui fall sem mun sjá um að setja inn stig fyrir hvern leik
        # Síðan þarf að slá inn ssn fyrir hvaða leikmaður spilaði hvaða leik og líka ssn hjá player í away team
