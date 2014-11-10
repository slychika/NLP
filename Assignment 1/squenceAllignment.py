'''
Natural Language Processing
Assignment 1
Sequence Alignment
Heather Dykstra
(With help from Luke Ladtkow and Wikipedia)
An edited version w/a recursive backtrace
'''

def main():
    string1 = input("Please enter string 1: ")
    string2 = input("Please enter string 2: ")

    matrixlcs, directionlcs = matrixLCS(string1, string2)
    print("The matrix of your string matches is:", matrixlcs)
    print("The matrix of your directions are:", directionlcs)
    
    strings = stringsLCS(matrixlcs, string1, string2)

    length1 = len(string1)
    length2 = len(string2)
    #print(length1, ",", length2)
    new1 = ""
    new2 = ""
    
    allCombo(directionlcs, length1, length2, string1, string2, new1, new2)
    
    #print("A string match is", strings)
       
    
def matrixLCS(a, b):
    lengths = [[0 for j in range(len(b)+1)] for i in range(len(a)+1)]
    direction = [[0 for j in range(len(b)+1)] for i in range(len(a)+1)]
    #Form the LCS 2270 Matrix
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if x == y:
                lengths[i+1][j+1] = lengths[i][j] + 1
            else:
                if lengths[i+1][j] > lengths[i][j+1]:
                    lengths[i+1][j+1] = lengths[i+1][j]
                else:
                    lengths[i+1][j+1] = lengths[i][j+1]
    #Do some backtrace for left and up
    for i in range(len(a)+1):
        for j in range(len(b)+1):
            if i != 0:
                if j != 0:
                    if lengths[i-1][j] == lengths[i][j]:
                        direction[i][j] += 4
                    if lengths[i][j-1] == lengths[i][j]:
                        direction[i][j] += 2
    #Finish backtrace for diagonals!
    # Note! I could optimize this slightly
    # and put this in the formation of the 2270 matrix...                    
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if x == y:
                direction[i+1][j+1] += 1
    #adjust backtrace matrix
    #puts in 2 and 4 for directions instead of 0
    for i in range(len(a)+1):
        if(i!=0):
            direction[i][0] = 4
    for j in range(len(b)+1):
        if(j!=0):
            direction[0][j] = 2
                    
    return lengths,direction

#this is my backtrace function!
#WOOHOO
def allCombo(direction, x, y, a, b, newa, newb, value=-1):
    directionValue = direction[x][y]
    if(value != -1):
        directionValue = value
    if directionValue == 0:
        print("Top:    ", newa)
        print("Bottom: ", newb)
    if directionValue == 1:
        newa = a[x-1] + newa
        newb = b[y-1] + newb
        allCombo(direction,x-1,y-1,a,b,newa,newb)
    if directionValue == 2:
        newa = "-" + newa
        newb = b[y-1] + newb
        allCombo(direction,x,y-1,a,b,newa,newb)
    if directionValue == 3:
        allCombo(direction,x,y,a,b,newa,newb,1)
        allCombo(direction,x,y,a,b,newa,newb,2)
    if directionValue == 4:
        newa = a[x-1] + newa
        newb = "-" + newb
        allCombo(direction,x-1,y,a,b,newa,newb)
    if directionValue == 5:
        allCombo(direction,x,y,a,b,newa,newb,1)
        allCombo(direction,x,y,a,b,newa,newb,4)
    if directionValue == 6:
        allCombo(direction,x,y,a,b,newa,newb,2)
        allCombo(direction,x,y,a,b,newa,newb,4)
    if directionValue == 7:
        allCombo(direction,x,y,a,b,newa,newb,1)
        allCombo(direction,x,y,a,b,newa,newb,2)
        allCombo(direction,x,y,a,b,newa,newb,4)

#adapted java code from a wiki,
#this does not backtrace what I wanted.
#but it does give one string with a set of chars
#that are in both in that order
def stringsLCS(lengths, a, b):
    # read the substring out from the lengths matrix
    result = ""
    x, y = len(a), len(b)
    while x != 0 and y != 0:
        if lengths[x][y] == lengths[x-1][y]:
            x -= 1
        elif lengths[x][y] == lengths[x][y-1]:
            y -= 1
        else:
            assert a[x-1] == b[y-1]
            result = a[x-1] + result
            x -= 1
            y -= 1
    return result

    
if __name__ == "__main__":
    main()
