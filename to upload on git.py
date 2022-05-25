from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import Menu
from tkinter import messagebox
import random
from random import sample

## Color Info
##bl = 'Blue'
##ye = 'Yellow'
##or = 'Orange'
##gr = 'Green'
##vl = 'Violet'

available_colors = ['Blue', 'Yellow', 'Orange', 'Green', 'Violet']
shorted_colors = ['bl', 'ye', 'or', 'vl', 'gr']
duplicate_colors_in_code = True
#duplicate_colors_in_code = False
num_of_dupl_colors = 1
code_length = 4
creationOfCbanswer_list = [410, 370, 330, 290, 250, 210, 170, 130, 90, 50]


class HelpAndAbout():
    def __init__(self):
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

        
class FirstsSettingsWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("280x380")
        self.title("Mastermind Settings")

# Creation of start button and label
        self.start_button = ttk.Button(self, text = "Start the game", command = self.openGameWindow)
        self.start_button.place(x = 30, y = 335)
        self.good_luck_label = ttk.Label(self, text = "and Good Luck !!!")
        self.good_luck_label.place(x = 118, y = 338)

    
        # Call of menubar in settings window
        self.settingsWindowCreationMenuBar()

        self.settings_textbox = ttk.Entry(self)
        self.settings_textbox.place(x = 30, y = 180)
        self.settings_textbox.config(width = 5, font = ("Calibri", 12))
        
    
        # Creation of menubar in settings window
    def settingsWindowCreationMenuBar(self):
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
        helpmenu.add_command(label = "Help Index", command = lambda:HelpAndAbout.helpIndex(self))
        helpmenu.add_command(label = "About...", command = lambda:HelpAndAbout.about(self))
        menubar.add_cascade(label = "Help", menu = helpmenu)

    # Duplication settings
    def settings(self):
        users_settings_input = self.settings_textbox.get()
        
        if users_settings_input == 1:
            print("1")
            return 1
        elif users_settings_input == 2:
            return 2
        
        
    # Creation of second window interaction    
    def openGameWindow(self):
        mastermind = Mastermind()
        mastermind.grab_set()


class Mastermind(tk.Toplevel):

    counter = 0
    
    def __init__(self):
        # Creation of necessary lists
        Mastermind.color = []
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
        self.label_info_head_upper = Label(self, text = "Color table info.", font = ("Calibri", 12),
                                     background = "PeachPuff3")
        self.label_info_head_upper.place(x = 8, y = 518)
        self.label_info_head_down = Label(self, text = "The available colors are to choose are bellow:",
                                          font = ("Calibri", 12),
                                     background = "PeachPuff3")
        self.label_info_head_down.place(x = 8, y = 538)
        self.label_info = Label(self, text = "bl = Blue,  ye = Yellow,  or = Orange,  vl = Violet,  gr = Green",
                                font = ("Calibri", 12), background = "PeachPuff3")
        self.label_info.place(x = 8, y = 558)
        # menubar creation
        self.mainWindowCreationMenuBar()
        
        # codebreaker's answer labels
        self.creationOfCbanswernumAndLabels()

        # codebreaker's answer feedback
        self.creationOfCbFeedback()

        # Creation of guess button
        self.guess_button = ttk.Button(self, text = "Guess", command = lambda:self.comandOfGuessButton())
        self.config(width = 8, height = 2)
        self.guess_button.place(x = 300, y = 480)

        # Creation of textboxes 1, 2, 3 & 4
        self.label_cb_ins_box_head = Label(self, text = "Codebreaker's input.", font = ("Calibri", 13),
                                           background = "PeachPuff3")
        self.label_cb_ins_box_head.place(x = 30, y = 455)
        self.textbox_1 = ttk.Entry(self)
        self.textbox_1.place(x = 30, y = 480)
        self.textbox_1.config(width = 5, font = ("Calibri", 12))

        self.textbox_2 = ttk.Entry(self)
        self.textbox_2.place(x = 80, y = 480)
        self.textbox_2.config(width = 5, font = ("Calibri", 12))
        
        self.textbox_3 = ttk.Entry(self)
        self.textbox_3.place(x = 130, y = 480)
        self.textbox_3.config(width = 5, font = ("Calibri", 12))

        self.textbox_4 = ttk.Entry(self)
        self.textbox_4.place(x = 180, y = 480)
        self.textbox_4.config(width = 5, background = "SkyBlue3", font = ("Calibri", 12))


    def comandOfGuessButton(self):
        creationofcode = self.creationOfCode(colors = available_colors, duplicate_colors_in_code
                                                                        = duplicate_colors_in_code)   

        codebreaker = self.codeBreaker()
        if self.validationOfCbGuess(guesscbreturnablevalue = codebreaker) == 1:
            printingcode = self.printingcode(copiedguess = codebreaker, copiedlist = creationofcode)
            answerandfeedbackcblabels = self.answerAndFeedbackCbLabels(text = printingcode,
                                                                           code = codebreaker)
        else:self.errorInputWarning()

    def validationOfCbGuess(self, guesscbreturnablevalue):        
        guesscbreturnablevalue = list(Mastermind.guesses_list)
        if len(guesscbreturnablevalue) != code_length:
            return 2 # It means True
        else: return 1 # It means False




    def creationOfCode(self, colors, duplicate_colors_in_code):
        available_colors_tuple = list(colors)
        if len(Mastermind.color) == code_length:
            return Mastermind.color

        if duplicate_colors_in_code is True:
            Mastermind.color = random.sample(available_colors_tuple, code_length)
            print(Mastermind.color)
            return Mastermind.color
        else:
            Mastermind.color = random.choices(available_colors_tuple, k = code_length)
            #print(Mastermind.color)
            return Mastermind.color




       
    def creationOfCbanswernumAndLabels(self):
        self.label_head_cb = Label(self, text = "Codebreaker's answers.", font = ("Calibri", 13),
                                   background = "PeachPuff3")
        self.label_head_cb.place(x = 8, y = 10)
        for _ in range(10):
            self.label_cb = Label(self, text = str(_ + 1), font = ("Calibri", 12), background = "PeachPuff3")
            self.label_cb.place(x = 8, y = creationOfCbanswer_list[_])
            Mastermind.label_feedback_list.append(Label(self, background = "NavajoWhite2",
                                                        font = ("Calibri", 12), width = 24))
            Mastermind.label_feedback_list[_].place(x = 320, y = creationOfCbanswer_list[_])
            Mastermind.label_answer_cb_list.append(Label(self, background = "light grey",
                                                         font = ("Calibri", 12), width = 24))
            Mastermind.label_answer_cb_list[_].place(x = 30, y = creationOfCbanswer_list[_])
        Mastermind.label_answer_cb_list[0].config(relief = SUNKEN, background = "LightSteelBlue3")



    def answerAndFeedbackCbLabels(self, text, code):

        if Mastermind.counter < 10:
            text = list(Mastermind.feedback_list)
            code = list(Mastermind.guesses_list)
            
            Mastermind.label_answer_cb_list[Mastermind.counter].config(background = "LightSteelBlue3")
            Mastermind.label_answer_cb_list[Mastermind.counter].config(text = code)
            Mastermind.label_answer_cb_list[Mastermind.counter].place(x = 30,
                                                                      y = creationOfCbanswer_list[Mastermind.counter])

            Mastermind.label_feedback_list[Mastermind.counter].config(text = text)
            Mastermind.label_feedback_list[Mastermind.counter].place(x = 320,
                                                                     y = creationOfCbanswer_list[Mastermind.counter])

            Mastermind.counter += 1
            if Mastermind.counter < 10:
                Mastermind.label_answer_cb_list[Mastermind.counter].config(relief = SUNKEN,
                                                                           background = "LightSteelBlue3")
                
            if Mastermind.counter == 10:
                self.guess_button['state'] = DISABLED
                Mastermind.endOfTheGameOutOfGuesses(self)
                
            elif Mastermind.feedback_list.count("Red") == 4:
                self.guess_button['state'] = DISABLED
                Mastermind.endOfGameWinner(self)



    def creationOfCbFeedback(self):
        self.label_feedback_head = Label(self, text = "Codebreaker's feedback.", font = ("Calibri", 13),
                                         background = "PeachPuff3")
        self.label_feedback_head.place(x = 300, y = 10)
        for __ in range(10):
            self.label_feedback = Label(self, text = str(__ + 1), font = ("Calibri", 12), background = "PeachPuff3")
            self.label_feedback.place(x = 300, y = creationOfCbanswer_list[__])
        
            
    def mainWindowCreationMenuBar(self):
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
        helpmenu.add_command(label = "Help Index", command = lambda:HelpAndAbout.helpIndex(self))
        helpmenu.add_command(label = "About...", command = lambda:HelpAndAbout.about(self))
        menubar.add_cascade(label = "Help", menu = helpmenu)

    
    def codeBreaker(self):
        Mastermind.guesses_list.clear()
        
        # textbox_1 ckeck
        users_input_1 = self.textbox_1.get()
        if users_input_1 in shorted_colors:
            if users_input_1 == "bl": Mastermind.guesses_list.append("Blue")
            elif users_input_1 == "ye": Mastermind.guesses_list.append("Yellow")   
            elif users_input_1 == "or": Mastermind.guesses_list.append("Orange")
            elif users_input_1 == "vl": Mastermind.guesses_list.append("Violet")
            elif users_input_1 == "gr": Mastermind.guesses_list.append("Green")
    
        # textbox_2 ckeck
        users_input_2 = self.textbox_2.get()
        if users_input_2 in shorted_colors:
            if users_input_2 == "bl": Mastermind.guesses_list.append("Blue")
            elif users_input_2 == "ye": Mastermind.guesses_list.append("Yellow")
            elif users_input_2 == "or": Mastermind.guesses_list.append("Orange")
            elif users_input_2 == "vl": Mastermind.guesses_list.append("Violet")
            elif users_input_2 == "gr": Mastermind.guesses_list.append("Green")

        users_input_3 = self.textbox_3.get()
        if users_input_3 in shorted_colors:
            if users_input_3 == "bl": Mastermind.guesses_list.append("Blue")
            elif users_input_3 == "ye": Mastermind.guesses_list.append("Yellow")   
            elif users_input_3 == "or": Mastermind.guesses_list.append("Orange")
            elif users_input_3 == "vl": Mastermind.guesses_list.append("Violet")
            elif users_input_3 == "gr": Mastermind.guesses_list.append("Green")
                    
        users_input_4 = self.textbox_4.get()
        if users_input_4 in shorted_colors:
            if users_input_4 == "bl": Mastermind.guesses_list.append("Blue")
            elif users_input_4 == "ye": Mastermind.guesses_list.append("Yellow")   
            elif users_input_4 == "or": Mastermind.guesses_list.append("Orange")
            elif users_input_4 == "vl": Mastermind.guesses_list.append("Violet")
            elif users_input_4 == "gr": Mastermind.guesses_list.append("Green")
                        
        return Mastermind.guesses_list 
        

    def printingcode(self, copiedguess, copiedlist):
        Mastermind.feedback_list.clear()
        guess = list(copiedguess)
        code = list(copiedlist)
        
        for num in range(len(guess)):
            if guess[num] == code[num]:
                guess[num] = 1
                code[num] = 2
                Mastermind.feedback_list.append("Red")

        for num in range(len(guess)):
            if guess[num] in code:
                Mastermind.feedback_list.append("White")
                
        return Mastermind.feedback_list


    def errorInputWarning(self):
        messagebox.showinfo(title = "Warning", message = "Wrong input...")
        
    def endOfTheGameOutOfGuesses(self):
        messagebox.showinfo(title = "Out of guesses!", message = "You lost try again...")
        Mastermind.destroy

    def userInputWarningWrongColor(self): 
        messagebox.showinfo(title = "Warning", message = "Wrong user's input")
        
    def endOfGameWinner(self):
        messagebox.showinfo(title = "Winner!", message = '''You win you are
the Codebraker''')


if __name__ == "__main__":
    
    FirstsSettingsWindow().mainloop()




    
