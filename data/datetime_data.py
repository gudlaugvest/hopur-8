import csv
from model.datetime_model import Datetime

class Datetime_Data:
    
    def __init__(self):
        self.file_name = "file/datetime.csv"
    
    def create_date(self, date):
        with open(self.file_name, "a", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["day", "month", "year"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({"day" : date.day, "month": date.month, "year": date.year})

    def get_all_dates(self):
        date_list = []
        with open(self.file_name, newline="" ,encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                date_list.append(Datetime(row["day"], row["month"], row["year"]))
        return date_list
