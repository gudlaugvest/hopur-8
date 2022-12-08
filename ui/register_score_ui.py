PLAYER_SSN = 'SSN'
PLAYER_NAME = 'NAME'
ROLE = 'ROLE'
TEAM_NAME = 'TEAM'



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
        #self.menu_output()
        #print()
    
        self.menu_output()
        print()          
        # Basic algorithm af hvað á að koma hérna:
        
        # Birta lista af öllum team captains
        # Velja úr þeim lista eftir kennitölu eða id fyrir framan
        # Hver team captain ætti aðeins að gera einu sinni results (held ég skildi þetta sem þannig)
        # Svo er spurt hver spilaði hvaða leik 4x501...... hafa lista af spilurum úr baðum liðum
        # Svo er beðið um result (for loopa sem er farið í gegnum 7 sinnum) (wihle loopu með counter upp í 7 (0-6))
        # á meðan counter er á milli 0-3 þá eru 501 leikir
        # á meðan counter er 4 þá er 301 leikur
        # á meðan counter er 5 þá er cricket 
        # á meðan counter er 6 þá er 501 leikur
        print("Team captains:")
        all_teams = self.logic_wrapper.get_all_teams()
        for team in all_teams:
            captain = self.logic_wrapper.get_captain(team.id)
            print("Captain ssn: {:<6} | Captain name: {:<6} | Team: {:<6}".format(captain.ss_number, captain.name, captain.team_id))
            #print(captain.ss_number, captain.name)
        print()

        captain_id = input("Enter captain id: ")
        # Biðjum um captain_id og þá fáum við lista af öllum sem eru í liðinu hans
        print()
        print("Players in this team".rjust(23))
        print()

        captain_team = self.logic_wrapper.get_team_by_captain_id(captain_id)
        players = self.logic_wrapper.get_all_players()
        for player in players:
            #captain_team_name = self.logic_wrapper.get_team_name_by_team_id(captain_team.id)
            if player.team_id == captain_team.id:
                print("Player ssn: {:<6} | Player name: {:<6} | Role: {:<12}| Team: {:<6}".format(player.ss_number, player.name, player.role, captain_team.name))
          
        # Finna hvaða leik þetta lið er að keppa í og birta upp eins og t.d.
        print()
        print()
        print("Leikur sem liðið er að spila: ")
        matches = self.logic_wrapper.get_all_match_results()
        for match in matches:
            #captain_team_name = self.logic_wrapper.get_team_by_name(captain_team.id)
            if match.home_team_id == captain_team.id:
                home_team_name = self.logic_wrapper.get_team_name_by_team_id(match.home_team_id)
                away_team_name = self.logic_wrapper.get_team_name_by_team_id(match.away_team_id)
                print("Match id: {:<6} | Home team: {:<6} :versus: Away team: {:<6}".format(match.id, home_team_name, away_team_name))
        print()
        
        # Velja síðan útfrá match id
        match_id = input("Sláðu inn match id fyrir þinn leik: ")
        print()
        print("Players in this match".rjust(23))
        print()
        match = self.logic_wrapper.get_match_by_id(match_id)
        players = self.logic_wrapper.get_all_players()
        #teams = self.logic_wrapper.get_all_teams()
        #self.logic_wrapper.get_players_from_team_id()
        
        
        print("{:<24} {:<24} {:<24} {:<24}".format(PLAYER_SSN, PLAYER_NAME, ROLE, TEAM_NAME))
        
        print("Players in home team")
        print()
        # birta út lista af leikmönnum í home_team
        for player in players:
            if player.team_id == match.home_team_id:
                print("{:<24} {:<24} {:<24} {:<24}".format(player.ss_number, player.name, player.role, player.team_id))
        print()
        
        print("Players in Away team")
        print()
        # birta út lista af leikmönnum í away_team
        for player in players:
            if player.team_id == match.away_team_id:
                print("{:<24} {:<24} {:<24} {:<24}".format(player.ss_number, player.name, player.role, player.team_id))
        print()
        
        
        # Síðan þarf að slá inn ssn fyrir hvaða leikmaður spilaði hvaða leik og líka ssn hjá player í away team
        
        
        
        
        # Svo þarf að slá inn result fyrir þann leik

        # get_match_by_team_id?




# ÞArf að sækja öll lið
# Þarft að finna liðin eftir nöfnunum á liðunum
# Svo getur þú kallað í get_players_by_team_id og kalla fyrir bæði liðin
# Þetta mun skila tveimur listum þ.a 1 listi fyrir home team og annar fyrir away team
