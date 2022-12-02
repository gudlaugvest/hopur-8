import csv
from model.captain_model import Captain

class Captain_data:

    def __init__(self):
        self.file_name = "file/captain.csv"

    def create_captain(self, captain: Captain):
        #i = len(self.get_all_teams()) + 1
        with open(self.file_name, "a", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["id_number"] 
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({"id_number": captain.id_number})

    def get_captain(self):
        captain_list = []
        with open(self.file_name, newline="" ,encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                captain_list.append(Captain(row["id_number"]))
        return captain_list

    