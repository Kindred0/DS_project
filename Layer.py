from tkinter import N
from PIL import Image
import numpy
import RGB_HSV_converter as rv

class Layer :
    def __init__(self, i) :
        self.img = Image.open(i)
        self.matrix = numpy.array(self.img)
        self.shape = self.matrix.shape
        self.HSV_matrix = []
    def __init__(self) :
        self.img = None
        self.matrix = []
        self.shape = (0, 0)
        self.HSV_matrix = []
    def get_HSV(self) :
        temp = []
        for i in self.matrix :
            for k in i :
              temp.append(rv.to_hsv(k))
            self.HSV_matrix.append(temp)  
    def __del__(self) :
        self.img.close()
        print("Destructor called")
    def show(self) :
        self.img.show()
    def show_matrix(self) :
        print(self.matrix)
    
def addition(layer1, layer2) :
    resultant = Layer
    layer1.get_HSV()
    layer2.get_HSV()
    temp = []
    for i in layer1.HSV_matrix :
        for k in i :
            value = 
            temp.append() 

def subtraction(layer1, layer2) :
    pass

def multiply(layer1, layer2) :
    pass

def devide(layer1, layer2) :
    pass

def overlay(layer1, layer2) :
    pass

def darken(layer1, layer2) :
    pass

def lighten(layer1, layer2) :
    pass

def dissolve(layer1, layer2) :
    pass

def normal(layer1, layer2) :
    pass


f = input("Enter the name and location of the image to be loaded\t: ")
img1 = Layer(f)
img1.show()
img1.show_matrix()