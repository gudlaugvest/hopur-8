import csv
from model.tournament_model import Tournament
from datetime import datetime

class Tournament_Data:

    def __init__(self):
        self.file_name = "file/tournament.csv"


      
    def create_tournament(self, tournament: Tournament):
        '''Create Tournament and write into a csv file named clubs.csv''' 
        i = len(self.get_all_tournaments()) + 1
        with open(self.file_name, "a", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["id", "name", "start_date", "end_date"] 
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({"id": i,"name": tournament.name, "start_date": tournament.start_date, "end_date": tournament.end_date})

    def update_tournament(self, tournament):
        """Update date of match"""
        all_tournament = self.get_all_tournaments()
        for i in range(len(all_tournament)):
            if tournament.id == all_tournament[i].id:
                all_tournament[i] = tournament
        
        with open(self.file_name, "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["id", "name", "start_date", "end_date"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for i in range(len(all_tournament)):
                writer.writerow({"id": all_tournament[i].id, "name": all_tournament[i].name, "start_date": all_tournament[i].start_date, "end_date": all_tournament[i].end_date})

    def get_tournament_by_id(self, id):
        """Loop through matches.csv file and get match id"""
        all_tournament = self.get_all_tournaments()
        for tournament in all_tournament:
            if tournament.id == id:
                return tournament   
        
    def get_all_tournaments(self):
        """Return all tournament attributes that are in tournament.csv file"""
        tournament_list = []
        with open(self.file_name, newline="" ,encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                #start_date = row['start_date']
                #end_date = row['end_date']
                #starting_date = datetime(year=start_date.split('.')[2], month=start_date.split('.')[1], day=start_date.split('.')[0])
                #ending_date = datetime(year=end_date.split('.')[2], month=end_date.split('.')[1], day=end_date.split('.')[0])
                tournament_list.append(Tournament(row["id"], row["name"],row["start_date"], row["end_date"]))
        return tournament_list
