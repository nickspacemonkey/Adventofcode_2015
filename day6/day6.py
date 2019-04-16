#!/usr/bin/env python3

class Grid():
    def __init__(self):
        self.lightgrid = {}
        for x in range(0, 1000):
            for y in range(0, 1000):
                self.lightgrid[x, y] = 0

    def turnOn(self, xBot, yBot, xTop, yTop):
        for x in range(xBot, xTop):
            for y in range(yBot, yTop):
                self.lightgrid[x, y] = 1

    def turnOff(self, xBot, yBot, xTop, yTop):
        for x in range(xBot, xTop):
            for y in range(yBot, yTop):
                self.lightgrid[x, y] = 0


    def toggle(self, xBot, yBot, xTop, yTop):
        for x in range(xBot, xTop):
            for y in range(yBot, yTop):
                if self.lightgrid[x, y] == 0:
                    self.lightgrid[x, y] = 1
                else:
                    self.lightgrid[x, y] = 0

#Function to get input from text document
def getInput():
    coordsList = []
    instructions = []
    data = open("text.txt")
        #Formats the text data into a python list
    for line in data:
        line = line.replace("\n", "")
        line = line.replace(",", " ")
        line = line.replace("turn ", "")
        line = line.replace("through ", "")
        coordsList.append(line)

# Formats the data into a list within a list. First item holds string values of on, off or toggle. Remaining 4 are integers for lower and upper coords xBot, yBot, xTop, yTop.
    for line in coordsList:
        instruction = line.split(" ")
        for n in range(1, 5):
            instruction[n] = int(instruction[n])
        instructions.append(instruction)
    return instructions

#Funtion that looks at each list and actions accordingly
def turnLights(coords):
    for x in coords:
        if x[0] == 'toggle':
            lights.toggle(x[1], x[2], x[3]+1, x[4]+1)
        elif x[0] == 'on':
            lights.turnOn(x[1], x[2], x[3]+1, x[4]+1)
        elif x[0] == 'off':
            lights.turnOff(x[1], x[2], x[3]+1, x[4]+1)

def count():
    # Count to check how many lights are on in the dictionary.
    count = 0
    for coord, state in lights.lightgrid.items():
        if state == 1:
            count +=1
    return count

def main():
    turn = turnLights(coords)
    print(count())

lights = Grid()
coords = getInput()

if __name__ == "__main__":
    main()
