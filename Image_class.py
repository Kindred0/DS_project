import numpy as np

class Image :
    def __init__(self, i , row, col) :
        self.row = row
        self.col = col
        file = open(i, 'r')
        self.array = np.fromfile(self.file, dtype = np.uint8, count = row * col)
        self.matrix = []
        temp = []
        for i in range(0, row * col) :
            temp.append(self.array[i])
            if i + 1 % row == 0 :
                self.matrix.append(temp)
                temp = []
        file.close()
    def save() :
        pass
    def show() :
        pass
