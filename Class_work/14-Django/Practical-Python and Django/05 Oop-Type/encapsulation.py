# Encapsulation is wrap data (variables) and methods (functions) inside a class some detail protect

class Bank:
    def __init__(self, id, name, saving, percentage, total):
        self.id = id
        self.name = name
        self.saving = saving
        self.__percentage = percentage   # private variable
        self.total = total

    def get_percentage(self):
        return self.__percentage

    def show(self):
        print(f"{self.id} Name is {self.name}, Type of account: {self.saving}, Interest: {self.__percentage}%, Total: {self.total}")

b = Bank(1, "jenil", "saving account", 7.5, 12500)

b.show()
print(b.get_percentage())