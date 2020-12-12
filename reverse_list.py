li = input("Enter the items to get a reversed list : ")
try:
    li = list(li)
    #TODO: 1st method - li.reverse()
    li.reverse()
    print(li)
    li.reverse() #back to normal
    #TODO: 2nd method - li[::-1]
    print(li[::-1])
    #TODO: 3nd method - custom
    n = len(li) - 1
    for i,item in enumerate(li):
        init = li.pop(n-i)
        li.append(init)
    print(li)
    #All methods applied
except Exception as e:
    print(e)