from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import Menu
from tkinter import messagebox

code = ["Blue", "Yellow"]
colors = ['b', 'y', 'o']

#def mainMenu():
    #Mastermind().mainloop()
    #guesses_list = Mastermind.codeBreaker(self)
    #Mastermind.codeprinting(guesses_list)
    #Mastermind.codeprinting(Mastermind.codeBreaker(self))

#class MainControler():
    #def __init__(self):
        #self.run()
    
    #def run(self):
        #numOfGuesses = 0
        #Mastermind().mainloop()
        #guesses_list = Mastermind.codeBreaker(self)
        #Mastermind.codeprinting(guesses_list)
        #Mastermind.codeprinting(Mastermind.codeBreaker(self))
        
        
class Mastermind(tk.Tk):
    #guesses_list = []
    #counter = 0
    def __init__(self):
        # Creation of main window
        super(Mastermind, self).__init__()
        self.createMenuBar()
        self.geometry("500x500")
        self.title('Mastermind game')
        #self.configure(background = "blue")

        # codebreaker's answer labels
        

        # Creation of Labelframe
        self.labelFrame = ttk.LabelFrame(self, text = "Codebraker guesses", width = 490,height = 383)
        self.labelFrame.place(x = 5, y = 0)

        # Creation of guess button
        self.button = ttk.Button(self, text = "Guess", command = self.codeBreaker)
        self.config(width = 8, height = 2)
        self.button.place(x = 300, y = 430)

        # Creation of textboxes 1 & 2
        self.textbox_1 = ttk.Entry(self)
        self.textbox_1.place(x = 20, y = 430)
        self.textbox_1.config(width = 12, font = ("Calibri", 13))
        #self.textbox_1.focus()

        self.textbox_2 = ttk.Entry(self)
        self.textbox_2.place(x = 150, y = 430)
        self.textbox_2.config(width = 12, font = ("Calibri", 13))
        #self.textbox_2.focus()
        
        
    def createMenuBar(self):
        menubar = Menu(self)
        self.config(menu = menubar)
        file_menu = Menu(menubar, tearoff = 0)

        # Creation of file menu
        menubar.add_cascade(label = "File", menu = file_menu)
        file_menu.add_command(label = "New", command = None)
        file_menu.add_separator()
        file_menu.add_command(label = "Exit", command = self.destroy)

        # Creation of help menu
        
        helpmenu = Menu(menubar, tearoff = 0)
        helpmenu.add_command(label = "Help Index", command = self.helpIndex)
        helpmenu.add_command(label = "About...", command = self.about)
        menubar.add_cascade(label = "Help", menu = helpmenu)

    def codeBreaker(self):
        self.guesses_list = []
        self.guesses_list.clear() # Clears the list
        
        # textbox_1 ckeck
        users_input_1 = self.textbox_1.get()
        if users_input_1 in colors:
            
            if users_input_1 == "b":
                self.guesses_list.append("Blue")
                #return "Blue"
            elif users_input_1 == "y": self.guesses_list.append("Yellow")
                
            elif users_input_1 == "o": self.guesses_list.append("Orange")

        
        # textbox_2 ckeck
        users_input_2 = self.textbox_2.get()
        if users_input_2 in colors:

            if users_input_2 == "b": self.guesses_list.append("Blue")
                
            if users_input_2 == "y":
                self.guesses_list.append("Yellow")
                #return "Yellow"
            elif users_input_2 == "o": self.guesses_list.append("Orange")
                
        if len(self.guesses_list) == 0: return None

        elif len(self.guesses_list) < 2:
            self.guesses_list.clear()
            return None
        #else: return print(self.guesses_list)
        else:return print(self.guesses_list)
        
    #def codeBreakersAnswerLabels(self, listtocopy):
        #Mastermind.counter =+ 1
        #guess = list(listtocopy)
        #self.label = Label(self, text = self.guess[0])
        #self.config(font = ("Calibri", 13))
        #self.place(x = 20, y = 100)
        
        #pass

    #def guessesPrint(self, guessesForPrint):
        #guess = list(guessesForPrint)
        #print(guessesForPrint)
        #self.label = Label(self, text = guessesForPrint)
        #self.label.config(font = ("Calibri", 13))
        #self.label.place(x = 0, y = 0)
        #pass

    def codeprinting(self, x):
        a = list(x)
        print(x)
        pass
        
    def codemakersFeedback(self, guessesCopy):
        pass    
        

    def about(self):
        messagebox.showinfo(title = "About", message = '''Mastermind game.
A creation of Mavrogiannis Michail
and Panourgias Panagiotis
for Open Hellenic Univercity
and PLHPRO lesson,
Academic Year 2022.''')

    def helpIndex(self):
        messagebox.showinfo("Help Index", '''Press color buttons to fill empty boxes and guess
the color combination that Codemaker is hiding
Good Luck and enjoy...''')
    
        
if __name__ == "__main__":
    #Mastermind()
    #MainControler() 

    #mainMenu()
    Mastermind().mainloop()
