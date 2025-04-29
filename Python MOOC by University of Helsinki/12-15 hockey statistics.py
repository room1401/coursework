# Write your solution here
import json

class Player():
    def __init__(self, name, team, game, goal, asst):
        self.__name = name
        self.__team = team
        self.__game = game
        self.__goal = goal
        self.__asst = asst

    def game(self):
        return self.__game

    def goal(self):
        return self.__goal

    def pts(self):
        return self.__goal + self.__asst

    def __str__(self) -> str:
        return f"{self.__name:21}{self.__team}{self.__goal:4} + {self.__asst:2} = {self.pts():3}"


class Table:
    def __init__(self) -> None:
        self.__players = {}
        self.__teams = {}
        self.__ctry = {}

    def create_table(self, data: list):
        for p in data:
            name, team, nation = p["name"], p["team"], p["nationality"]
            self.__players[name] = Player(name, team, int(p["games"]), int(p["goals"]), int(p["assists"]))
            self.__teams[team] = self.__teams.get(team, []) + [name]
            self.__ctry[nation] = self.__ctry.get(nation, []) + [name]

    def search(self, name:str):
        if name in self.__players:
            return self.__players[name]

    def teams(self):
        return self.__teams
    
    def ctry(self):
        return self.__ctry

    def sort_team(self, team):
        players = [self.__players[x] for x in self.teams()[team]]
        return sorted(players, key=lambda x: x.pts(), reverse=True)

    def sort_ctry(self, ctry):
        players = [self.__players[x] for x in self.ctry()[ctry]]
        return sorted(players, key=lambda x: x.pts(), reverse=True)

    def sort_pt(self):
        return sorted(self.__players.values(), key=lambda x: (x.pts(), x.goal()), reverse=True)

    def sort_go(self):
        return sorted(self.__players.values(), key=lambda x: (x.goal(), -x.game()), reverse=True)


class FileHandler:
    def __init__(self, filename):
        with open(filename) as file:
             self.__data = json.load(file)

    def data(self):
        return self.__data

class App:
    def __init__(self):
        self.__db = Table()
    
    def load(self, filename):
        data = FileHandler(filename).data()
        print(f"read the data of {len(data)} players")
        self.__db.create_table(data)

    def help(self):
        menu = ["\ncommands:", "0 quit", "1 search for player", "2 teams", "3 countries", \
                "4 players in team", '5 players from country', "6 most points", "7 most goals"]
        print("\n".join(menu))

    def search(self):
        name = input("name: ")
        print(f"\n{self.__db.search(name)}")

    def show_teams(self):
        for team in sorted(self.__db.teams().keys()):
            print(team)

    def show_ctry(self):
        for nat in sorted(self.__db.ctry().keys()):
            print(nat)

    def sort_team(self):
        team = input("team: ")
        for player in self.__db.sort_team(team):
            print(player)

    def sort_ctry(self):
        country = input("country: ")
        for player in self.__db.sort_ctry(country):
            print(player)

    def most_pt(self):
        rank = int(input("how many: "))
        for i in range(rank):
            print(self.__db.sort_pt()[i])

    def most_go(self):
        rank = int(input("how many: "))
        for i in range(rank):
            print(self.__db.sort_go()[i])

    def run(self):
        fname = input("\nfile name: ")
        self.load(fname)
        self.help()
        actions = {"1": self.search, "2": self.show_teams, "3": self.show_ctry, \
                   "4": self.sort_team, "5": self.sort_ctry, "6": self.most_pt, \
                   "7": self.most_go}
        
        while True:
            command = input("\ncommand: ")
            if command == "0":
                break
            if command in actions:
                actions[command]()


application = App()
application.run()
