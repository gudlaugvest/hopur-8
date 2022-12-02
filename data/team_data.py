import csv
from model.team_model import Team

class Team_Data:

    def __init__(self):
        self.file_name = "file/team.csv"

    def create_team(self, team: Team):
        i = len(self.get_all_teams()) + 1
        with open(self.file_name, "a", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["id", "name", "captain_id", "club"] 
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({"id": i, "name": team.name, "captain_id": team.captain_id, "club": team.club})

    def get_all_teams(self):
        team_list = []
        with open(self.file_name, newline="" ,encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                team_list.append(Team(row["id"], row["name"], row["club"]))
        return team_list
