li = input("Enter numbers : ")
li = li.replace("[", "")
li = li.replace("]", "")
li = li.replace(" ", "")
while True:
    if " " in li:
        li = li.replace(" ", "")
    else:
        break
li = li.split(",")
newLi = []
try:
    for item in li:
        item = int(item)
        if item > 10:
            while True:
                rev_item = str(item)[::-1]
                if item != int(rev_item):
                    item += 1
                else:
                    newLi.append(item)
                    break
        else:
            newLi.append(item)
    print(newLi)
except Exception as e:
    print(e)
                