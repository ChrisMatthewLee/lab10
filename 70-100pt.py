##########################################
#                                        #
#             Draw a house!              #
#                                        #
##########################################

# Use create_line(), create_rectangle() and create_oval() to make a 
# drawing of a house using the tKinter Canvas widget.

# 70pt: House outline (roof and the house)
# 80pt: Square windows and a door
# 90pt: A door handle plus a chimney!
# 100pt: Green grass on the ground and a red house!

# Minus 5pts if your code has no comments
# Minus 10pts if you only commit once to github

from Tkinter import *
root = Tk()

# Create the canvas widget
drawpad = Canvas(root, width=800,height=600, background='white')
drawpad.grid(row=0, column=1)

# Insert your code here to draw the house!

#roof
line1 = drawpad.create_line(200,200,400,50)
line2 = drawpad.create_line(400,50,600,200)

#red outline
red_square = drawpad.create_rectangle(200,200,600,500, fill= "red" )

#window1
window1 = drawpad.create_rectangle(250,350,300,300, fill= 'white')

#window2
window2 = drawpad.create_rectangle(550,350,500,300, fill= 'white')

#door
door = drawpad.create_rectangle(350,500,450,350, fill= 'white')

#grass
grass = drawpad.create_rectangle(0,500,1000,1000, fill= 'green')

#handle
handle = drawpad.create_rectangle(430,450,445,425,)

root.mainloop()

