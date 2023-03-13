T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    a = a % 10
    two = [6, 2, 4, 8]
    three = [1, 3, 9, 7]
    four = [6, 4]
    seven = [1, 7, 9, 3]
    eight = [6, 8, 4, 2]
    nine = [1, 9]
    if (a == 1):
        print(1)
    elif (a == 2):
        print(two[b % 4])
    elif (a == 3):
        print(three[b % 4])
    elif (a == 4):
        print(four[b % 2])
    elif (a == 5):
        print(5)
    elif (a == 6):
        print(6)
    elif (a == 7):
        print(seven[b % 4])
    elif (a == 8):
        print(eight[b % 4])
    elif (a == 9):
        print(nine[b % 2])
    else:
        print(10)
