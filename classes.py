class Item:
    def __init__(self, name, id_num, stock):
        self.name = name
        self.id_num = id_num
        self.stock = stock

    def __str__(self):
        return "\nItem: " + self.name + "\nID Number: " + str(self.id_num) + "\nStock Count: " + str(self.stock)

