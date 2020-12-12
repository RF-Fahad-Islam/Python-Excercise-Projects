import random
def multiplicationTable(number):
    table = []
    randomNo = random.randint(3,9)
    for i in range(1,11):
        if i == randomNo:
            increaser = random.randint(1,number - random.randint(number//2, number-2))
            table.append((number*i)+increaser)
        else:
            table.append(number*i)
    return table
def isCorrect(table, number):
    Realtable = [i*number for i in range(1,11)]
    for n in table:
        if n not in Realtable:
           result =  f"The table is detected as a fraud :\n\"{n}\" in {table.index(n)} index should be \"{Realtable[table.index(n)]}\""
    return result

n = int(input("Enter the number : "))
table = multiplicationTable(n)
c = isCorrect(table, n)
print(table)
print(c)