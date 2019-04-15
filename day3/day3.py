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

santa = Santa()

def getInput():
    with open("text.txt") as data:
        for line in data:
            directions = line
    return directions

# print(getInput())

def checkPresents(directions):
    presents = {'0, 0': 1}
    for x in directions:
        if x == "^":
            santa.moveUp()
        elif x == ">":
            santa.moveRight()
        elif x == "V" or x =="v":
            santa.moveDown()
        else:
            santa.moveLeft()
        current_coords = str(santa.coords['x']) + ', ' + str(santa.coords['y'])
        if current_coords in presents:
            presents[current_coords] += 1
        else:
            presents[str(santa.coords['x']) + ', ' + str(santa.coords['y'])] = 1

    return presents



directions = getInput()
presents = checkPresents(directions)

# print(directions)
# print(santa.coords)
# print(presents)
print(len(presents))
