import csv
from model.player_model import Player


class Player_Data:
    def __init__(self):
        self.file_name = "data\player.csv"
            

    def create_player(self, player):
        i = len(self.get_all_players()) + 1
        with open(self.file_name, "a", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["id", "name", "id_number", "home_address", "phone_number", "email_address", "team"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({"id" : i, "name": player.name, "id_number": player.id_number, "home_address": player.home_address, "phone_number": player.home_address, "email_address": player.email_address, "team": player.team})
#id,name,id_number,home_address,phone_number,email_address,team
    def get_all_players(self):
        player_list = []
        with open(self.file_name, newline="" ,encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                player_list.append(Player(row["id"], row["name"], row["id_number"],row["home_address"], row["phone_number"], row["email_address"], row["team"]))
        return player_list




