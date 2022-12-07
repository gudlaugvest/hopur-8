import csv
from model.player_model import Player


class Player_Data:
    def __init__(self):
        self.file_name = "file/player.csv"
            

    def create_player(self, player):
        with open(self.file_name, "a", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["name", "ss_number", "home_address", "phone_number", "email_address", "role", "team_name"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({"name": player.name, "ss_number": player.ss_number, "home_address": player.home_address, "phone_number": player.phone_number, "email_address": player.email_address, "role": player.role, "team_name": player.team_name })


    def read_all_players(self):
        player_list = []
        with open(self.file_name, newline="" ,encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                player_list.append(Player(row["name"], row["ss_number"],row["home_address"], row["phone_number"], row["email_address"],row["role"], row["team_name"]))
        return player_list

    def get_player_by_name(self, name):
        all_players = self.read_all_players()
        for player in all_players:
            if player.name == name:
                return player
    
    def get_player_by_id(self, ss_number):
        all_players = self.read_all_players()
        for player in all_players:
            if player.ss_number == ss_number:
                return player
    
    def get_players_by_team_id(self, team_id):
        all_players = self.read_all_players()
        players = []
        for player in all_players:
            if player.team_id == team_id:
                players.append(player)
        return players

    
