
class Register_Score:
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection


    def menu_output(self):
        print()
        print("####################################")
        print()
        print("Register Score".rjust(23))
        print()
        

    def input_prompt(self):
        #self.menu_output()
        #print()
        while True:
            pass
            self.menu_output()
            print()
            get_all_teams = self.logic_wrapper.get_all_teams()
            captain_id = input("Enter your id: ")
            # Nú þarf forritið að taka inn id hjá captain og fær þá leikina sem hann er captain í
            right_team = self.logic_wrapper.get_team_by_captain_id() # Ef til er klasi fyrir það
            # If team_captain er í home team þá getur hann skrifað inn result af leiknum *(ef leikurinn er búinn)


            # Basic algorithm af hvað á að koma hérna
            # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            # Birta lista af öllum team captains
            # Velja úr þeim lista eftir kennitölu eða id fyrir framan
            # Hver team captain ætti aðeins að gera einu sinni results (held ég skildi þetta sem þannig)
            # Svo er spurt hver spilaði hvaða leik 4x501...... hafa lista af spilurum úr baðum liðum
            # Svo er beðið um result (for loopa sem er farið í gegnum 7 sinnum) (wihle loopu með counter upp í 7 (0-6))
            # á meðan counter er á milli 0-3 þá eru 501 leikir
            # á meðan counter er 4 þá er 301 leikur
            # á meðan counter er 5 þá er cricket 
            # á meðan counter er 6 þá er 501 leikur