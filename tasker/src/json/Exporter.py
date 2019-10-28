import json


class Exporter:

    def __init__(self):
        pass

    def save_tasks(self, tasks):
        with open('taski.json', 'w') as zapis:
            json.dump(tasks, zapis)

        # zapisz taski do pliku tutaj
        pass
