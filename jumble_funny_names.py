'''
Author : Fahad
Practice Problem 9 Solution
'''
import random
def jumbleName(nameList):
    #* Jumbled the names
    lastnames = []
    firstnames = []
    jumbled = []
    for name in nameList:
        name = name.split(" ")
        for i in range(1,len(name)):
            lastnames.append(name[1])
            firstnames.append(name[0])
    lastnames.reverse()
    for i,l in enumerate(lastnames):
        jumbled.append(f"{firstnames[i]} {lastnames[random.randint(0, len(lastnames)-1)]}")
    for name in jumbled:
        print(name) 
           
if __name__ == "__main__":
    #* Take the input from the user
    n = input("Enter the friends number : ")
    nameList = []
    for i in range(int(n)):
        name = input(f"{i+1}. Enter the friend name : ")
        nameList.append(name)
    jumbleName(nameList)