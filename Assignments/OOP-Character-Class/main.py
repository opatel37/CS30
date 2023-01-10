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
p1 = Character("Jim", "YAY", "CYA")