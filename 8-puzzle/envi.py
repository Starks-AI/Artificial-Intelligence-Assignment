
arr = ["1","2","3","4","_","5","6","7","8"]
goal_arr = []

def display():
    global arr
    i=0
    while i<9:
        print("{}   {}   {}\n".format(arr[i],arr[i+1],arr[i+2]))
        i+=3
    
def move():
    global arr
    print("Where would you like to move\n For 'Up' press 'W'\n For 'Down' press 'S'\n For 'Left' press 'A'\n For 'Right' press 'D'\n")
    move = input().upper()

    
    if move == 'W':
        #print("UP\n")
        curr = arr.index('_')
        if curr-3>=0:
            arr[curr] = arr[curr-3]
            arr[curr-3] = "_"
        else:
            print("\n invalid input".upper())

    if move == 'S':
        #print("Down\n")
        curr = arr.index('_')
        if curr+3<=8:
            arr[curr] = arr[curr+3]
            arr[curr+3] = "_"
        else:
            print("\n invalid input".upper())

    if move == 'A':
        #print("Left\n")
        curr = arr.index('_')
        if curr-1>=0:
            arr[curr] = arr[curr-1]
            arr[curr-1] = "_"
        else:
            print("\n invalid input".upper())

    if move == 'D':
        #print("Right\n")
        curr = arr.index('_')
        if curr+1<9:
            arr[curr] = arr[curr+1]
            arr[curr+1] = "_"
        else:
            print("\n invalid input".upper())

print("Enter you target array")
for i in range(0,3):
    temp = [i for i in input().split()]
    

print(goal_arr)

#while True:
#    display()
#    move()
