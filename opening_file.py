#simple script from opening a file

f = open("countries.txt", "r")

list1 = []

for line in f:
    line = line.strip()  #line.strip gets rid of extra characters in line, like new line or white space
    print(line)
    list1.append(line)

f.close()

choice = str(input("Choose letter: "))
print("List1: " + str(list1))
print("The numer of elements in the list is: " + str(len(list1)))

for country in list1:
    if country[0] == choice:
        print(country)    
