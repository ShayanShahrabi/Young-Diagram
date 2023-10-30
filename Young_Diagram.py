class matrixMakerRowMaj:
    #-------------------------------------------------------------------------
    def __init__(self, array:list, row:int, col:int):
        self.array = array  # 1D array
        self.row = row
        self.col = col
        self.size = row * col
    #-------------------------------------------------------------------------
    # value return
    # the 2D matrix rows and columns are 0-based
    def getAt(self, row, col) -> int:  # take row and col, return element in that row and col
        return self.array[row * self.col + col]
    #-------------------------------------------------------------------------
    def setAt(self, row, col, value) -> None:  # take row, col and value then set new element
        self.array[row * self.col + col] = value
    #-------------------------------------------------------------------------
    # index return
    def index_to_row_col(self, index):  # take 0-based index in 1-D array, return row and col in 2-D matrix
        return ( (index // self.col) , index % self.col)
    #-------------------------------------------------------------------------
    def row_col_to_index(self, row, col):  # takes row col in 2-D matrix, return index in 1-D array
        if row * self.col + col > self.size:
            return None
        return (row * self.col + col)
    #-------------------------------------------------------------------------
    # the Young Table elements are sorted in decreasing order
    # Young Table methods
    def siftDown(self, row, col) -> None:

        currentNum = self.getAt(row, col)

        if row < self.row - 1:  # if not among the last row
            downNeighbor = self.getAt(row+1, col)
            existDown = True
        else:  # row = self.row - 1
            existDown = False
            

        if col < self.col - 1:  # if not among the last column
            rightNeighbor = self.getAt(row, col+1)
            existRight = True
        else:  # col = self.col - 1
            existRight = False
            

        if (existDown and existRight):
            maxNeighbor = max (downNeighbor, rightNeighbor)
        elif(existRight):
            maxNeighbor = rightNeighbor
        elif(existDown):
            maxNeighbor = downNeighbor
        else:  # if at the bottom right corner
            return
    

        if currentNum < maxNeighbor:
            if existRight and existDown and maxNeighbor == rightNeighbor:  # has both neghbors, right is greater
                self.setAt(row, col, maxNeighbor)
                self.setAt(row, col+1, currentNum)
                self.siftDown(row, col+1)
            elif  existRight and existDown and maxNeighbor == downNeighbor:  # has both neghbors, down is greater
                self.setAt(row, col, maxNeighbor)
                self.setAt(row+1, col, currentNum)
                self.siftDown(row+1, col)
            elif existRight:  # has only right neghbor
                self.setAt(row, col, maxNeighbor)
                self.setAt(row, col+1, currentNum)
                self.siftDown(row, col+1)
            elif existDown:  # has only down neghbor
                self.setAt(row, col, maxNeighbor)
                self.setAt(row+1, col, currentNum)
                self.siftDown(row+1, col)
        else:  # if the element is in correct place
            return        
    #-------------------------------------------------------------------------
    def buildYoungTable(self) -> None:  
        for i in range(self.row - 1, -1, -1):  # row
            for j in range(self.col - 1, -1, -1):  # col
                self.siftDown(i, j)
    #-------------------------------------------------------------------------
    def printTable(self) -> None:
        print('\nCurrent Table:\n')
        for i in range(len(self.array)):
            if i % self.col == 0 and i != 0:
                print('')
            print(self.array[i], end=' ')
        print('')
    #-------------------------------------------------------------------------
    def minElement(self) -> int:
        return self.array[-1]
    #-------------------------------------------------------------------------
