
class Register_UI:
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection


    def menu_output(self):
        print()
        print("############################")
        print()
        print("Register final match".rjust(18))
        print()


    def input_prompt(self):
        self.menu_output()
        player = Player()
        counter = 0
        while counter <=3:
            player.name = input("Enter name of Player: ")
            player.id_number = input("Enter id number: ")
            player.home_address = input("Enter home address: ")
            player.phone_number = input("Enter phone number: ")
            player.email_address = input("Enter email address: ")
            print()
            counter += 1
            self.logic_wrapper.create_player(player)