class Datetime_Logic:
    def __init__(self, data_connections):
        '''This function initializes the class'''
        self.data_wrapper = data_connections


    def create_date(self, date):
        self.data_wrapper.create_date(date)


    def get_all_dates(self):
        self.data_wrapper.get_all_dates()
