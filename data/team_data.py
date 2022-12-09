import csv
from model.team_model import Team

class Team_Data:

    def __init__(self):
        self.file_name = "file/team.csv"

    def create_team(self, team: Team):
        """Create Team and write into a csv file named team.csv"""
        i = len(self.get_all_teams()) + 1
        with open(self.file_name, "a", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["id", "name", "club", "captain_id"] 
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({"id": i, "name": team.name, "club": team.club, "captain_id": team.captain_id})

    def get_all_teams(self):
        """Return all team attributes that are in teams.csv"""
        team_list = []
        with open(self.file_name, newline="" ,encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                team_list.append(Team(row["id"], row["name"], row["club"], row["captain_id"]))
        return team_list

    def get_captain(self, team_id):
        """Get captain ssn number from player.csv file and return that player if captain is not found return None"""
        the_team = self.get_team_by_Id(team_id)
        players = self.data_wrapper.get_all_players()
        for player in players:
            if player.ss_number == the_team.captain_id:
                return player
        return 
    
    def get_team_by_Id(self, team_id):
        """Loop through team.csv and get team id"""
        all_teams = self.get_all_teams()
        for team in all_teams:
            if team.id == team_id:
                return team

    
    
    
    #    teams = self.get_all_teams()
    #    correct_team = None
    #    for team in teams:
    #        if team.captain_id == team_id:
    #            correct_team = team
    #            return correct_team.captain_id
    #    return None


    def get_team_by_name(self, name):
        """Loop through team.csv and get team name"""
        all_teams = self.get_all_teams()
        for team in all_teams:
            if team.name == name:
                return team


    def get_team_by_captain_id(self, captain_id):
        """Loop through team.csv and get captain ssn"""
        all_teams = self.get_all_teams()
        for team in all_teams:
            if team.captain_id == captain_id:
                return team

    def get_team_name_by_team_id(self, team_id):
        """Loop through team.csv and get team name using team id"""
        all_teams = self.get_all_teams()
        for team in all_teams:
            if team.id == team_id:
                return team.name


    def assign_captain_to_team(self, p):
        """Assign captain to team"""
        player_list = self.read_all_players()
        
        for player in player_list:
            player.role = p.role
        with open(self.file_name,mode='w', newline="" ,encoding="utf-8") as csvfile:
            fieldnames = ['name','ss_number','home_address','phone_number','email_address','role','team_id']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for player in player_list:
                writer.writerow({"name": player.name, "ss_number": player.ss_number, "home_address": player.home_address, "phone_number": player.phone_number, "email_address": player.email_address, "role": player.role, "team_id": player.team_id })

       

            
