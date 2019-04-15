#Function to get input from text document
def getInput():
    santaList = []
    with open("text.txt") as data:
        #Formats the text data into a python list
        for line in data:
            line = line.replace("\n", "")
            santaList.append(line)
    return santaList

#Funtion to test againt rule 1
def rule1(lines):
    niceLines = []
    for line in lines:
        vowelCount = 0
        for x in line:
            if x=='a' or x=='e' or x=='i' or x=='o' or x=='u':
                vowelCount +=1
        if vowelCount > 2:
            niceLines.append(line)
        else:
            naughtyLines.append(line)
    return niceLines

def rule2(lines):
    niceLines = []
    for line in lines:
        rule2 = False
        count = 1
        for x in line:
            if count < len(line):
                if x == line[count]:
                    rule2 = True
                else:
                    count += 1
        if rule2 == True:
            niceLines.append(line)
        else:
            naughtyLines.append(line)
    return niceLines

def rule3(lines):
    niceLines = []
    for line in lines:
        if 'ab' in line or 'cd' in line or 'pq' in line or 'xy' in line:
            naughtyLines.append(line)
        else:
            niceLines.append(line)
    return niceLines


#testStrings = ['ugknbfddgicrmopn', 'jchzalrnumimnmhp', 'haegwjzuvuyypxyu', 'dvszwmarrgswjxmb']

naughtyLines = []

fullList = getInput()
rule1 = rule1(fullList)
rule2 = rule2(rule1)
rule3 = rule3(rule2)

print('Total nice strings:', len(rule3))
print('Total naughty strings:', len(naughtyLines))
print('Total lines in list:', len(rule3) + len(naughtyLines))
