from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import Menu
from tkinter import messagebox
import random

##bl = 'Blue'
##ye = 'Yellow'
##or = 'Orange'
##gr = 'Green'
##vl = 'Violet'

colors = ['Blue', 'Yellow', 'Orange', 'Green', 'Violet']
#colors = ['bl', 'ye', 'or', 'vl', 'gr']
num_of_dupl_colors = 1
code_length = 4
creationOfCbanswer_list = [410, 370, 330, 290, 250, 210, 170, 130, 90, 50]
#counter = 0

#def mainMenu():
    #d = Mastermind()
    #d.mainloop()
    #printingcode(self, a)
    #print(d.guesses_list)
    
    #Mastermind().mainloop()
    #guesses_list = Mastermind.codeBreaker(self)
    #users_input_1 = inputList(self)
    #guesses_list = Mastermind.codeBreaker(users_input_1)
    #Mastermind.codeprinting(guesses_list)
    #Mastermind.codeprinting(Mastermind.codeBreaker(self))

class MainControler():
    def __init__(self):
        self.run()
    
    def run(self):
        #generalselections = Generalselections()
        mastermind = Mastermind()
        m_1 = MastermindsCode()



       
##class Generalselections(tk.Tk):
##    def __init__(self):
##        super(Generalselections, self).__init__()
##        self.geometry("550x590")
##        self.title('Mastermind game')
##        self.configure(background = "PeachPuff3")
##        self.startbutton = ttk.Button(self, text = "Start", command = self.runTheMainGameWindow())
##        self.startbutton.place(x = 40, y = 100)
##
##
##    def runTheMainGameWindow(self):
##        Mastermind()
##        pass
    
    #def firstSelectionsWindow(self):
        
        

        
class MastermindsCode():
    counter = 0
    def __init__(self):
        MastermindsCode.color = []
        MastermindsCode.temp_color_list = []
        self.creationOfCode(colors = colors)

    def creationOfCode(self, colors):
        colors = list(colors)
        while True:
            if MastermindsCode.counter <= len(colors):
                MastermindsCode.color = random.choice(colors)
                #print("MastermindsCode.color :", MastermindsCode.color)
                duplicated_color = MastermindsCode.temp_color_list.count(MastermindsCode.color)
            if duplicated_color <= (num_of_dupl_colors - 1): #and len(temp_color_list) < 5:
                MastermindsCode.temp_color_list.append(MastermindsCode.color)
                MastermindsCode.counter += 1
            if len(MastermindsCode.temp_color_list) == 2:break
        print("MastermindsCode.temp_color_list :", MastermindsCode.temp_color_list)
        return MastermindsCode.temp_color_list
        #print("MastermindsCode.temp_color_list :", MastermindsCode.temp_color_list)
        
    
        
class Mastermind(tk.Tk):
    #Mastermind.guesses_list = []
    counter = 0
    def __init__(self):
        Mastermind.guesses_list = []
        Mastermind.feedback_list = []
        Mastermind.label_answer_cb_list = []
        Mastermind.label_feedback_list = []
        # Creation of main window
        super(Mastermind, self).__init__()
        #self.createMenuBar()
        self.geometry("550x590")
        self.title('Mastermind game')
        self.configure(background = "PeachPuff3")

        # color information
        self.label_info_head = Label(self, text = "Color table info.", font = ("Calibri", 12), background = "PeachPuff3")
        self.label_info_head.place(x = 20, y = 530)
        self.label_info = Label(self, text = "bl = Blue,   ye = Yellow,   or = Orange,   vl = Violet, gr = Green", font = ("Calibri", 12), background = "PeachPuff3")
        self.label_info.place(x = 20, y = 550)
        # menubar creation
        self.createMenuBar()
        
        # codebreaker's answer labels
        self.creationOfCbanswernumAndLabels()

        # codebreaker's answer feedback
        self.creationOfCbFeedback()

        # Creation of Labelframe
        #self.labelFrame = ttk.LabelFrame(self, text = "Codebraker guesses", width = 490,height = 383)
        #self.labelFrame.place(x = 10, y = 0)


        # 
        # Creation of guess button
        self.guess_button = ttk.Button(self, text = "Guess", command = lambda:self.answerAndFeedbackCbLabels
                                       (self.printingcode(copiedguess = self.codeBreaker(),
                                        copiedlist =MastermindsCode.creationOfCode(self, colors = colors))
                                        ,code = self.codeBreaker()))
        #self.button = ttk.Button(self, text = "Guess", command = self.codeBreaker)
        self.config(width = 8, height = 2)
        self.guess_button.place(x = 300, y = 480)

        # Creation of textboxes 1 & 2
        self.label_cb_ins_box_head = Label(self, text = "Codebreaker's input.", font = ("Calibri", 13), background = "PeachPuff3")
        self.label_cb_ins_box_head.place(x = 30, y = 455)
        self.textbox_1 = ttk.Entry(self)
        self.textbox_1.place(x = 30, y = 480)
        self.textbox_1.config(width = 5, font = ("Calibri", 12))
        #self.textbox_1.focus()

        self.textbox_2 = ttk.Entry(self)
        self.textbox_2.place(x = 80, y = 480)
        self.textbox_2.config(width = 5, font = ("Calibri", 12))
        #self.textbox_2.focus()
        
        self.textbox_3 = ttk.Entry(self)
        self.textbox_3.place(x = 130, y = 480)
        self.textbox_3.config(width = 5, font = ("Calibri", 12))
        #self.textbox_3.focus()

        self.textbox_4 = ttk.Entry(self)
        self.textbox_4.place(x = 180, y = 480)
        self.textbox_4.config(width = 5, background = "SkyBlue3", font = ("Calibri", 12))
        #self.textbox_4.focus()

       
    def creationOfCbanswernumAndLabels(self):
        self.label_head_cb = Label(self, text = "Codebreaker's answers.", font = ("Calibri", 13), background = "PeachPuff3")
        self.label_head_cb.place(x = 8, y = 10)
        for _ in range(10):
            #self.label_cb = Label(self, text = str(_ + 1) + "  ----")
            self.label_cb = Label(self, text = str(_ + 1), font = ("Calibri", 12), background = "PeachPuff3")
            self.label_cb.place(x = 8, y = creationOfCbanswer_list[_])
            Mastermind.label_feedback_list.append(Label(self, background = "NavajoWhite2", font = ("Calibri", 12), width = 24))
            Mastermind.label_feedback_list[_].place(x = 320, y = creationOfCbanswer_list[_])
            Mastermind.label_answer_cb_list.append(Label(self, background = "light grey", font = ("Calibri", 12), width = 24))
            Mastermind.label_answer_cb_list[_].place(x = 30, y = creationOfCbanswer_list[_])
        #Mastermind.label_answer_cb_list[0].config(background = "light blue")
        Mastermind.label_answer_cb_list[0].config(relief = SUNKEN, background = "LightSteelBlue3")

    def answerAndFeedbackCbLabels(self, text, code):

        if Mastermind.counter < 10:
            text = list(Mastermind.feedback_list)
            code = list(Mastermind.guesses_list)
            #print("text", text)
            #print("code", code)

            
            Mastermind.label_answer_cb_list[Mastermind.counter].config(background = "LightSteelBlue3")
            Mastermind.label_answer_cb_list[Mastermind.counter].config(text = code)
            Mastermind.label_answer_cb_list[Mastermind.counter].place(x = 30, y = creationOfCbanswer_list[Mastermind.counter])

            Mastermind.label_feedback_list[Mastermind.counter].config(text = text)
            Mastermind.label_feedback_list[Mastermind.counter].place(x = 320, y = creationOfCbanswer_list[Mastermind.counter])

            Mastermind.counter += 1
            if Mastermind.counter < 10:
                #Mastermind.label_answer_cb_list[Mastermind.counter].config(background = "light blue")
                Mastermind.label_answer_cb_list[Mastermind.counter].config(relief = SUNKEN, background = "LightSteelBlue3")
                
            if Mastermind.counter == 10:
                self.guess_button['state'] = DISABLED
                Mastermind.endOfTheGameOutOfGuesses(self)
                
            elif Mastermind.feedback_list.count("Red") == 4:
                self.guess_button['state'] = DISABLED
                Mastermind.endOfGameWinner(self)
#######################################
        #elif Mastermind.counter == 9:
            #Mastermind.endOfTheGame(self)
        #else: print("End of the game")
        
    def creationOfCbFeedback(self):
        self.label_feedback_head = Label(self, text = "Codebreaker's feedback.", font = ("Calibri", 13), background = "PeachPuff3")
        self.label_feedback_head.place(x = 300, y = 10)
        for __ in range(10):
            #self.label_feedback = Label(self, text = "feedback " + str(__ + 1))
            self.label_feedback = Label(self, text = str(__ + 1), font = ("Calibri", 12), background = "PeachPuff3")
            self.label_feedback.place(x = 300, y = creationOfCbanswer_list[__])
        #self.label_2 = Label(self, text = "2")
        #self.label_2.place(x = 20, y = 300)
            #self.label.grid(column = 0, row = 0)
            
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

    #def inputList(self):
        #users_input_1 = (self.textbox_1.get()).split("-")
        #return users_input_1

    def codeBreaker(self):
        Mastermind.guesses_list.clear()
        #self.guesses_list = []
        #self.guesses_list.clear() # Clears the list
        
        # textbox_1 ckeck
        users_input_1 = self.textbox_1.get()
        #if users_input_1 in colors:
        if users_input_1 == "bl": Mastermind.guesses_list.append("Blue")
        elif users_input_1 == "ye": Mastermind.guesses_list.append("Yellow")   
        elif users_input_1 == "or": Mastermind.guesses_list.append("Orange")
        elif users_input_1 == "vl": Mastermind.guesses_list.append("Violet")
        elif users_input_1 == "gr": Mastermind.guesses_list.append("Green")
        #else: Mastermind.userInputWarningWrongColor(self)
        #else:
            #print("Wrong color. Try again.")
            #break
        #return "Wrong"

    
        # textbox_2 ckeck
        users_input_2 = self.textbox_2.get()
        #if users_input_2 in colors:
        if users_input_2 == "bl": Mastermind.guesses_list.append("Blue")
        elif users_input_2 == "ye": Mastermind.guesses_list.append("Yellow")
        elif users_input_2 == "or": Mastermind.guesses_list.append("Orange")
        elif users_input_2 == "vl": Mastermind.guesses_list.append("Violet")
        elif users_input_2 == "gr": Mastermind.guesses_list.append("Green")

##        users_input_3 = self.textbox_3.get()
##        #if users_input_3 in colors:
##        if users_input_3 == "bl": Mastermind.guesses_list.append("Blue")
##        elif users_input_3 == "ye": Mastermind.guesses_list.append("Yellow")   
##        elif users_input_3 == "or": Mastermind.guesses_list.append("Orange")
##        elif users_input_3 == "vl": Mastermind.guesses_list.append("Violet")
##        elif users_input_3 == "gr": Mastermind.guesses_list.append("Green")
                    
##        users_input_4 = self.textbox_4.get()
##        #if users_input_4 in colors:
##        if users_input_4 == "bl": Mastermind.guesses_list.append("Blue")
##        elif users_input_4 == "ye": Mastermind.guesses_list.append("Yellow")   
##        elif users_input_4 == "or": Mastermind.guesses_list.append("Orange")
##        elif users_input_4 == "vl": Mastermind.guesses_list.append("Violet")
##        elif users_input_4 == "gr": Mastermind.guesses_list.append("Green")
##                        
##        #print("Mastermind.guesses_list :", Mastermind.guesses_list)
        return Mastermind.guesses_list #else:
        #Mastermind.userInputWarningWrongColor(self) #return "x"
        

    def printingcode(self, copiedguess, copiedlist):
        #guess = copiedguess
        #if guess == "Wrong":
            #print("Wrong")

        #else:
        Mastermind.feedback_list.clear()
        guess = list(copiedguess)
        #print("guess :", guess)
        code = list(copiedlist)
        #print("code :", code)
        #print("--" * 10)
        #print("\noriginal_guess_list :", guess)

        #if "x" in guess:
            #return None
        #else:
        for num in range(len(guess)):
        #for num in code_length:
            #print("num :", num)
            #print("len(guess) :", len(guess))
            if guess[num] == code[num]:
                #print("yes guess == code")
                guess[num] = 1
                code[num] = 2
                Mastermind.feedback_list.append("Red")


        for num in range(len(guess)):
            if guess[num] in code:
                Mastermind.feedback_list.append("White")
            #else:
                
                #Mastermind.feedback_list.append("White")
                #for col in guess:
                    #print(col)
        #code_list = code
        #print("\nMastermind.feedback_list :", Mastermind.feedback_list)
        #print("\nfinal_guess_list :", guess)
        #print("\ncode_list :", code)
        return Mastermind.feedback_list
        
        #for num in range(counter):
            
            #counter += 1
        #else: print("Wrong.")
        
        
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

    #def codeprinting(self, x):
        #a = list(x)
        #print(x)
        #pass
        
    #def codemakersFeedback(self, guessesCopy):
        #pass
        

    def endOfTheGameOutOfGuesses(self):
        messagebox.showinfo(title = "Out of guesses!", message = '''You lost try again...''')
        Mastermind.destroy

    def userInputWarningWrongColor(self): 
        messagebox.showinfo(title = "Warning", message = '''Wrong user's input''')
        
    def endOfGameWinner(self):
        messagebox.showinfo(title = "Winner!", message = '''You win you are
the Codebraker''')
        
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
    MainControler() 

    #mainMenu()
    #Mastermind().mainloop()
