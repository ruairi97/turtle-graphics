# import lines
from tkinter import *
import turtlefigures
import turtle
import tkinter.ttk as ttk

 
# make the frame and give its geometry
root = Tk()
root.title("Turtle Application")
root.geometry("900x800+300+300")
root.config(bg= "#ffffe6")


# ------------ MAKE THE INTERFACE ---------------------
# make the pen a turtle shape


# make the first label
label = Label(root, text = "Turtle Generator")
label.grid(row = 0, column = 0, columnspan = 2)

# make the canvas panel
canvasPanel = LabelFrame(root, text = "Canvas Frame")
canvasPanel.grid(row = 2, column = 0, columnspan = 4, rowspan = 4)

canvas = Canvas(canvasPanel, width = 600, height = 600)
canvas.pack()

# get the canvas pen and screen
screen = turtle.TurtleScreen(canvas)
pen = turtle.RawTurtle(screen)
pen.color("#33cc33")
pen.shape("turtle")
pen.speed(0)
pen.width(1)
screen.bgcolor("LightBlue1")

# make the control panel
controlPanel = LabelFrame(root, text = "Control Frame")
controlPanel.grid(row = 1, column = 6, rowspan = 4, columnspan = 3)


       
# make the length widgets
lengthLabel = Label(controlPanel, text = "Length", bg = "#ffffe6")
lengthLabel.grid(row = 0, column = 0)
 
lengthStr = StringVar()
lengthEntry = Entry(controlPanel, textvariable = lengthStr)
lengthEntry.grid(row = 0, column = 1)
 
# make the order widgets
orderLabel = Label(controlPanel, text = " Order", bg = "#ffffe6")
orderLabel.grid(row = 1, column = 0)
 
orderStr = StringVar()
orderEntry = Entry(controlPanel, textvariable = orderStr)
orderEntry.grid(row = 1, column = 1)
 
# make the clear button
def clearF():
       # reset the entries using their textvars
       lengthStr.set("")
       orderStr.set("")
#end
clearButton = Button(controlPanel, text = "Clear", command = clearF)
clearButton.grid(row = 3, column = 0)

# make the draw button
def drawF():
       # get order and length
       length = int(lengthStr.get())
       order = int(orderStr.get())
 

       # get the figure id from OptionMenu
       figure = figureStr.get()
       figureId = figureList.index(figure)
 
       # if check to see what to draw
       if figureId == 0:
              fractalInfoStr.set("Binary Tree: first fractal looked at")
              pen.up(); pen.backward(length);pen.down()
              turtlefigures.tree(order, length, pen)
       elif figureId == 1:
              fractalInfoStr.set("Dandelion: fractal completed in lab")
              pen.up(); pen.backward(length);pen.down()
              turtlefigures.dandelion(order, length, pen)
       elif figureId == 2:
              fractalInfoStr.set("Fern: fractal completed in lab")
              pen.up(); pen.backward(length);pen.down()
              turtlefigures.fern(order, length, pen)
       elif figureId == 3:
              fractalInfoStr.set("Flake: fractal completed in lab")
              pen.up(); pen.backward(length);pen.down()
              turtlefigures.flake(order, length, pen)
       elif figureId == 4:
              fractalInfoStr.set("Antiflake: fractal completed in lab, uses same values as flake in reverse")
              pen.up(); pen.backward(length);pen.down()
              turtlefigures.antiflake(order, length, pen)
       elif figureId == 5:
              fractalInfoStr.set("Pentagon, fractal completed by using length value given in lab")
              pen.up(); pen.backward(length);pen.down()
              turtlefigures.pentagon(order, length, pen)
       elif figureId == 6:
              fractalInfoStr.set("Pentagram, personal contribution")
              pen.up(); pen.backward(length);pen.down()
              turtlefigures.pentagram(order, length, pen)
       elif figureId == 7:
              fractalInfoStr.set("Square, first personal contribution made to help me understand making fractals")
              pen.up(); pen.backward(length);pen.down()
              turtlefigures.square(order, length, pen)
       elif figureId == 8:
              fractalInfoStr.set("Scurve,fractal completed using lecture notes ")
              pen.up(); pen.backward(length);pen.down()
              turtlefigures.Scurve(order, length, pen)
       elif figureId == 9:
              fractalInfoStr.set("scurve, interesting mistake made when working on making a scurve")
              pen.up(); pen.backward(length);pen.down()
              turtlefigures.scurve(order, length, pen)
       elif figureId == 10:
              fractalInfoStr.set("Circles, personal contribution")
              pen.up(); pen.backward(length);pen.down()
              turtlefigures.circles(order, length, pen)
       '''elif figureId == 11:
              fractalInfoStr.set("Carpet, completion of fractal discussed in class")
              pen.up(); pen.backward(length);pen.down()
              turtlefigures.carpet(order, length, pen)
              '''
# make the clear button
def treeF():
       # get the values of order and length as int
       length = int(lengthStr.get())
       order = int(orderStr.get())
 
       # move pen to a better position
       pen.up(); pen.backward(length);pen.down()
 
       # pen draws binary tree
       turtlefigures.tree(order, length, pen)
 



#end       
drawButton = Button(controlPanel, text = "Draw", command = drawF)
drawButton.grid(row = 2, column = 0)

# make drop down box
figureList = ["Binary Tree", "Dandelion", "Fern", "Flake", "Antiflake", "Pentagon", "Pentagram", "Square", "Scurve", "scurve", "Circles"]
figureStr = StringVar()
figureOptionMenu = OptionMenu(controlPanel, figureStr, *figureList)
figureOptionMenu.grid(row = 3, column = 1)
figureStr.set("Binary Tree")

# make the reset button
def resetF():
       pen.reset()
       pen.speed(0)
       pen.color("#33cc33")

resetButton = Button(controlPanel, text = "Reset", command = resetF)
resetButton.grid(row = 4, column = 0)


'''

# make the canvas selector drop down box
bgList = ["Pond", "Street", "Field", "Mud"]
bgColorList = ["LightBlue1", "red", "forest green", "saddle brown"]
bgStr = StringVar()
def bgBackgroundSelector(bgStr):
       print(bgStr.get())
       screen.bgcolor(bgColorList[bgList.index(bgStr.get())])

bgOptionMenu = ttk.OptionMenu(controlPanel, bgStr, bgList[0], *bgList, command = bgBackgroundSelector)
bgOptionMenu.grid(row = 4, column = 1)
bgStr.set("Pond")
bg = bgStr.get()

'''


# make the fractal info panel
fractalInfoPanel = LabelFrame(root, text = "Fractal Info", width = 300, height = 100)
fractalInfoPanel.grid(row = 4, column = 6)

fractalInfoStr = StringVar()


fractalInfoLabel = Label(fractalInfoPanel, text = "", textvariable = fractalInfoStr)
fractalInfoLabel.grid(row = 0, column = 0)

# make turle location

locationPanel = LabelFrame(root, text = "Turtle Location")
locationPanel.grid(row = 6, column = 1, rowspan = 1, columnspan = 1)

def pondF():
       screen.bgcolor("LightBlue1")
       
pondButton = Button(locationPanel, text = "Pond", bg = "LightBlue1", command = pondF)
pondButton.grid(row = 0, column = 0)

def streetF():
       screen.bgcolor("azure4")
       
streetButton = Button(locationPanel, text = "Street", bg = "azure4", command = streetF)
streetButton.grid(row = 0, column = 1)

def fieldF():
       screen.bgcolor("forest green")
       
fieldButton = Button(locationPanel, text = "Field", bg = "forest green", command = fieldF)
fieldButton.grid(row = 1, column = 0)

def mudF():
       screen.bgcolor("PeachPuff4")
       
mudButton = Button(locationPanel, text = "Mud", bg = "PeachPuff4", command = mudF)
mudButton.grid(row = 1, column = 1)

# make ninja turtle selector

turtlePanel = LabelFrame(root, text = "Ninja Turtle Selector")
turtlePanel.grid(row = 7, column = 1, rowspan = 1, columnspan = 1)


def leonardoF():
       pen.color("dodger blue")
       
leonardoButton = Button(turtlePanel, text = "Leonardo", bg = "dodger blue", command = leonardoF)
leonardoButton.grid(row = 0, column = 0)

def raphaelF():
       pen.color("red")
       
raphaelButton = Button(turtlePanel, text = "Raphael", bg = "red", command = raphaelF)
raphaelButton.grid(row = 0, column = 1)

def michelangeloF():
       pen.color("orange")
       
michelangeloButton = Button(turtlePanel, text = "Michelangelo", bg = "orange", command = michelangeloF)
michelangeloButton.grid(row = 1, column = 0)

def donatelloF():
       pen.color("purple1")
       
donatelloButton = Button(turtlePanel, text = "Donatello", bg = "purple1", command = donatelloF)
donatelloButton.grid(row = 1, column = 1)


'''

# make the tree button
def treeF():
       # get the values of order and length as int
       length = int(lengthStr.get())
       order = int(orderStr.get())
 
       # move pen to a better position
       pen.up(); pen.backward(length);pen.down()
 
       # pen draws binary tree
       turtlefigures.tree(order, length, pen)
 
#end
treeButton = Button(root, text = "Tree", command = treeF)
treeButton.grid(row = 1, column = 2)



# make the fern button
def fernF():
       # get the values of order and length as int
       length = int(lengthStr.get())
       order = int(orderStr.get())
 
       # move pen to a better position
       pen.up(); pen.backward(length);pen.down()
 
       # pen draws binary fern
       turtlefigures.fern(order, length, pen)
 
#end
fernButton = Button(root, text = "Fern", command = fernF)
fernButton.grid(row = 2, column = 2)


# make the dandelion button
def dandelionF():
       # get the values of order and length as int
       length = int(lengthStr.get())
       order = int(orderStr.get())
 
       # move pen to a better position
       pen.up(); pen.backward(length);pen.down()
 
       # pen draws binary dandelion
       turtlefigures.dandelion(order, length, pen)
 
#end
dandelionButton = Button(root, text = "Dandelion", command = dandelionF)
dandelionButton.grid(row = 3, column = 2)

# make the flake button
def flakeF():
       # get the values of order and length as int
       length = int(lengthStr.get())
       order = int(orderStr.get())
 
       # move pen to a better position
       pen.up(); pen.backward(length);pen.down()
 
       # pen draws binary flake
       turtlefigures.flake(order, length, pen)
 
#end
flakeButton = Button(root, text = "Flake", command = flakeF)
flakeButton.grid(row = 4, column = 2)

# make the antiflake button
def antiflakeF():
       # get the values of order and length as int
       length = int(lengthStr.get())
       order = int(orderStr.get())
 
       # move pen to a better position
       pen.up(); pen.backward(length);pen.down()
 
       # pen draws binary antiflake
       turtlefigures.antiflake(order, length, pen)
 
#end
antiflakeButton = Button(root, text = "Antiflake", command = antiflakeF)
antiflakeButton.grid(row = 4, column = 2)

# make the hexagon button
def hexagonF():
       # get the values of order and length as int
       length = int(lengthStr.get())
       order = int(orderStr.get())
 
       # move pen to a better position
       pen.up(); pen.backward(length);pen.down()
 
       # pen draws binary hexagon
       turtlefigures.hexagon(order, length, pen)
 
#end
       
hexagonButton = Button(root, text = "Hexagon", command = hexagonF)
hexagonButton.grid(row = 5, column = 2)

# make the pentagram button
def pentagramF():
       # get the values of order and length as int
       length = int(lengthStr.get())
       order = int(orderStr.get())
 
       # move pen to a better position
       pen.up(); pen.backward(length);pen.down()
 
       # pen draws binary pentagram
       turtlefigures.pentagram(order, length, pen)
 
#end
pentagramButton = Button(root, text = "Pentagram", command = pentagramF)
pentagramButton.grid(row = 6, column = 2)


# make the square button
def squareF():
       # get the values of order and length as int
       length = int(lengthStr.get())
       order = int(orderStr.get())
 
       # move pen to a better position
       pen.up(); pen.backward(length);pen.down()
 
       # pen draws binary square
       turtlefigures.square(order, length, pen)
 
#end
squareButton = Button(root, text = "Square", command = squareF)
squareButton.grid(row = 7, column = 2)

# make the Scurve button
def ScurveF():
       # get the values of order and length as int
       length = int(lengthStr.get())
       order = int(orderStr.get())
 
       # move pen to a better position
       pen.up(); pen.backward(length);pen.down()
 
       # pen draws binary Scurve
       turtlefigures.Scurve(order, length, pen)
 
#end
ScurveButton = Button(root, text = "Scurve", command = ScurveF)
ScurveButton.grid(row = 8, column = 2)




# make the scurve button
def scurveF():
       # get the values of order and length as int
       length = int(lengthStr.get())
       order = int(orderStr.get())
 
       # move pen to a better position
       pen.up(); pen.backward(length);pen.down()
 
       # pen draws binary scurve
       turtlefigures.scurve(order, length, pen)
 
#end
scurveButton = Button(root, text = "scurve", command = scurveF)
scurveButton.grid(row = 9, column = 2)


# make the circle button
def circleF():
       # get the values of order and length as int
       length = int(lengthStr.get())
       order = int(orderStr.get())
 
       # move pen to a better position
       pen.up(); pen.backward(length);pen.down()
 
       # pen draws binary scurve
       turtlefigures.circle(order, length, pen)
 
#end
circleButton = Button(root, text = "Circle", command = circleF)
circleButton.grid(row = 10, column = 2)

'''





























