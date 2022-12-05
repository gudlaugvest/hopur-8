from ui.main_menu_ui import MainMenu_UI
from ui.tournament_ui import Tournament_UI
from ui.club_ui import Club_UI
from data.player_data import Player_Data


mainmenu = MainMenu_UI()
mainmenu.input_prompt()


tournamentmenu = Tournament_UI()
tournamentmenu.input_prompt()

clubmenu = Club_UI()
clubmenu.input_prompt()