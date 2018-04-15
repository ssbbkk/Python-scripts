f = open("file_test.txt","w")

while True:
    line = input("> ")
    if line == "q":
        break
    f.write(line + "\n")

f.close()
