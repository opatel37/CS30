# Task 1
class Backpack:
    def __init__(self, color, size):
        self.color = color
        self.size = size
        self.items = []
        self.zipper = False

    def open_bag(self):
        self.zipper = True
        print("Backpack is now open!")

    def close_bag(self):
        self.zipper = False
        print("Backpack is now close!")

    def put_in(self, item):
        self.items.append(item)

    def take_out(self, item):
        self.items.remove(item)



# Task 2
bag1 = Backpack("blue", "small")
bag2 = Backpack("red", "medium")
bag3 = Backpack("green", "large")



# Task 3
bag1.open_bag()
bag1.put_in("Lunch")
bag1.put_in("Jacket")
bag1.close_bag()
bag1.open_bag()
bag1.take_out("Jacket")
bag1.close_bag()