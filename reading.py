f = open("code.txt", "r")

codes = {}

for line in f:
    entry = line.strip().split("-")
    codes[entry[0]] = entry[1]

f.close()

print(codes)
print(codes.keys())
print(codes.values())
