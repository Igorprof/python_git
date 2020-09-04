import hashlib

def num_substrs(s):
    hashes = set()
    for start in range(len(s)):
        for end in range(start + 1, len(s) + 1):
            hashes.add(hashlib.sha1(s[start:end].encode('utf-8')).hexdigest())
    return len(hashes) - 1

s = input('Введите строку: ')

print(num_substrs(s))