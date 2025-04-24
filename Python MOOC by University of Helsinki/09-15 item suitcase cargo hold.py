# Write your solution here:
class Item:
    def __init__(self, name, weight):
        self.__name = name
        self.__weight = weight

    def name(self):
        return self.__name

    def weight(self):
        return self.__weight

    def __str__(self):
        return f"{self.name()} ({self.weight()} kg)"

class Suitcase:
    def __init__(self, maxWeight) -> None:
        self.__maxWeight = maxWeight
        self.__items = []
        self.__weight = 0

    def add_item(self, item: Item):
        if item.weight() <= self.__maxWeight - self.__weight:
            self.__items.append(item)
            self.__weight += item.weight()

    def __str__(self):
        return f"{getAmt(self.__items, 'item')} ({self.__weight} kg)"

    def print_items(self):
        for item in self.__items:
            print(item)

    def weight(self):
        return self.__weight

    def heaviest_item(self):
        if self.__items:
            return max(self.__items, key=lambda x: x.weight())

class CargoHold:
    def __init__(self, maxW):
        self.__room = maxW
        self.__cargo = []

    def add_suitcase(self, sc):
        if sc.weight() <= self.__room:
            self.__cargo.append(sc)
            self.__room -= sc.weight()

    def __str__(self):
        return f"{getAmt(self.__cargo, 'suitcase')}, space for {self.__room} kg"

    def print_items(self):
        for sc in self.__cargo:
            sc.print_items()

def getAmt(lst, unit: str):
    if len(lst) != 1:
        unit += "s"
    return f"{len(lst)} {unit}"

if __name__ == "__main__":
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)
    
    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)
    
    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)
    
    cargo_hold = CargoHold(1000)
    cargo_hold.add_suitcase(adas_suitcase)
    cargo_hold.add_suitcase(peters_suitcase)
    
    print("The suitcases in the cargo hold contain the following items:")
    cargo_hold.print_items()
