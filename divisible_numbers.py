n = input("Enter the number of apples : ")
mn = input("Enter the minimum number : ")
mx = input("Enter the maximum number : ")
try:
    n = int(n)
    mn = int(mn)
    mx = int(mx)
    if mn > mx:
        print("Minimum number cannot be larger than maximum number.")
    if mn == mx:
        print(f"The minimum and maximum number is not in range.")
    else:
        for i in range(mn, (mx+1)):
            if n%i == 0:
                print(f"{i} is a divisor of {n}")
            else:
                print(f"{i} is not a divisor of {n}")
except ValueError:
    print("Please type integers only, not a string.")