from statistics import median

def getInput():
    dimensions = []
    with open("day2text.txt") as data:
        for line in data:
            line = line.replace("\n", '')
            dimensions.append(line.split("x"))
    return dimensions

# def getInput():
#     dimensions = [['2', '3', '4'], ['1', '1', '10']]
#     return dimensions

def stringToInt(stringlist):
    intlist = []
    x = 0
    for i in stringlist:
        singlelist = stringlist[x]
        singlelist = list(map(int, singlelist))
        intlist.append(singlelist)
        x+=1
    return(intlist)

# def getSize(dimensions):
#     paper_sizes = []
#     for box in dimensions:
#         area1 = (box[0] * box[1]) * 2
#         area2 = (box[1] * box[2]) * 2
#         area3 = (box[2] * box[0]) * 2
#
#         areas = []
#         areas.extend(((area1 // 2), (area2 // 2), (area3 // 2)))
#
#         slack = min(areas)
#         paper_sizes.append(area1 + area2 + area3 + slack)
#     return paper_sizes

def getRibbon(dimensions):
    ribbon_lengths = []
    for box in dimensions:
        middle = median(box)
        minimum = min(box)

        ribbon = middle + middle + minimum + minimum
        bow = box[0] * box[1] * box[2]

        ribbon_lengths.append(ribbon + bow)

    return ribbon_lengths

datalist = getInput()
intlist = stringToInt(getInput())
totalorder = sum(getRibbon(intlist))

print(totalorder)
