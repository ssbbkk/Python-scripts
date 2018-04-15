f = open("code.txt", "w")

while True:
    letter = input("Letter > ")
    
    if letter == "quit":
        print("Quitting...")
        break

    code = input("Code for letter \"" + letter + "\" > ")
    f.write(letter + "-" + code + "\n")

f.close()
