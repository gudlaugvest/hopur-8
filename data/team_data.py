import csv
from model.team_model import Team

class Team_Data:

    def __init__(self):
        self.file_name = "file/team.csv"

    def create_team(self, team):
        with open(self.file_name, "a", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["name", "team captain", "team players", "team club"] 
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({"name": team.name, "team_captain_id": team.team_captain, "team_players_ids": team.team_players, "team_club_id": team.team_club})

    def get_all_teams(self):
        team_list = []
        with open(self.file_name, newline="" ,encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                team_list.append(Team(row["id"], row["name"],row["team_captain_id"], row["team_players_ids"], row["team_club_id"]))
        return team_list
