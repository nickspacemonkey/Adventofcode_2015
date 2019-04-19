import hashlib

def main(puzzle_input):
    count = 0
    while True:
        string = puzzle_input + str(count)
        result = hashlib.md5(string.encode())
        hex_result = result.hexdigest()
        if hex_result.startswith("000000"):
            print(hex_result)
            print(count)
            break
        count += 1

if __name__ == '__main__':
    main("ckczppom")
