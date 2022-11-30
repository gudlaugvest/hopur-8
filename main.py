from ui.main_menu_ui import MainMenu_UI
from ui.tournament_organizer_ui import Tournament_Organizer_UI
from ui.tournament_ui import Tournament_UI

mainmenu = MainMenu_UI()
mainmenu.input_prompt()

organizermenu = Tournament_Organizer_UI()
organizermenu.input_prompt()

tournamentmenu = Tournament_UI()
tournamentmenu.input_prompt()
