import csv
from model.tournament_model import Tournament
from datetime import datetime

class Tournament_Data:

    def __init__(self):
        self.file_name = "file/tournament.csv"


      
    def create_tournament(self, tournament: Tournament):
        '''this function creates a tournament''' 
        i = len(self.get_all_tournaments()) + 1
        with open(self.file_name, "a", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["id", "name", "start_date", "end_date"] 
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({"id": i,"name": tournament.name, "start_date": tournament.start_date, "end_date": tournament.end_date})
       
        
    def get_all_tournaments(self):
        tournament_list = []
        with open(self.file_name, newline="" ,encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                start_date = row['start_date']
                end_date = row['end_date']
                #starting_date = datetime(year=start_date.split('.')[2], month=start_date.split('.')[1], day=start_date.split('.')[0])
                #ending_date = datetime(year=end_date.split('.')[2], month=end_date.split('.')[1], day=end_date.split('.')[0])
                tournament_list.append(Tournament(row["id"], row["name"],row["start_date"], row["end_date"]))
        return tournament_list

    def update_tournament(self, tournament):
        tournament_list = self.get_all_tournaments()
        for i in range(len(tournament_list)):
            if tournament.id == tournament_list[i].id:
                tournament_list[i] = tournament
        

        with open(self.file_name, "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["id", "name", "start_date", "end_date"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for i in range(len(tournament_list)):
                writer.writerow({"id": tournament_list[i].id, "name": tournament_list[i].name, "start_date": tournament_list[i].start_date, "end_date": tournament_list[i].end_date})
                
        
        
               

    def register_type_of_match(self):
        '''This function specifies what type of match'''
        pass

    def get_all_games_in_tournament(self, tournament):
        pass