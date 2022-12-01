import csv
from model.captain_model import Captain

class Captain_data:

    def __init__(self):
        self.file_name = "file/captain.csv"

    def create_team(self, captain: Captain):
        i = len(self.get_all_teams()) + 1
        with open(self.file_name, "a", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["name", "id"] 
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({"name": captain.name, "id": i})

    def get_all_teams(self):
        captain_list = []
        with open(self.file_name, newline="" ,encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                captain_list.append(Captain(row["name"], row["id"]))
        return captain_list