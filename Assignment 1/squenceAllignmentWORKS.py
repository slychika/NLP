'''
Natural Language Processing
Assignment 1
Sequence Alignment
'''

def main():
    #string1, string2 = None
    string1 = input("Please enter string 1: ")
    string2 = input("Please enter string 2: ")

    matrixlcs, directionlcs = matrixLCS(string1, string2)
    print("The matrix of your string matches is:", matrixlcs)
    print("The matrix of your directions are:", directionlcs)
    
    strings = stringsLCS(matrixlcs, string1, string2)
    
    print("Your string matches are", strings)
       
    
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
                    
    return lengths,direction

def stringsLCS(lengths, a, b):
    # read the substring out from the matrix
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
