
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
        all_teams = self.logic_wrapper.get_all_teams()
        print("Team captains:")
        for team in all_teams:
            captain = self.logic_wrapper.get_captain(team_id=team.id)
            print(captain.ssn_number, captain.name)
        print()

        captain_id = input("Enter captain id: ")
        captain = self.logic_wrapper.get_player_by_id(captain_id)
        if captain is None:
            print()
            print("No captain with this id! Try again")
            return
        
        team = self.logic_wrapper.get_team_by_captain_id(captain_id)
        if team == None:
            print()
            print("No team found with this captain! Try again")
            return
        
        team_players = self.logic_wrapper.get_players_by_team_id(team.id)
        if len(team_players) < 4:
            print()
            print("Not enough players in this team!")
            return
        
        print("Players in this team:")
        for player in team_players:
            print(player.ssn_number, player.name)
        print()

        
        

       


        
   





