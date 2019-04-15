class Santa:
    def __init__(self, *args):
        self.coords = {'x':0, 'y':0}

    def moveUp(self):
        self.coords['x'] += 1
    def moveDown(self):
        self.coords['x'] -= 1

    def moveRight(self):
        self.coords['y'] += 1
    def moveLeft(self):
        self.coords['y'] -= 1

    def checkPresents(self, directions):
        global presents

        start = 0
        if self != santa:
            start = 1

        for x in directions[start::2]:
            if x == "^":
                self.moveUp()
            elif x == ">":
                self.moveRight()
            elif x == "V" or x =="v":
                self.moveDown()
            else:
                self.moveLeft()
            current_coords = str(self.coords['x']) + ', ' + str(self.coords['y'])

            if current_coords in presents:
                presents[current_coords] += 1
            else:
                presents[current_coords] = 1

def getInput():
    with open("text.txt") as data:
        for line in data:
            directions = line
    return directions

presents = {'0, 0': 2}

directions = getInput()
santa = Santa()
roboSanta = Santa()

santa.checkPresents(directions)
roboSanta.checkPresents(directions)
print(len(presents))
