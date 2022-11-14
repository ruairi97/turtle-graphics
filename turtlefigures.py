from turtle import *
import math

def tree(n, l, pen):
     if n==0 or l<2 :
          return
     #endif
     pen.forward(l)
     pen.left(45)
     tree(n-1, l/2, pen)
     pen.right(90)
     tree(n-1, l/2, pen)
     pen.left(45)
     pen.backward(l)

#end 

def dandelion(n, l, pen):
     if n==0 or l<2 :
          return
     #endif
     pen.forward(l)
     pen.left(90)
     dandelion(n-1, l/2, pen)
     pen.right(60)
     dandelion(n-1, l/2, pen)
     pen.right(60)
     dandelion(n-1, l/2, pen)
     pen.right(60)
     dandelion(n-1, l/2, pen)
     pen.left(90)
     pen.backward(l)

#end

def fern(n, l, pen):
     if n==0 or l<2 :
          return
     #endif
     pen.forward(2*l/3)
     pen.left(45)
     fern(n-1, l/2, pen)
     pen.right(45)
     pen.forward(2*l/3)
     pen.right(30)
     fern(n-1, l/2, pen)
     pen.left(30)
     pen.forward(2*l/3)
     pen.right(10)
     fern(n-1, 0.75*l, pen)
     pen.left(10)
     pen.backward(2*l)

#end
     


def koch(n, l, pen):
     if n==0 or l<2 :
          pen.forward(l)
          return
     #endif
     koch(n-1, l/3, pen)
     pen.left(60)
     koch(n-1, l/3, pen)
     pen.right(120)
     koch(n-1, l/3, pen)
     pen.left(60)
     koch(n-1, l/3, pen)
    
#end

def flake(n, l, pen):
     for i in range(3):
          koch(n, l, pen)
          pen.right(120)
     #endfor
#end

def antiflake(n, l, pen):
     for i in range(3):
          koch(n, l, pen)
          pen.left(120)
     #endfor
#end

def pentagon(n, l, pen):
     if n==0 or l<2 :
          return
     #endif
     for i in range(5):
          hexagon(n-1, l*0.381966601126, pen)
          pen.forward(l)
          pen.left(72)


def pentagram(n, l, pen):
     if n==0 or l<2 :
          return
     #endif
     for i in range(5):
          pen.left(36)
          pen.forward(l*1.61803398875)
          pen.left(108)
     pen.left(36)
     pen.forward(l*1.61803398875)
     pen.left(144)
     pen.forward(l*0.61803398875)
     pentagram(n-1, l*0.381966011250105, pen)
     pen.backward(l*0.61803398875)
     pen.right(144)
     pen.backward(l*1.61803398875)
     pen.right(36)
     
def square(n, l, pen):
     if n==0 or l<2:
          return
     #endif
     for i in range(4):
          pen.forward(l)
          pen.left(90)
     square(n-1, l/3, pen)
     pen.forward(l/1.5)
     square(n-1, l/3, pen)
     pen.left(90)
     pen.forward(l/1.5)
     pen.right(90)
     square(n-1, l/3, pen)
     pen.backward(l/1.5)
     square(n-1, l/3, pen)
     pen.left(90)
     pen.backward(l/3)
     pen.right(90)
     pen.forward(l/3)
     square(n-1, l/3, pen)
     pen.backward(l/3)
     pen.left(90)
     pen.backward(l/3)
     pen.right(90)
     
     
     
#notworking
def scurve(n, l, pen):
     if n==0 or l<2:
          return
     #endif
     for i in range (4):
          scurve(n-1, l, pen)
          pen.right(45)
          pen.forward(l)
          pen.right(45)
          scurve(n-1, l, pen)
          pen.forward(l)
          pen.left(90)
          scurve(n-1, l, pen)
          pen.right(45)
          pen.forward(l)
          pen.right(45)
          scurve(n-1, l, pen)

def Scurve(n, l, pen):
     if n==0 or l<2:
          return
     #endif
     Scurve(n-1, l, pen)
     pen.right(45)
     pen.forward(l)
     pen.right(45)
     Scurve(n-1, l, pen)
     pen.left(90)
     pen.forward(l)
     pen.left(90)
     Scurve(n-1, l, pen)
     pen.right(45)
     pen.forward(l)
     pen.right(45)
     Scurve(n-1, l, pen)

def carpet(n, l, pen):
     if n == 0:
          pen.color('orange')
          pen.beginFill()
          for i in range (4):
               pen.forawrd(l)
               pen.left(90)
               pen.end_fill

     else:
          for i in range(4):
               carpet(n-1, l/3, pen)
               pen.forward(l/3)
               carpet(n-1, l/3, pen)
               pen.forward(l/3)
               pen.forward(l/3)
               pen.left(90)


def striangle(n, l, pen):
     if n==0 or l<2:
          return
     #endif
     for i in range (3):
          pen.forward(l)
          pen.left(120)
     striangle(n-1, l/2, pen)
     pen.forward(l/2)
     striangle(n-1, l/2, pen)
     pen.backward(l/2)
     pen.left(60)
     pen.forward(l/2)
     pen.right(60)
     striangle(n-1, l/2, pen)
     pen.left(60)
     pen.backward(l/2)
     pen.right(60)

#notworking
def circle(n, l, pen):
     if n==0 or l<2:
          return
     #endif
     pen.circle(l)
     pen.left(60)
    
     pen.forward(1.73205080757*l)
     pen.right(90)
     
     circle(n-1, l/2, pen)
     
     pen.left(30)
     pen.backward(1.73205080757*l)
     
     pen.left(60)
     circle(n-1, l/2, pen)


def circles(n, l, pen):
     if n==0 or l<2:
          return
     #endif
     pen.circle(l)
     circles(n-1, 0.464*l, pen)
     pen.circle(0.464*l)
     pen.up()
     pen.left(90)
     pen.forward(0.464*l)
     pen.right(30)
     pen.forward(0.928*l)
     pen.right(150)
     pen.forward(0.464*l)
     pen.left(90)
     pen.down()
     circles(n-1, 0.464*l, pen)
     pen.circle(0.464*l)
     pen.up()
     pen.left(90)
     pen.forward(0.464*l)
     pen.left(90)
     pen.forward(0.928*l)
     pen.left(90)
     pen.forward(0.464*l)
     pen.left(90)
     pen.down()
     circles(n-1, 0.464*l, pen)
     pen.circle(0.464*l)
     pen.up()
     pen.left(90)
     pen.forward(0.464*l)
     pen.right(150)
     pen.forward(0.928*l)
     pen.right(30)
     pen.forward(0.464*l)
     pen.left(90)
     pen.down()

     
     
     
     
     
     

























     
          
     
     














     

     

