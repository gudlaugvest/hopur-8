import csv
from model.player_model import Player


class Player_Data:
    def __init__(self):
        self.file_name = "file/player.csv"
            

    def create_player(self, player):
        with open(self.file_name, "a", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["name", "ss_number", "home_address", "phone_number", "email_address", "role", "team_id"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({"name": player.name, "ss_number": player.ss_number, "home_address": player.home_address, "phone_number": player.phone_number, "email_address": player.email_address, "role": player.role, "team_id": player.team_id })


    def read_all_players(self):
        player_list = []
        with open(self.file_name, newline="" ,encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                player_list.append(Player(row["name"], row["ss_number"],row["home_address"], row["phone_number"], row["email_address"],row["role"], row["team_id"]))
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


""" 
    def update_player(self, player):
        players = self.read_all_players()
        for i in range(players):
            if players[i].id == player.id:
                players[i] = player

        with open(self.file_name, "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["name", "ss_number", "home_address", "phone_number", "email_address", "role", "team_name"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for p in players:
                writer.writerow({"name": p.name, "ss_number": p.ss_number, "home_address": p.home_address, "phone_number": p.phone_number, "email_address": p.email_address, "role": p.role, "team_name": p.team_name })
"""
        
    
"""
name,ss_number,home_address,phone_number,email_address,role,team_name
Jonni,0320002345,Laufrimi 13,8889999,jonni@ru.is,player,lið1
Gunni,0303032345,Gustav 13,565657585,gunni@ru.is,captain,lið1
Patti,0402012343,Vik 12,54642453,patti@ru.is,player,lið1
Stebbi,0912993456,Vikuvegur 98,8454675,stebbi@ru.is,player,lið1

"""