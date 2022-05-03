from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import Menu
from tkinter import messagebox

code = ["Blue", "Violet"]
colors = ['bl', 'ye', 'or', 'vl']
creationOfCbanswer_list = [410, 370, 330, 290, 250, 210, 170, 130, 90, 50]


class Mastermind(tk.Tk):
    counter = 0
    def __init__(self):
        Mastermind.guesses_list = []
        Mastermind.feedback_list = []
        # Creation of main window
        super(Mastermind, self).__init__()
        #self.createMenuBar()
        self.geometry("550x590")
        self.title('Mastermind game')
        #self.configure(background = "blue")

        # color information
        self.label_info_head = Label(self, text = "Color table info.", font = ("Calibri", 12))
        self.label_info_head.place(x = 20, y = 530)
        self.label_info = Label(self, text = "bl = Blue,   ye = Yellow,   or = Orange,   vl = Violet", font = ("Calibri", 12))
        self.label_info.place(x = 20, y = 550)
        
        # menubar creation
        self.createMenuBar()
        
        # codebreaker's answer labels
        self.creationOfCbanswernum()

        # codebreaker's answer feedback
        self.creationOfCbFeedback()

        # Creation of Labelframe
        #self.labelFrame = ttk.LabelFrame(self, text = "Codebraker guesses", width = 490,height = 383)
        #self.labelFrame.place(x = 10, y = 0)

        # Creation of guess button
        self.button = ttk.Button(self, text = "Guess", command = lambda:self.answerAndFeedbackCbLabels(self.printingcode(copiedguess = self.codeBreaker(), copiedlist = code), code = self.codeBreaker()))
        #self.button = ttk.Button(self, text = "Guess", command = self.codeBreaker)
        self.config(width = 8, height = 2)
        self.button.place(x = 300, y = 480)

        # Creation of textboxes 1 & 2
        self.label_cb_ins_box_head = Label(self, text = "Codebreaker's input.", font = ("Calibri", 13))
        self.label_cb_ins_box_head.place(x = 20, y = 455)
        self.textbox_1 = ttk.Entry(self)
        self.textbox_1.place(x = 20, y = 480)
        self.textbox_1.config(width = 12, font = ("Calibri", 12))

        self.textbox_2 = ttk.Entry(self)
        self.textbox_2.place(x = 150, y = 480)
        self.textbox_2.config(width = 12, font = ("Calibri", 12))

       
    def creationOfCbanswernum(self):
        self.label_head_cb = Label(self, text = "Codebreaker's answers.", font = ("Calibri", 13))
        self.label_head_cb.place(x = 8, y = 10)
        for _ in range(10):
            #self.label_cb = Label(self, text = str(_ + 1) + "  ----")
            self.label_cb = Label(self, text = str(_ + 1), font = ("Calibri", 12))
            self.label_cb.place(x = 8, y = creationOfCbanswer_list[_])

        
    def answerAndFeedbackCbLabels(self, text, code):
        if Mastermind.counter < 10:
            text = list(Mastermind.feedback_list)
            code = list(Mastermind.guesses_list)
            print("text", text)
            print("code", code)
            self.label_feedback = Label(self, text = text, background = "white", font = ("Calibri", 12), width = 24)
            self.label_feedback.place(x = 320, y = creationOfCbanswer_list[Mastermind.counter])
            self.label_answer_cb = Label(self, text = code, background = "light blue", font = ("Calibri", 12), width = 24)
            self.label_answer_cb.place(x = 30, y = creationOfCbanswer_list[Mastermind.counter])
            Mastermind.counter += 1
        else: print("End of the game")
   

    def creationOfCbFeedback(self):
        self.label_feedback_head = Label(self, text = "Codebreaker's feedback.", font = ("Calibri", 13))
        self.label_feedback_head.place(x = 300, y = 10)
        for __ in range(10):
            #self.label_feedback = Label(self, text = "feedback " + str(__ + 1))
            self.label_feedback = Label(self, text = str(__ + 1), font = ("Calibri", 12))
            self.label_feedback.place(x = 300, y = creationOfCbanswer_list[__])
     

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
        Mastermind.guesses_list.clear()
        
        # textbox_1 ckeck
        users_input_1 = (self.textbox_1.get())
        if users_input_1 in colors:
            if users_input_1 == "bl": Mastermind.guesses_list.append("Blue")
            elif users_input_1 == "ye": Mastermind.guesses_list.append("Yellow")   
            elif users_input_1 == "or": Mastermind.guesses_list.append("Orange")
            elif users_input_1 == "vl": Mastermind.guesses_list.append("Violet")
            
        # textbox_2 ckeck
        users_input_2 = self.textbox_2.get()
        if users_input_2 in colors:
            if users_input_2 == "bl": Mastermind.guesses_list.append("Blue")   
            elif users_input_2 == "ye": Mastermind.guesses_list.append("Yellow")
            elif users_input_2 == "or": Mastermind.guesses_list.append("Orange")
            elif users_input_2 == "vl": Mastermind.guesses_list.append("Violet")
                
        return Mastermind.guesses_list


    def printingcode(self, copiedguess, copiedlist):
        Mastermind.feedback_list.clear()
        guess = list(copiedguess)
        code = list(copiedlist)
        #print("--" * 10)
        #print("\noriginal_guess_list :", guess)
        for num in range(len(guess)):
            if guess[num] == code[num]:
                guess[num] = 1
                code[num] = 2
                Mastermind.feedback_list.append("Red")

        for num in range(len(guess)):
            if guess[num] in code:
                Mastermind.feedback_list.append("White")
            
        #print("\nMastermind.feedback_list :", Mastermind.feedback_list)
        #print("\nfinal_guess_list :", guess)
        #print("\ncode_list :", code)
        return Mastermind.feedback_list
        
        
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
    Mastermind()
   
