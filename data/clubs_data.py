import csv
from model.club_model import Club

class Clubs_Data:
    
    def __init__(self):
        self.file_name = "file/clubs.csv"
    
    def create_club(self, club):
        """Create Club and write into a csv file named clubs.csv"""
        i = len(self.get_all_clubs()) + 1
        with open(self.file_name, "a", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["id", "name", "home_address", "phone_number"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({"id" : i, "name": club.name, "home_address": club.home_address, "phone_number": club.phone_number})

    def get_all_clubs(self):
        """Return all club attributes that are in clubs.csv file """
        club_list = []
        with open(self.file_name, newline="" ,encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                club_list.append(Club(row["name"], row["home_address"], row["phone_number"]))
        return club_list


    def get_club_by_name(self, name):
        """Loop through clubs.csv file and return Club name if no Club name is found return None"""
        all_clubs = self.get_all_teams()
        for club in all_clubs:
            if club.name == name:
                return club
        return None

