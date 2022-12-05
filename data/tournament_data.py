import csv
from model.tournament_model import Tournament

class Tournament_Data:

    def __init__(self):
        self.file_name = "file/tournament.csv"


      
    def create_tournament(self, tournament: Tournament):
        '''this function creates a tournament''' 
        i = len(self.get_all_tournaments()) + 1
        with open(self.file_name, "a", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["id", "name", "number_of_rounds", "date"] 
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({"id": i,"name": tournament.name, "number_of_rounds": tournament.number_of_rounds, "date": tournament.date})

    def get_all_tournaments(self):
        tournament_list = []
        with open(self.file_name, newline="" ,encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                tournament_list.append(Tournament(row["id"], row["name"], row["number_of_rounds"],row["date"]))
        return tournament_list

    def register_type_of_match(self):
        '''This function specifies what type of match'''
        pass

    def get_all_games_in_tournament(self, tournament):
        pass