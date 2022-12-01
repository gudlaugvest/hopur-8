import csv
from model.tournament_model import Tournament

class Clubs_Data:
    
    def __init__(self):
        self.file_name = "data/clubs.csv"
    
    def create_club(self, tournament):
        with open(self.file_name, "a", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["name", "home_address", "phone_number"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({"name": tournament.name, "home_address": tournament.home_address, "phone_number": tournament.phone_number})

    def get_all_players(self):
        player_list = []
        with open(self.file_name, newline="" ,encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                player_list.append(Tournament(row["name"], row["home_address"], row["phone_number"]))
        return player_list
