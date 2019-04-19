import hashlib

# string = "abcdef609043"
#
# result = hashlib.md5(string.encode())
#
# print(result.hexdigest())

puzzle_input = "ckczppom"
found = False
count = 0
while found == False:
    string = puzzle_input + str(count)
    result = hashlib.md5(string.encode())
    hex_result = result.hexdigest()
    five = 0
    for i in range(5):
        if hex_result[i] == "0":
            five += 1
    if five == 5:
        print(hex_result)
        print(count)
        found = True
    else:
        count += 1
