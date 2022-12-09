
class General_User_UI:
    def __init__(self, logic_wrapper):
        self.logic_wrapper = logic_wrapper


    def menu_output(self):
        """Print out General User Menu and options"""
        print()
        print("####################################")
        print()
        print(" Menu".rjust(20))
        print()
        print("1. Get list of players and teams")
        print("2. Get list of matches and scores")
        print("3. Get list of unplayed matches")
        print("4. Get status of tournament")
        print("b. Go back")
        print("q. Quit")


    def input_prompt(self):
        """Get user input"""
        while True:
            self.menu_output()
            print()
            command = input("Enter Command: ")
            command = command.lower()
            if command == "b":
                break
            elif command == "q":
                quit()
            elif command == "1":
                teams = self.logic_wrapper.get_all_teams()
                players = self.logic_wrapper.get_all_players()
                for team in teams:
                    print()
                    print(f"Team name: {team.name}")
                    print()
                    for player in players:
                        if team.id == player.team_id:
                            print(player)
            
            elif command == "2":
                print("Played Matches: \n".rjust(72))
                print()
                all_matches = self.logic_wrapper.get_all_match_results()
                all_games = self.logic_wrapper.get_all_games()
                # Þarf að fá þá ssn hjá einum af home team og einum af away team til að skrifa fyrir ofan hvert match sem prentast út
                print("Home team players SSN", "Scores".rjust(36), "Away team players SSN".rjust(40), "Type of game".rjust(30), "Match ID".rjust(20))
                print()
                print()
                # correct_match = None
                # for match in all_matches:
                #     if match.id == all_games.match_id:
                #         correct_match = match
                #         print(f"{correct_match.home_team_player_id} vs {correct_match.away_team_player_id}".rjust(50))
                for game in all_games:
                    print(game)
                

                # for match in all_matches:
                #     for game in all_games:
                #         if match.id == game.match_id:
                         
                #             print(match)
                    
                    
           
            elif command == "3":
            # Á að geta fengið lista af óspiluðum leikjum þ.þ.e.a.s leikir sem date > current date
                todays_date = '06.12.2022'
                list_of_unplayed_matches = self.logic_wrapper.unplayed_matches(todays_date)
                for matches in list_of_unplayed_matches:
                    if todays_date < matches.date:
                        print(matches)
                    print()
            
            elif command == "4":
                list_of_status_tournament = self.logic_wrapper.get_all_tournaments()
                print("Tournament:", "begins:".rjust(10), "ends:".rjust(20))
                print()
                for status in list_of_status_tournament:
                    print(status)
            
            else:
                print("Invalid input, try again!")