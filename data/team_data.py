import csv
from model.team_model import Team

class Team_Data:

    def __init__(self):
        self.file_name = "file/team.csv"

    def create_team(self, team: Team):
        i = len(self.get_all_teams()) + 1
        with open(self.file_name, "a", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["id", "name", "club", "captain_id"] 
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({"id": i, "name": team.name, "club": team.club, "captain_id": team.captain_id})

    def get_all_teams(self):
        team_list = []
        with open(self.file_name, newline="" ,encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                team_list.append(Team(row["id"], row["name"], row["club"], row["captain_id"]))
        return team_list

    def get_captain(self, team_id):
        the_team = self.get_team_by_Id(team_id)
        players = self.data_wrapper.get_all_players()
        for player in players:
            if player.ss_number == the_team.captain_id:
                return player
        return None
    
    def get_team_by_Id(self, team_id):
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
        all_teams = self.get_all_teams()
        for team in all_teams:
            if team.name == name:
                return team


    def get_team_by_captain_id(self, captain_id):
        all_teams = self.get_all_teams()
        for team in all_teams:
            if team.captain_id == captain_id:
                return team