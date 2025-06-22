def odd_even(a):
    if a % 2 == 0:
        return "value is even"
    else:
        return "value is odd"


for i in range(1, 11):
    result = odd_even(i)
    # print(f"{i}: {result}")
    print(result)




