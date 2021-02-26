from collections import defaultdict

def display(myarr):
    if '_' in myarr:
        i=0
        while i<9:
            print("{}   {}   {}\n".format(myarr[i],myarr[i+1],myarr[i+2]))
            i+=3
    else:
        print('Invalid movement'.upper())

class Graph:

    def __init__(self,vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addedge(self,u,v):

        self.graph[tuple(u)].append(v)

    def IDS(self,src,target,maxdepth):

        if src == target:
            print("   /\\  ")
            print("  /  \\ ")
            print(" / || \\")
            print("   ||   ")
            print("   ||   ")
            print("   ||   ")
            print("   ||   ")
            print("   ||   ")
            display(src)
            return True

        if maxdepth <= 0:
            return False

        for i in self.graph[tuple(src)]:
            if (self.IDS(i,target,maxdepth-1)):
                print("   /\\  ")
                print("  /  \\ ")
                print(" / || \\")
                print("   ||   ")
                print("   ||   ")
                print("   ||   ")
                print("   ||   ")
                print("   ||   ")
                display(src)
                return True
        return False

    def IDDFS(self,src,target,maxdepth):

        for i in range(maxdepth):
            if (self.IDS(src,target,i)):
                return True
        
        return False