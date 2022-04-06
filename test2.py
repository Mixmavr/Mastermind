from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("500x500")
root.title('Mastermind game')

#frame = Frame(root)
#frame.pack()

#class Mastermind(tk.Frame):

#############################
# Buttons label frames
labelframe1 = LabelFrame(root, text = "Mastermind Block", width = 495,height = 383)
labelframe1.place(x = 5, y = 0)

#labelframe2 = LabelFrame(root, text = "Mastermind Buttons", width = 100, height = 50)
#labelframe2 = LabelFrame(x = 5 , y = 400)

#############################
# Help button event
def helpIndex():
    messagebox.showinfo("Help Index", '''Press color buttons to fill empty boxes and guess
the color combination that Codemaker is hiding
Good Luck and enjoy...''')

#############################
# About button event
def About():
    messagebox.showinfo("About", '''Mastermind game.
A creation of Mavrogiannis Michail
and Panourgias Panagiotis
for Open Hellenic Univercity
and PLHPRO lesson,
Academic Year 2022.''')

def callback():
   frame1 = Label(root, text="1", bg="red",fg="white", width = 8, height = 2, relief = SUNKEN)#, padx=15, pady=15)

#############################                      
# Buttons to create code
redcolorbutton = Button(root, text = "Red", fg = "red", width = 8, height = 2, command = callback)
redcolorbutton.place(x = 10, y = 408)

#menu_button1 = Menubutton(root, text = "1st frame")
#menu = Menu(menu_button1, tearoff = 0)
#menu_button1.place(x = 10, y = 408)
#for i in range(2):
    #add_radiobutton(label = red, value = red, variable = red)

bluecolorbutton = Button(root, text = "Blue", fg = "blue", width = 8, height = 2)
bluecolorbutton.place(x = 80, y = 408)

orangecolorbutton = Button(root, text = "Orange", fg = "orange", width = 8, height = 2)
orangecolorbutton.place(x = 150, y = 408)

yellowcolorbutton = Button(root, text = "Yellow", fg = "yellow", width = 8, height = 2)
yellowcolorbutton.place(x = 220, y = 408)

purplecolorbutton = Button(root, text = "Purple", fg = "purple", width = 8, height = 2)
purplecolorbutton.place(x = 290, y = 408)

guessbutton = Button(root, text = "Guess", fg = 'black', width = 8, height = 2)
guessbutton.place(x = 420, y = 450)

#############################
# Menubar in window
# File Menu
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command = None)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.destroy)
menubar.add_cascade(label="File", menu=filemenu)

# Help Menu
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command = helpIndex)
helpmenu.add_command(label="About...", command=About)
menubar.add_cascade(label="Help", menu=helpmenu)

#############################

frame1 = Label(root, text="1", bg="light blue",
                    fg="white", width = 8, height = 2, relief=SUNKEN)

frame1.place(x = 10, y = 340)


frame2 = Label(root, text="2", bg="light blue",
                    fg="white", width = 8, height = 2, relief=SUNKEN)
frame2.place(x = 80, y = 340)


frame3 = Label(root, text="3", bg="light blue",
                    fg="white", width = 8, height = 2, relief=SUNKEN)

frame3.place(x = 150, y = 340)


frame4 = Label(root, text="4", bg="light blue",
                    fg="white", width = 8, height = 2, relief=SUNKEN)

frame4.place(x = 220, y = 340)


#frame1.geometry("100x100")
#Displaying the frame1 in row 0 and column 0
#frame1.grid(row=500, column=500)



#############################

def callback():
   frame1 = Label(bg = "red")#, padx=15, pady=15)
    #frame1.place(x = 100, y = 100)

#############################

#root = Tk()
#root.geometry("500x500")
#root.title('Mastermind game')
root.config(menu=menubar)
root.mainloop()


#############################

#for i in range(2):
    #for j in range (2):
if redcolorbutton.bind("<Button-1>", callback()):
    print(1)
