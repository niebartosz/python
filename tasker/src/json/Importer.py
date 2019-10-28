import json


class Importer:

    def __init__(self):

        pass

    def read_tasks(self):
        with open ('taski.json','r', encoding='utf-8') as odczyt:
            self.tasks = json.load(odczyt)



        # odczytaj plik i zdekoduj treść tutaj
        pass

    def get_tasks(self):


        # zwróć zdekodowane taski tutaj
        return self.tasks