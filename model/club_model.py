class Club:
    def __init__(self, name = "", home_address = "", phone_number = "") -> None:
        self.name = name
        self.home_address = home_address
        self.phone_number = phone_number

    def __str__(self) -> str:
        return f"Club's name: {self.name}, Home address: {self.home_address}, Phone number: {self.phone_number}"