Assignment: Turtle Fractal Interface

To Run: Open 'turlegenerator.py' and run module.

The following contains information about my personal contributions to this assignment.

---LISTING FRACTALS---

Pentagon: 
In an early lab session, a fellow student constructed a simple recursive hexagon using a length he either calculated or found online. We were told to take note of the length and attempt it ourselves. 

scurve: 
This personal fractal was created by accident as I was attempting to make a sierpinski carpet using lecture notes. A missing pen.left(90) command had seemed to cause this. 

Carpet: 
I wanted to include a carpet that had a fill function like what was shown by another student. As this fractal could be filled I chose to fill it with the colour orange.

Square: 
The first fractal that I drew out on pen and paper to fully understand recursion. I mapped out the points where I would call the square. 

Circles:
I saw an image online of three tangent circles fitting inside a bigger circle. I decided I wanted to create this as one of my personal fractals. I searched online to find information to find out the measurements I need to know. I found that the radii of the smaller circles were 1.392. Now as that meant the radius of the bigger circle had to be 3l, 1.392 had to be divided by three to find the figure used in my code to create the smaller circles. This now meant that the radius of the big circle was equal to l. Now I was able to draw out how I would map out my points on pen and paper. As it was given what angles I needed to turn the pen as the centre points of each tangent circle formed an equilateral triangle, I was able to find the points at which I needed to call the circles at. 

Pentagram:
This was my personal fractal. I first got the idea of creating this fractal after seeing an image of a pentagram inside a pentagon which then went on to be recursive in itself. While this initially seemed tricky, I first found an image of this fractal which contained all the angles that I needed to know. I then found a website called rechneronline.de which contained a pentagram calculator. Simply by giving l (length of the pentagon the value 1, I had all the info I needed to begin work on this fractal. First I drew the pentagon. I now needed to complete the pentagram. The chord length was important in doing so. This value was .61803398875. I also used the long chord slice in constructing my pentagram. Since I now had this constructed, I had to use the short chord length when calling my pentagram. I decided to remove the pentagon from the fractal entirely as I already had a pentagon fractal and I wanted to produce something unique to my own assignment. 

---INFORMATION ABOUT MY INTERFACE---

As I could not attend the lecture and lab which covered the interface, I caught up by first examining the code which was needed to construct the money converter. I took what was here to make my first practice attempt to make an interface. For each fractal, I constructed a singular button. The fractal would draw on a separate screen. By attending catch up labs I was able to follow instruction and construct a canvas frame in the same window as my buttons. I replaced the buttons with a dropdown menu so the fractals could be selected from here. Now I wanted to add my own touches. For the near entirety of my assignment I have been using my mac book pro which has a 13 inch screen. I decided that I wanted to size the canvas frame and the size of window to accommodate this so my work would look accessible and presentable on this device and for larger screens as well. Next I wanted to use a washed out lighter colour for the background of my window to make it look nice and not overwhelming to look at. 

Next I wanted to add my own personal touch to my interface. I decided I wanted to take a playful and entertaining approach which would offer the user a sense of enjoyment through giving the them the option of selection for both the pen and location. Firstly I set the pen shape to a turtle. Next I wanted to treat the fill of the canvas frame as locations where the turtle could be placed. My first attempt at achieving my desired effect was unfortunately unsuccessful as I wanted to have another dropdown menu in my control panel to do so. Upon finding out that it would not be possible to do so I decided to try another approach.

 I created a completely new panel for this option and place this underneath the canvas. I consulted a tkinter colour list to find out which colours I wanted to use. I then assigned a location to each colour.  I went on to define each location by using screen.bgcolor to give them a colour which matched the location I wanted. I decided four buttons with two rows and two columns would look nice, small and neat. I carried out an extremely similar process to make another panel. This panel allows the user to pick which “ninja turtle” they want to select as a pen. Each colour corresponds to the colour of the masks of the characters from the  TV show Teenage Mutant Ninja Turtles. I also made this a four button panel so it would align nicely with my previous one.

