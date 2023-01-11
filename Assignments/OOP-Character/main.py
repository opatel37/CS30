# Task 1

class Character:
    def __init__(self, name, phrase1, phrase2):
       self.name = name
       self.phrase1 = phrase1
       self.phrase2 = phrase2
       self.level = 0

    def speak(self, phrase_num):
        if phrase_num == 1:
            print(self.phrase1)
        elif phrase_num == 2:
            print(self.phrase2)
        else:
            print("Invalid Input")

    def set_level(self, new_level):
        self.level = new_level
        print(self.level)



# Task 2
p1 = Character("Bob", "LOL", "HAHA")
p2 = Character("Jim", "YAY", "CYA")



# Task 3
print(p1.phrase1)
p2.level = 2
print(p1.phrase2)