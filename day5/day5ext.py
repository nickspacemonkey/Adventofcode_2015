#Function to get input from text document
def getInput():
    santaList = []
    data = open("text.txt")
        #Formats the text data into a python list
    for line in data:
        line = line.replace("\n", "")
        santaList.append(line)
    return santaList



def rule1(lines):
    niceLines = []
    for line in lines:
        rule1 = False
        pairs = []
        count = 1
        previous_pair = ""
        for x in line:
            if count < len(line):
                quad = x * 4
                pair = x + line[count]
                if quad in line:
                    rule1 = True
                elif pair == previous_pair:
                    count += 1
                elif pair in pairs:
                    rule1 = True
                else:
                    previous_pair = pair
                    pairs.append(pair)
                    count += 1
        if rule1 == True:
            niceLines.append(line)
        else:
            naughtyLines.append(line)
    return niceLines

def rule2(lines):
    niceLines = []
    for line in lines:
        rule2 = False
        count = 2
        for x in line:
            if count < len(line):
                if x == line[count]:
                    rule2 = True
                else:
                    count +=1
        if rule2 == True:
            niceLines.append(line)
        else:
            naughtyLines.append(line)
    return niceLines


naughtyLines = []

fullList = getInput()
rule2 = rule2(fullList)
rule1 = rule1(rule2)

print('Total nice strings:', len(rule1))
print('Total naughty strings:', len(naughtyLines))
print('Total lines in list:', len(rule1) + len(naughtyLines))
