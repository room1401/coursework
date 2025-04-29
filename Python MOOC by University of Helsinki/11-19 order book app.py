# Write your solution here
# If you use the classes made in the previous exercise, copy them here
class Task:
    id = 1
    
    def __init__(self, desc, name, time):
        self.id = Task.id
        Task.id += 1
        self.description = desc
        self.programmer = name
        self.workload = time
        self.__is_finished = False

    def is_finished(self):
        return self.__is_finished
    
    def mark_finished(self):
        self.__is_finished = True

    def __str__(self) -> str:
        return f"{self.id}: {self.description} ({self.workload} hours), \
        programmer {self.programmer} {'' if self.__is_finished else 'NOT '}FINISHED"


class OrderBook:
    def __init__(self) -> None:
        self.__tasks = []
        self.__pgm = {}

    def add_order(self, desc, name, time):
        dummy = Task(desc, name, time)
        self.__tasks.append(dummy)
        self.__pgm[name] = self.__pgm.get(name, []) + [dummy.id]

    def all_orders(self):
        return self.__tasks

    def programmers(self):
        return list(self.__pgm.keys())

    def mark_finished(self, id: int):
        for task in self.__tasks:
            if task.id == id:
                task.mark_finished()
                return
        
        raise ValueError

    def finished_orders(self):
        return [x for x in self.__tasks if x.is_finished()]
        
    def unfinished_orders(self):
        return [x for x in self.__tasks if not x.is_finished()]

    def status_of_programmer(self, name: str):
        fin, f_time, uf_time = 0, 0, 0
        if name not in self.__pgm:
            raise ValueError
        
        for i in self.__pgm[name]:
            task = self.__tasks[i - 1]
            if task.is_finished():
                fin += 1
                f_time += task.workload
            else:
                uf_time += task.workload

        return (fin, len(self.__pgm[name]) - fin, f_time, uf_time)


class OrderApp:
    def __init__(self) -> None:
        self.__order = OrderBook()

    def help(self):
        menu = ["commands:", "0 exit", "1 add order", "2 list finished tasks", \
                "3 list unfinished tasks", "4 mark task as finished", \
                "5 programmers", "6 status of programmer"]
        print("\n".join(menu))

    def warning(self):
        print("erroneous input")

    def insert(self):
        desc = input("description: ")
        data = input("programmer and workload estimate: ").split()
        if len(data) < 2 or not data[1].isdigit():
            self.warning()
            return
        
        self.__order.add_order(desc, data[0], int(data[1]))
        print("added!")

    def list_fin(self):
        res = self.__order.finished_orders()
        if res:
            [print(x) for x in res]
        else:
            print("no finished tasks")

    def list_unfin(self):
        res = self.__order.unfinished_orders()
        if res:
            [print(x) for x in res]
        else:
            print("no unfinished tasks")

    def mark(self):
        id = input("id: ")
        if not id.isdigit() or int(id) < 0 or int(id) > len(self.__order.all_orders()):
            self.warning()
            return
        
        self.__order.mark_finished(int(id))
        print("marked as finished")

    def list_pgm(self):
        print([x for x in self.__order.programmers()])

    def stats(self):
        name = input("programmer: ")
        if name not in self.__order.programmers(): 
            self.warning()
            return
        
        done, pending, spent, remain = self.__order.status_of_programmer(name)
        print(f"tasks: finished {done} not finished {pending},", \
              f"hours: done {spent} scheduled {remain}")

    def execute(self):
        self.help()
        actions = {"1": self.insert, "2": self.list_fin, "3": self.list_unfin, \
                   "4": self.mark, "5": self.list_pgm, "6": self.stats}
        while True:
            command = input("\ncommand: ")
            if command == "0":
                break
            if command in actions:
                actions[command]()


application = OrderApp()
application.execute()
