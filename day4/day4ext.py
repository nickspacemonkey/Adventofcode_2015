import hashlib

# string = "abcdef609043"
#
# result = hashlib.md5(string.encode())
#
# print(result.hexdigest())
def main(puzzle_input):
    found = False
    count = 0
    while found == False:
        string = puzzle_input + str(count)
        result = hashlib.md5(string.encode())
        hex_result = result.hexdigest()
        if hex_result.startswith("000000"):
            print(hex_result)
            print(count)
            found = True
        else:
            count += 1

if __name__ == '__main__':
    main("ckczppom")
