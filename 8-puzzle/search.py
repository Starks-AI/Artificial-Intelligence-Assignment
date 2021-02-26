from graph import Graph

arr = ["1","2","3","4","_","5","6","7","8"]
goal_arr = []




#########################Define the functions
def display(myarr):
    if '_' in myarr:
        i=0
        while i<9:
            print("{}   {}   {}\n".format(myarr[i],myarr[i+1],myarr[i+2]))
            i+=3
    else:
        print('Invalid movement'.upper())
    

def moveup(myarr):
    if '_' in myarr:
        curr = myarr.index('_')
        if curr-3>=0:
            myarr[curr] = myarr[curr-3]
            myarr[curr-3] = "_"
        else:

            return [0]
        return myarr
    else:
        return [0]
    
def movedown(myarr):
    if '_' in myarr:
        curr = myarr.index('_')
        if curr+3<=8:
            myarr[curr] = myarr[curr+3]
            myarr[curr+3] = "_"
        else:

            return [0]
        return myarr
    else:
        return [0]

def moveleft(myarr):
    if '_' in myarr:
        curr = myarr.index('_')
        if curr-1>=0:
            myarr[curr] = myarr[curr-1]
            myarr[curr-1] = "_"
        else:

            return [0]
        return myarr
    else: 
        return [0]

def moveright(myarr):
    if '_' in myarr:

        curr = myarr.index('_')
        if curr+1<9:
            myarr[curr] = myarr[curr+1]
            myarr[curr+1] = "_"
        else:
            
            return [0]
        return myarr
    else:
        return [0]







###################Input the goal array
while len(goal_arr)<9:
    print("Enter your target array")
    for i in range(0,3):
        temp = input().split()
        if len(temp)==3:
            for item in temp:
                goal_arr.append(item)
        else:
            print("invalid format")
            goal_arr=[]
            break

print ("Your start array is\n ")
display(arr)
print("\n Your target array is \n")
display(goal_arr)




#################Construct the tree
g = Graph(70)

first = arr

g.addedge(tuple(first),tuple(moveup(first.copy())))
g.addedge(tuple(first),tuple(movedown(first.copy())))
g.addedge(tuple(first),tuple(moveleft(first.copy())))
g.addedge(tuple(first),tuple(moveright(first.copy())))




value_arr = []
index = 0

for i in range(0,2):
    for a,b,c,d in g.graph.values(): 
        value_arr.append(a)
        value_arr.append(b)
        value_arr.append(c)
        value_arr.append(d)


    for item in value_arr[index:]:
        if item in g.graph.keys():
            pass
        else:
            g.addedge(item,tuple(moveup(list(item).copy())))
            g.addedge(item,tuple(movedown(list(item).copy())))
            g.addedge(item,tuple(moveleft(list(item).copy())))
            g.addedge(item,tuple(moveright(list(item).copy())))

    index = len(value_arr)



for a,b,c,d in g.graph.values(): 
        value_arr.append(a)
        value_arr.append(b)
        value_arr.append(c)
        value_arr.append(d)


#######################Start the search



if g.IDDFS(first,tuple(goal_arr),4) == True:
    print("\nIs possible".upper())
else:
    print("\nNot possible".upper())



