from model.datetime_model import Datetime
from logic.logic_wrapper import Logic_Wrapper


class Datetime_UI:
    def __init__(self, logic_wrapper: Logic_Wrapper):
        self.logic_wrapper = logic_wrapper


    def input_prompt(self):

        date = Datetime()
        date.day = input("day: ")
        date.month = input("month: ")
        date.year = input("year: ")
        self.logic_wrapper.create_date(date)