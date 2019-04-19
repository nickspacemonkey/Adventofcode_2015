import hashlib

str = "abcdef609043"

result = hashlib.md5(str.encode())

print(result.hexdigest())
