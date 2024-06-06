import random
import rich
import rich.panel
import rich.console
class Person:
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age
        self.beliviblity = 0
        if self.age < 20:
            bev = list(range(1, 100+1)) + [75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75] + [80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80,]
            self.beliviblity = random.choice(bev)
        elif self.age <= 40 or self.age >= 20:
            bev = list(range(1, 100+1)) + [75, 75, 75, 75, 75] + [80, 80, 80]
            self.beliviblity = random.choice(bev)
    def stats(self):
        return [self.name, self.age, self.beliviblity]
    def show_stats(self):
        pre = rich.panel.Panel(f"Age: {self.age}\nBelivibility: {self.beliviblity}", title=f"{self.name}")
        pri = rich.console.Console()
        pri.print(pre)


person = Person("Name", 24)
person.show_stats()