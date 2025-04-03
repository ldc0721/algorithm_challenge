#youngsik's finger
finger = int(input())
count = int(input())


def youngsik(x,y):
    if x == 1 :
        return 8*y
    elif x == 2 :
        if y%2 == 0 :
            return 1 + 8*(y//2)
        else :
            return -1 + 8*((y+1)//2)
    elif x == 3 :
        return 2 + 4*y
    elif x == 4 :
        if y%2 == 0 :
            return 3 + 8*(y//2)
        else :
            return -3 + 8*(y+1)//2
    elif x == 5 :
        return 4 + 8*y

print(int(youngsik(finger, count)))

