presents = {'0, 0': 1}
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
        # if self == santa:
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
                presents[current_coords] += 2
            else:
                presents[str(self.coords['x']) + ', ' + str(self.coords['y'])] = 1
        # elif self == roboSanta:
        #     for x in directions[1::2]:
        #         if x == "^":
        #             self.moveUp()
        #         elif x == ">":
        #             self.moveRight()
        #         elif x == "V" or x =="v":
        #             self.moveDown()
        #         else:
        #             self.moveLeft()
        #         current_coords = str(self.coords['x']) + ', ' + str(self.coords['y'])
        #
        #         if current_coords in presents:
        #             presents[current_coords] += 1
        #         else:
        #             presents[str(self.coords['x']) + ', ' + str(self.coords['y'])] = 1

def getInput():
    with open("text.txt") as data:
        for line in data:
            directions = line
    return directions

directions = getInput()
santa = Santa()
roboSanta = Santa()

santa.checkPresents(directions)
roboSanta.checkPresents(directions)
print(len(presents))


# print(getInput())

# def checkPresents(directions):
#     presents = {'0, 0': 1}
#     for x in directions[0::2]:
#         if x == "^":
#             santa.moveUp()
#         elif x == ">":
#             santa.moveRight()
#         elif x == "V" or x =="v":
#             santa.moveDown()
#         else:
#             santa.moveLeft()
#         current_coords = str(santa.coords['x']) + ', ' + str(santa.coords['y'])
#         if current_coords in presents:
#             presents[current_coords] += 2
#         else:
#             presents[str(santa.coords['x']) + ', ' + str(santa.coords['y'])] = 1
#
#     return presents
#
# def checkPresentsRobo(directions):
#     presents = {'0, 0': 1}
#     for x in directions[1::2]:
#         if x == "^":
#             roboSanta.moveUp()
#         elif x == ">":
#             roboSanta.moveRight()
#         elif x == "V" or x =="v":
#             roboSanta.moveDown()
#         else:
#             roboSanta.moveLeft()
#         current_coords = str(roboSanta.coords['x']) + ', ' + str(roboSanta.coords['y'])
#         if current_coords in presents:
#             presents[current_coords] += 2
#         else:
#             presents[str(roboSanta.coords['x']) + ', ' + str(roboSanta.coords['y'])] = 1
#
#     return presents




# presents = checkPresents(directions)
# roboPresents = checkPresentsRobo(directions)

# print(directions)
# print(santa.coords)
# print(presents)
# print(roboPresents)
