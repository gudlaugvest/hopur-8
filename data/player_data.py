import csv
from model.player_model import Player


class Player_Data:
    def __init__(self):
        self.file_name = "file/player.csv"
            

    def create_player(self, player):
        """Create Player and write into a csvfile named player.csv"""
        with open(self.file_name, "a", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["name", "ss_number", "home_address", "phone_number", "email_address", "role", "team_id"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({"name": player.name, "ss_number": player.ss_number, "home_address": player.home_address, "phone_number": player.phone_number, "email_address": player.email_address, "role": player.role, "team_id": player.team_id })


    def read_all_players(self):
        """Return all player attributes that are in player.csv file"""
        player_list = []
        with open(self.file_name, newline="" ,encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                player_list.append(Player(row["name"], row["ss_number"],row["home_address"], row["phone_number"], row["email_address"],row["role"], row["team_id"]))
        return player_list

    def get_player_by_name(self, name):
        """Loop through player.csv and get name of player"""
        all_players = self.read_all_players()
        for player in all_players:
            if player.name == name:
                return player
    
    def get_player_by_id(self, ss_number):
        """Loop through player.csv and get social security number"""
        all_players = self.read_all_players()
        for player in all_players:
            if player.ss_number == ss_number:
                return player
    
    def get_players_by_team_id(self, team_id):
        """Loop through player.csv and get players with the same team id"""
        all_players = self.read_all_players()
        players = []
        for player in all_players:
            if player.team_id == team_id:
                players.append(player)
        return players

    def add_player_to_team(self, p):
        """Add player to team"""
        player_list = self.read_all_players()
        for player in player_list:
            if p.ss_number == player.ss_number:
                player.team_id = p.team_id
        with open(self.file_name,mode='w', newline="" ,encoding="utf-8") as csvfile:
            fieldnames = ['name','ss_number','home_address','phone_number','email_address','role','team_id']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for player in player_list:
                writer.writerow({"name": player.name, "ss_number": player.ss_number, "home_address": player.home_address, "phone_number": player.phone_number, "email_address": player.email_address, "role": player.role, "team_id": player.team_id })

    
    def assign_captain(self, p):
        """Assign Captain"""

        # This function should allow user to assign a captain to a team
        # The captain should be a player in the team
        # 

        player_list = self.read_all_players()
        for player in player_list:
            if p.ss_number == player.ss_number:
                player.role = p.role
        with open(self.file_name,mode='w', newline="" ,encoding="utf-8") as csvfile:
            fieldnames = ['name','ss_number','home_address','phone_number','email_address','role','team_id']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for player in player_list:
                writer.writerow({"name": player.name, "ss_number": player.ss_number, "home_address": player.home_address, "phone_number": player.phone_number, "email_address": player.email_address, "role": player.role, "team_id": player.team_id })

       
