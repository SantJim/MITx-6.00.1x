num = 50
iterate = 50

ran = int(input("Enter a number"))

char = "2"

while True:
    print("Is your number" + str(num) )
    char = input("enter h l or c")
    if char == "l":
        89iterate =  int(iterate/2)
        num = int(num + (iterate))
    elif char == "h":
        iterate = int(iterate/2)
        num = int( num - (iterate) )
    elif char == "c":
        break
    
