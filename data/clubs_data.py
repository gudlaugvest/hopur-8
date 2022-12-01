import csv
from model.tournament_model import Tournament

class Clubs_Data:
    
    def __init__(self):
        self.file_name = "file/clubs.csv"
    

    def create_club(self, tournament):
        i = len(self.get_all_clubs()) + 1
        with open(self.file_name, "a", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["name", "home_address", "phone_number"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({"id" : i, "name": tournament.name, "home_address": tournament.home_address, "phone_number": tournament.phone_number})

    def get_all_clubs(self):
        club_list = []
        with open(self.file_name, newline="" ,encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                club_list.append(Tournament(row["name"], row["home_address"], row["phone_number"]))
        return club_list
