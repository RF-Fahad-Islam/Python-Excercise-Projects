try:
    cases = input("Enter the number input : ")
    cases = int(cases)
    li = []
    for i in range(cases):
        user = input("Enter a number to find the next parendrime : ")
        li.append(user)
    for user in li:
        num = int(user)
        while True:
            rev_num = str(num)[::-1]
            if num != int(rev_num):
                num += 1
            else:
                print(f"The {num} is a nearest parendrime number of {user}")
                break
            
except ValueError:
    print("Please Enter a number.")