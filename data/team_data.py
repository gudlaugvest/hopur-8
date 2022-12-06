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
                team_list.append(Team(row["id"], row["name"], row["club"]))
        return team_list

    def get_captain(self, team_id):
        teams = self.get_all_teams()
        correct_team = None
        for team in teams:
            if team.id == team_id:
                correct_team = team
                break
        players = self.data_wrapper.get_all_players()
        correct_player = None
        for player in players:
            if player.id == correct_team.team_captain:
                correct_player = player
                return correct_player
        return None


    def get_team_by_name(self, name):
        all_teams = self.get_all_teams()
        for team in all_teams:
            if team.name == name:
                return team