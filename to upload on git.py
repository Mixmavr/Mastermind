from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import Menu
from tkinter import messagebox
import random
from random import sample

##b = 'Blue'
##y = 'Yellow'
##o = 'Orange'
##g = 'Green'
##v = 'Violet'
##l = 'Lime'

pc_codebreaker_list = ['Blue', 'Yellow', 'Orange', 'Green']



class FirstsSettingsWindow(tk.Tk):

    def __init__(self):
        super().__init__()
        #super(FirstsSettingsWindow, self).__init__()
        self.selected_settings = [0, 0, 0, 0, 0]
    
        self.geometry("390x380")
        self.title("Mastermind Settings")

        



            # Creation of start button and label
        self.start_button = ttk.Button(self, text = "Start the game", command = self.opengamewindow)
        self.start_button.place(x = 30, y = 335)
        self.good_luck_label = ttk.Label(self, text = "and Good Luck !!!")
        self.good_luck_label.place(x = 118, y = 338)

        
            # Call of menubar in settings window
        self.settingsWindowCreationMenuBar()

            # Windows selections header
        self.general_header = ttk.Label(self, text = "Settings of the game.")
        self.general_header.place(x = 10, y = 10)
        self.general_header.config(font = ("Calibri", 15))

            # User's role in the game
        self.role_header = ttk.Label(self, text = '''1. Choose your role in the game write in the box
    'cb' for Codebreaker or 'cm' for Codemaker.''')
        self.role_header.place(x = 10, y = 50)
        self.role_textbox = ttk.Entry(self, width = 10)
        self.role_textbox.place(x = 330, y = 57)
        self.role_textbox.config(width = 5, font = ("Calibri", 12))

            # Total number of colors settings
        self.num_of_colors_header = ttk.Label(self, text = "2. Choose the number of colors in game, '5' or '6'.")
        self.num_of_colors_header.place(x = 10, y = 107)
        self.num_of_colors_textbox = ttk.Entry(self, width = 10)
        self.num_of_colors_textbox.place(x = 330, y = 105)
        self.num_of_colors_textbox.config(width = 5, font = ("Calibri", 12))


            # Code length settings
        self.code_length_header = ttk.Label(self, text = "3. Choose the code length, '3' or '4'.")
        self.code_length_header.place(x = 10, y = 157)
        self.code_length_textbox = ttk.Entry(self, width = 10)
        self.code_length_textbox.place(x = 330, y = 155)
        self.code_length_textbox.config(width = 5, font = ("Calibri", 12))


            # Duplication in random codemaker's code
        self.duplicate_colors_in_code_header = ttk.Label(self, text = "4. Choose duplicate colors in codemaker's code, 'y' or 'n'.")
        self.duplicate_colors_in_code_header.place(x = 10, y = 207)
        self.duplicate_colors_in_code_textbox = ttk.Entry(self, width = 10)
        self.duplicate_colors_in_code_textbox.place(x = 330, y = 205)
        self.duplicate_colors_in_code_textbox.config(width = 5, font = ("Calibri", 12))


            # Name of user player
        self.users_name_header = ttk.Label(self, text = "5. Insert your name.")
        self.users_name_header.place(x = 10, y = 257)
        self.users_name_textbox = ttk.Entry(self, width = 10)
        self.users_name_textbox.place(x = 290, y = 255)
        self.users_name_textbox.config(width = 10, font = ("Calibri", 12))    

        
        
    def opengamewindow(self):
        
        self.selected_number_of_colors = 0
        self.selected_code_length = 0
        self.selected_duplicate_colors = 0
        if self.role_textbox.get() in ["cm"]:
            self.selected_role = "cm"
            self.selected_settings[0] = self.selected_role
        elif self.role_textbox.get() in ["cb"]:
            self.selected_role = "cb"
            self.selected_settings[0] = self.selected_role
                
        if self.num_of_colors_textbox.get() in ["5"]:
            self.selected_number_of_colors = 5
            self.selected_settings[1] = self.selected_number_of_colors
        elif self.num_of_colors_textbox.get() in ["6"]:
            self.selected_number_of_colors = 6
            self.selected_settings[1] = self.selected_number_of_colors

        if self.code_length_textbox.get() in ["3"]:
            self.selected_code_length = 3
            self.selected_settings[2] = self.selected_code_length
                
        elif self.code_length_textbox.get() in ["4"]:
            self.selected_code_length = 4
            self.selected_settings[2] = self.selected_code_length

        if self.duplicate_colors_in_code_textbox.get() in ["y"]:
            self.selected_duplicate_colors = "True" # It means True
            self.selected_settings[3] = self.selected_duplicate_colors
        elif self.duplicate_colors_in_code_textbox.get() in ["n"]:
            self.selected_duplicate_colors = "False" # It means False
            self.selected_settings[3] = self.selected_duplicate_colors

        if len(self.users_name_textbox.get()) > 0:
            self.inserted_users_name = self.users_name_textbox.get()
            self.selected_settings[4] = self.inserted_users_name
            print("user's name :", self.selected_settings[4])
        elif not self.users_name_textbox.get():
            self.selected_settings[4] = 0
            
        #print("\n\t\tselected_settings", self.selected_settings)

        if 0 not in self.selected_settings:
            mastermind = Mastermind(users_role_in_game = self.selected_settings[0], number_of_colors = self.selected_settings[1],
                           code_length = self.selected_settings[2],
                        duplicate_colors_in_code = self.selected_settings[3], username = self.selected_settings[4])
            mastermind.grab_set()
        else:
            HelpAboutWarnings.errorInputWarning(self)


    def settingsWindowCreationMenuBar(self):
        menubar = Menu(self)
        self.config(menu = menubar)
        file_menu = Menu(menubar, tearoff = 0)

            # Creation of file menu
        menubar.add_cascade(label = "File", menu = file_menu)
        file_menu.add_command(label = "Exit", command = self.destroy)

            # Creation of help menu
        helpmenu = Menu(menubar, tearoff = 0)
        helpmenu.add_command(label = "Help Index", command = lambda:HelpAboutWarnings.helpIndex(self))
        helpmenu.add_command(label = "About...", command = lambda:HelpAboutWarnings.about(self))
        menubar.add_cascade(label = "Help", menu = helpmenu)
        




        
class HelpAboutWarnings():
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

    def errorInputWarning(self):
        messagebox.showinfo(title = "Warning", message = "Wrong input...")

        
    def endOfTheGameOutOfTries(self):
        messagebox.showinfo(title = "Out of guesses!", message = f'''You lost try again...
The code was:
{' '.join(Mastermind.color)}''')


    def userInputWarningWrongColor(self): 
        messagebox.showwarning(title = "Warning", message = "Wrong user's input")

        
    def endOfGameWinner(self):
        messagebox.showinfo(title = "Winner!", message = '''You win you are
the Codebraker''')

    def endOfGamePcWinner(self):
        messagebox.showinfo(title = "You lost!", message = "Pc is the codebreaker.")

    def endOfGameUserWinner(self):
        messagebox.showinfo(title = "Winner", message = "You are the codemaker and you won the pc!")

        

        
#class Mastermind(tk.Tk):
class Mastermind(tk.Toplevel):#, FirstsSettingsWindow):
    
    #counter = 0

    def __init__(self, users_role_in_game, number_of_colors, code_length, duplicate_colors_in_code, username):
        
        Mastermind.counter = 0
        
        self.users_role_in_game = users_role_in_game
        self.number_of_colors = number_of_colors
        self.code_length = code_length
        self.duplicate_colors_in_code = duplicate_colors_in_code
        self.username = username
        
        self.available_colors = ['Blue', 'Yellow', 'Orange', 'Green', 'Violet', 'Lime'][:self.number_of_colors]
        self.shorted_colors = ['b', 'y', 'o', 'g', 'v', 'l'][:self.number_of_colors]
        self.creationOfCbanswer_list = [410, 370, 330, 290, 250, 210, 170, 130, 90, 50]

        Mastermind.color = []

        self.guesses_list = []
        self.feedback_list = []
        self.label_answer_cb_list = []
        self.label_feedback_list = []
        self.user_codemaker_list = []
        self.user_cm_feedback_list = []

        super(Mastermind, self).__init__()
        #super(self).__init__()
        
           
            # menubar creation
        self.topWindowCreationMenuBar()
        
            # codebreaker's answer labels
        self.creationOfCbanswernumAndLabels()

            # codebreaker's answer feedback
        self.creationOfCbFeedback()



            # When User is Codebreaker.
        if self.users_role_in_game == "cb":
                # Creation of main window
            self.geometry("550x620")
            self.title('Mastermind game')
            self.configure(background = "PeachPuff3")

                # Creation of User - Codebrekaer's Guess button
            self.guess_button = ttk.Button(self, text = "Guess", command = lambda:self.commandOfGuessButton(creationofcode = self.creationOfCode))

                # Creation of PC - Codemaker's code.
            self.creationOfCode = self.creationOfCode(colors = self.available_colors, duplicate_colors_in_code
                                             = self.duplicate_colors_in_code)
            self.config(width = 8, height = 2)
            self.guess_button.place(x = 300, y = 480)

                # color table information
            self.label_info_head_upper = Label(self, text = "Color table info.", font = ("Calibri", 12),
                                         background = "PeachPuff3")
            self.label_info_head_upper.place(x = 8, y = 518)
            self.label_info_head_down = Label(self, text = "The available colors to choose are bellow:",
                                              font = ("Calibri", 12),
                                         background = "PeachPuff3")
            self.label_info_head_down.place(x = 8, y = 538)

            if self.number_of_colors == 5:
                self.label_info = Label(self, text = "b = Blue,  y = Yellow,  o = Orange,  g = Green,  v = Violet",
                                    font = ("Calibri", 12), background = "PeachPuff3")
                self.label_info.place(x = 8, y = 558)
            else:
                self.label_info = Label(self, text = "b = Blue,  y = Yellow,  o = Orange,  g = Green,  v = Violet, l = Lime",
                                    font = ("Calibri", 12), background = "PeachPuff3")
                self.label_info.place(x = 8, y = 558)


            self.role_in_game_info = Label(self, text = "{} is the 'Codebreaker' and pc is the 'Codemaker'.". format(self.username),
                                           font = ("Calibri", 12), background = "PeachPuff3", foreground='green')
            self.role_in_game_info.place(x = 8, y = 590)

            
                # Creation of textboxes
            if self.code_length == 3:
                self.label_cb_ins_box_head = Label(self, text = "Codebreaker's input.", font = ("Calibri", 13),
                                               background = "PeachPuff3")
                self.label_cb_ins_box_head.place(x = 30, y = 455)
                self.textbox_cb_1 = ttk.Entry(self)
                self.textbox_cb_1.place(x = 30, y = 480)
                self.textbox_cb_1.config(width = 5, font = ("Calibri", 12))
                #self.textbox_1.focus()

                self.textbox_cb_2 = ttk.Entry(self)
                self.textbox_cb_2.place(x = 80, y = 480)
                self.textbox_cb_2.config(width = 5, font = ("Calibri", 12))
                #self.textbox_2.focus()
            
                self.textbox_cb_3 = ttk.Entry(self)
                self.textbox_cb_3.place(x = 130, y = 480)
                self.textbox_cb_3.config(width = 5, font = ("Calibri", 12))
                #self.textbox_3.focus()


            else:
                self.label_cb_ins_box_head = Label(self, text = "Codebreaker's input.", font = ("Calibri", 13),
                                               background = "PeachPuff3")
                self.label_cb_ins_box_head.place(x = 30, y = 455)
                self.textbox_cb_1 = ttk.Entry(self)
                self.textbox_cb_1.place(x = 30, y = 480)
                self.textbox_cb_1.config(width = 5, font = ("Calibri", 12))
                #self.textbox_1.focus()

                self.textbox_cb_2 = ttk.Entry(self)
                self.textbox_cb_2.place(x = 80, y = 480)
                self.textbox_cb_2.config(width = 5, font = ("Calibri", 12))
                #self.textbox_2.focus()
            
                self.textbox_cb_3 = ttk.Entry(self)
                self.textbox_cb_3.place(x = 130, y = 480)
                self.textbox_cb_3.config(width = 5, font = ("Calibri", 12))
                self.textbox_cb_4 = ttk.Entry(self)
                self.textbox_cb_4.place(x = 180, y = 480)
                self.textbox_cb_4.config(width = 5, background = "SkyBlue3", font = ("Calibri", 12))



            # When User is Codemaker.
        elif self.users_role_in_game == "cm":

                # Creation of main window
            self.geometry("550x730")
            self.title('Mastermind game')
            self.configure(background = "PeachPuff3")

                # Creation of User - Codebrekaer's Guess button
            self.creation_code_button = ttk.Button(self, text = "Create the code",
                                                   command = lambda:self.creationUsersCmCodeButtonCommand())
            self.config(width = 8, height = 2)
            self.creation_code_button.place(x = 300, y = 480)

                # color table information
            self.label_info_head_upper = Label(self, text = "Color table info.", font = ("Calibri", 12),
                                         background = "PeachPuff3")
            self.label_info_head_upper.place(x = 8, y = 618)
            self.label_info_head_down = Label(self, text = "The available colors to choose are bellow:",
                                              font = ("Calibri", 12),
                                         background = "PeachPuff3")
            self.label_info_head_down.place(x = 8, y = 638)
            
            
            if self.number_of_colors == 5:
                self.label_info = Label(self, text = "b = Blue,  y = Yellow,  o = Orange,  g = Green,  v = Violet",
                                    font = ("Calibri", 12), background = "PeachPuff3")
                self.label_info.place(x = 8, y = 658)
            else:
                self.label_info = Label(self, text = "b = Blue,  y = Yellow,  o = Orange,  g = Green,  v = Violet, l = Lime",
                                    font = ("Calibri", 12), background = "PeachPuff3")
                self.label_info.place(x = 8, y = 658)
                

            self.label_feedback_info_header = Label(self, text = "The available feedback colors are: r = Red, w = White and empty textbox.",
                                                    font = ("Calibri", 12), background = "PeachPuff3")
            self.label_feedback_info_header.place(x = 8, y = 590)

            self.role_in_game_info = Label(self, text = "{} is the 'Codemaker' and pc is the 'Codebreaker'.". format(self.username),
                                           font = ("Calibri", 12), background = "PeachPuff3", foreground='green')
            self.role_in_game_info.place(x = 8, y = 690)
            

            if self.code_length == 3:
                self.label_cm_ins_box_head = Label(self, text = "Codemaker's input.", font = ("Calibri", 13),
                                               background = "PeachPuff3")
                self.label_cm_ins_box_head.place(x = 30, y = 455)
                self.textbox_cm_1 = ttk.Entry(self)
                self.textbox_cm_1.place(x = 30, y = 480)
                self.textbox_cm_1.config(width = 5, font = ("Calibri", 12))
                #self.textbox_1.focus()

                self.textbox_cm_2 = ttk.Entry(self)
                self.textbox_cm_2.place(x = 80, y = 480)
                self.textbox_cm_2.config(width = 5, font = ("Calibri", 12))
                #self.textbox_2.focus()
            
                self.textbox_cm_3 = ttk.Entry(self)
                self.textbox_cm_3.place(x = 130, y = 480)
                self.textbox_cm_3.config(width = 5, font = ("Calibri", 12))


                # Creation of user's feedback entry boxes
                self.textbox_cm_feedback_1 = ttk.Entry(self)
                self.textbox_cm_feedback_1.place(x = 30, y = 550)
                self.textbox_cm_feedback_1.config(width = 5, font = ("Calibri", 12), state= "disabled")

                self.textbox_cm_feedback_2 = ttk.Entry(self)
                self.textbox_cm_feedback_2.place(x = 80, y = 550)
                self.textbox_cm_feedback_2.config(width = 5, font = ("Calibri", 12), state= "disabled")

                self.textbox_cm_feedback_3 = ttk.Entry(self)
                self.textbox_cm_feedback_3.place(x = 130, y = 550)
                self.textbox_cm_feedback_3.config(width = 5, font = ("Calibri", 12), state= "disabled")

                

            else:
                self.label_cm_ins_box_head = Label(self, text = "Codemaker's input.", font = ("Calibri", 13),
                                               background = "PeachPuff3")
                self.label_cm_ins_box_head.place(x = 30, y = 455)
                self.textbox_cm_1 = ttk.Entry(self)
                self.textbox_cm_1.place(x = 30, y = 480)
                self.textbox_cm_1.config(width = 5, font = ("Calibri", 12))
                #self.textbox_1.focus()

                self.textbox_cm_2 = ttk.Entry(self)
                self.textbox_cm_2.place(x = 80, y = 480)
                self.textbox_cm_2.config(width = 5, font = ("Calibri", 12))
                #self.textbox_2.focus()
            
                self.textbox_cm_3 = ttk.Entry(self)
                self.textbox_cm_3.place(x = 130, y = 480)
                self.textbox_cm_3.config(width = 5, font = ("Calibri", 12))
                self.textbox_cm_4 = ttk.Entry(self)
                self.textbox_cm_4.place(x = 180, y = 480)
                self.textbox_cm_4.config(width = 5, background = "SkyBlue3", font = ("Calibri", 12))
                #self.textbox_4.focus()
                print("User is codemaker")

                # Creation of user's feedback entry boxes
                self.textbox_cm_feedback_1 = ttk.Entry(self)
                self.textbox_cm_feedback_1.place(x = 30, y = 550)
                self.textbox_cm_feedback_1.config(width = 5, font = ("Calibri", 12), state= "disabled")

                self.textbox_cm_feedback_2 = ttk.Entry(self)
                self.textbox_cm_feedback_2.place(x = 80, y = 550)
                self.textbox_cm_feedback_2.config(width = 5, font = ("Calibri", 12), state= "disabled")

                self.textbox_cm_feedback_3 = ttk.Entry(self)
                self.textbox_cm_feedback_3.place(x = 130, y = 550)
                self.textbox_cm_feedback_3.config(width = 5, font = ("Calibri", 12), state= "disabled")

                self.textbox_cm_feedback_4 = ttk.Entry(self)
                self.textbox_cm_feedback_4.place(x = 180, y = 550)
                self.textbox_cm_feedback_4.config(width = 5, font = ("Calibri", 12), state= "disabled")

                

            self.label_cm_ins_box_header = Label(self, text = "Codemaker's feedback input boxes.", font = ("Calibri", 13),
                                               background = "PeachPuff3")
            self.label_cm_ins_box_header.place(x = 30, y = 525)

            self.next_move_button = Button(self, text = "Give feedback", command = lambda:
                                           self.answerAndFeedbackCbLabels(text = self.codemaker(), code = pc_codebreaker_list))
            self.next_move_button.place(x = 300, y = 550)
            self.next_move_button.config(width = 14, height = 1)
            self.next_move_button['state'] = DISABLED
        
        
            


    def creationUsersCmCodeButtonCommand(self):
        self.user_codemaker_list.clear()
        if self.code_length == 3:
                # textbox_1 check
            users_cm_input_1 = self.textbox_cm_1.get()
            #print(users_cm_input_1)
            if users_cm_input_1 in self.shorted_colors:
                if users_cm_input_1 == "b": self.user_codemaker_list.append("Blue")
                elif users_cm_input_1 == "y": self.user_codemaker_list.append("Yellow")   
                elif users_cm_input_1 == "o": self.user_codemaker_list.append("Orange")
                elif users_cm_input_1 == "v": self.user_codemaker_list.append("Violet")
                elif users_cm_input_1 == "g": self.user_codemaker_list.append("Green")
                elif users_cm_input_1 == "l": self.user_codemaker_list.append("Lime")
    
                # textbox_2 check
            users_cm_input_2 = self.textbox_cm_2.get()
            if users_cm_input_2 in self.shorted_colors:
                if users_cm_input_2 == "b": self.user_codemaker_list.append("Blue")
                elif users_cm_input_2 == "y": self.user_codemaker_list.append("Yellow")
                elif users_cm_input_2 == "o": self.user_codemaker_list.append("Orange")
                elif users_cm_input_2 == "v": self.user_codemaker_list.append("Violet")
                elif users_cm_input_2 == "g": self.user_codemaker_list.append("Green")
                elif users_cm_input_2 == "l": self.user_codemaker_list.append("Lime")

                # textbox_3 check
            users_cm_input_3 = self.textbox_cm_3.get()
            if users_cm_input_3 in self.shorted_colors:
                if users_cm_input_3 == "b": self.user_codemaker_list.append("Blue")
                elif users_cm_input_3 == "y": self.user_codemaker_list.append("Yellow")   
                elif users_cm_input_3 == "o": self.user_codemaker_list.append("Orange")
                elif users_cm_input_3 == "v": self.user_codemaker_list.append("Violet")
                elif users_cm_input_3 == "g": self.user_codemaker_list.append("Green")
                elif users_cm_input_3 == "l": self.user_codemaker_list.append("Lime")
            

            if self.validationOfInput(returnablevalue = self.user_codemaker_list) == 1:
                self.creation_code_button.destroy()
                self.textbox_cm_1.destroy()
                self.textbox_cm_2.destroy()
                self.textbox_cm_3.destroy()
                self.users_cm_code_label = ttk.Label(self, text = self.user_codemaker_list, font = ("Calibri", 13), width = 22,
                                                     relief = SUNKEN, background = "cyan")
                self.users_cm_code_label.place(x = 30, y = 480)
                self.textbox_cm_feedback_1.config(state = "enabled")
                self.textbox_cm_feedback_2.config(state = "enabled")
                self.textbox_cm_feedback_3.config(state = "enabled")
                self.next_move_button['state'] = NORMAL
                
                self.answerAndFeedbackCbLabels(text = "", code = pc_codebreaker_list)

                return self.user_codemaker_list

            else:
                HelpAboutWarnings.errorInputWarning(self)
                


        else:
                # textbox_cm_1 
            users_cm_input_1 = self.textbox_cm_1.get()
            if users_cm_input_1 in self.shorted_colors:
                if users_cm_input_1 == "b": self.user_codemaker_list.append("Blue")
                elif users_cm_input_1 == "y": self.user_codemaker_list.append("Yellow")   
                elif users_cm_input_1 == "o": self.user_codemaker_list.append("Orange")
                elif users_cm_input_1 == "v": self.user_codemaker_list.append("Violet")
                elif users_cm_input_1 == "g": self.user_codemaker_list.append("Green")
                elif users_cm_input_1 == "l": self.user_codemaker_list.append("Lime")
    
                # textbox_cm_2 
            users_cm_input_2 = self.textbox_cm_2.get()
            if users_cm_input_2 in self.shorted_colors:
                if users_cm_input_2 == "b": self.user_codemaker_list.append("Blue")
                elif users_cm_input_2 == "y": self.user_codemaker_list.append("Yellow")
                elif users_cm_input_2 == "o": self.user_codemaker_list.append("Orange")
                elif users_cm_input_2 == "v": self.user_codemaker_list.append("Violet")
                elif users_cm_input_2 == "g": self.user_codemaker_list.append("Green")
                elif users_cm_input_2 == "l": self.user_codemaker_list.append("Lime")

                # textbox_cm_3 
            users_cm_input_3 = self.textbox_cm_3.get()
            if users_cm_input_3 in self.shorted_colors:
                if users_cm_input_3 == "b": self.user_codemaker_list.append("Blue")
                elif users_cm_input_3 == "y": self.user_codemaker_list.append("Yellow")   
                elif users_cm_input_3 == "o": self.user_codemaker_list.append("Orange")
                elif users_cm_input_3 == "v": self.user_codemaker_list.append("Violet")
                elif users_cm_input_3 == "g": self.user_codemaker_list.append("Green")
                elif users_cm_input_3 == "l": self.user_codemaker_list.append("Lime")
                # textbox_cm_4 
            users_cm_input_4 = self.textbox_cm_4.get()
            if users_cm_input_4 in self.shorted_colors:
                if users_cm_input_4 == "b": self.user_codemaker_list.append("Blue")
                elif users_cm_input_4 == "y": self.user_codemaker_list.append("Yellow")   
                elif users_cm_input_4 == "o": self.user_codemaker_list.append("Orange")
                elif users_cm_input_4 == "v": self.user_codemaker_list.append("Violet")
                elif users_cm_input_4 == "g": self.user_codemaker_list.append("Green")
                elif users_cm_input_4 == "l": self.user_codemaker_list.append("Lime")

            

            if self.validationOfInput(returnablevalue = self.user_codemaker_list) == 1:
                self.creation_code_button.destroy()
                self.textbox_cm_1.destroy()
                self.textbox_cm_2.destroy()
                self.textbox_cm_3.destroy()
                self.textbox_cm_4.destroy()
                self.users_cm_code_label = ttk.Label(self, text = self.user_codemaker_list, font = ("Calibri", 13), width = 22,
                                                         relief = SUNKEN, background = "cyan")
                self.users_cm_code_label.place(x = 30, y = 480)
                self.textbox_cm_feedback_1.config(state = "enabled")
                self.textbox_cm_feedback_2.config(state = "enabled")
                self.textbox_cm_feedback_3.config(state = "enabled")
                self.textbox_cm_feedback_4.config(state = "enabled")
                self.next_move_button['state'] = NORMAL

                self.answerAndFeedbackCbLabels(text = "", code = pc_codebreaker_list)

                return self.user_codemaker_list

            else:HelpAboutWarnings.errorInputWarning(self)
                
       
    def codemaker(self):
        self.user_cm_feedback_list.clear()
        
        if self.code_length == 3:
            
                # textbox_1 check
            users_cm_feed_input_1 = self.textbox_cm_feedback_1.get()
            if users_cm_feed_input_1 in ["r", "w", ""]:
                if users_cm_feed_input_1 == "r": self.user_cm_feedback_list.append("Red")
                elif users_cm_feed_input_1 == "w": self.user_cm_feedback_list.append("White")
                elif users_cm_feed_input_1 == "": self.user_cm_feedback_list.append("  ")
    
                # textbox_2 check
            users_cm_feed_input_2 = self.textbox_cm_feedback_2.get()
            if users_cm_feed_input_2 in ["r", "w", ""]:
                if users_cm_feed_input_2 == "r": self.user_cm_feedback_list.append("Red")
                elif users_cm_feed_input_2 == "w": self.user_cm_feedback_list.append("White")
                elif users_cm_feed_input_2 == "": self.user_cm_feedback_list.append("  ")

                # textbox_3 check
            users_cm_feed_input_3 = self.textbox_cm_feedback_3.get()
            if users_cm_feed_input_3 in ["r", "w", ""]:
                if users_cm_feed_input_3 == "r": self.user_cm_feedback_list.append("Red")
                elif users_cm_feed_input_3 == "w": self.user_cm_feedback_list.append("White")
                elif users_cm_feed_input_3 == "": self.user_cm_feedback_list.append("  ")

        
            if self.validationOfInput(returnablevalue = self.user_cm_feedback_list) == 1:
                return self.user_cm_feedback_list
            else:
                HelpAboutWarnings.errorInputWarning(self)


        else:
                # textbox_1 check
            users_cm_feed_input_1 = self.textbox_cm_feedback_1.get()
            if users_cm_feed_input_1 in ["r", "w", ""]:
                if users_cm_feed_input_1 == "r": self.user_cm_feedback_list.append("Red")
                elif users_cm_feed_input_1 == "w": self.user_cm_feedback_list.append("White")
                elif users_cm_feed_input_1 == "": self.user_cm_feedback_list.append("  ")
    
                # textbox_2 check
            users_cm_feed_input_2 = self.textbox_cm_feedback_2.get()
            if users_cm_feed_input_2 in ["r", "w", ""]:
                if users_cm_feed_input_2 == "r": self.user_cm_feedback_list.append("Red")
                elif users_cm_feed_input_2 == "w": self.user_cm_feedback_list.append("White")
                elif users_cm_feed_input_2 == "": self.user_cm_feedback_list.append("  ")

                # textbox_3 check
            users_cm_feed_input_3 = self.textbox_cm_feedback_3.get()
            if users_cm_feed_input_3 in ["r", "w", ""]:
                if users_cm_feed_input_3 == "r": self.user_cm_feedback_list.append("Red")
                elif users_cm_feed_input_3 == "w": self.user_cm_feedback_list.append("White")
                elif users_cm_feed_input_3 == "": self.user_cm_feedback_list.append("  ")

                # textbox_4 check
            users_cm_feed_input_4 = self.textbox_cm_feedback_4.get()
            if users_cm_feed_input_4 in ["r", "w", ""]:
                if users_cm_feed_input_4 == "r": self.user_cm_feedback_list.append("Red")
                elif users_cm_feed_input_4 == "w": self.user_cm_feedback_list.append("White")
                elif users_cm_feed_input_4 == "": self.user_cm_feedback_list.append("  ")


            print("self.user_cm_feedback_list :", self.user_cm_feedback_list)


            if self.validationOfInput(returnablevalue = self.user_cm_feedback_list) == 1:
                return self.user_cm_feedback_list
            else:
                HelpAboutWarnings.errorInputWarning(self)
            


    def newGameMenuButton(self):
        self.destroy()
        Mastermind(self.users_role_in_game, self.number_of_colors, self.code_length, self.duplicate_colors_in_code, self.username)
        

    def commandOfGuessButton(self, creationofcode):
        codebreaker = self.codeBreaker()
            
        if self.validationOfInput(returnablevalue = codebreaker) == 1:
            printingcode = self.printingcode(copiedguess = codebreaker, copiedlist = creationofcode)
            answerandfeedbackcblabels = self.answerAndFeedbackCbLabels(text = printingcode,
                                                                           code = codebreaker)
        else:
            HelpAboutWarnings.errorInputWarning(self)


        
    def validationOfInput(self, returnablevalue):        
        returnablevalue = list(returnablevalue)
        if len(returnablevalue) != self.code_length:
            return 2 # It means False
        elif len(returnablevalue) == self.code_length:
            return 1 # It means True




    def creationOfCode(self, colors, duplicate_colors_in_code):
        available_colors_list = list(colors)
        print("available_colors_list", available_colors_list)
        if len(Mastermind.color) == self.code_length:
            return Mastermind.color

        if duplicate_colors_in_code == "False":
            Mastermind.color = random.sample(available_colors_list, k = self.code_length)
            return Mastermind.color
        
        elif duplicate_colors_in_code == "True":
            Mastermind.color = random.choices(available_colors_list, k = self.code_length)
            print("with duplicate colors :", Mastermind.color)
            return Mastermind.color

       
    def creationOfCbanswernumAndLabels(self):
        self.label_head_cb = Label(self, text = "Codebreaker's answers.", font = ("Calibri", 13),
                                   background = "PeachPuff3")
        self.label_head_cb.place(x = 8, y = 10)
        for _ in range(10):
            self.label_cb = Label(self, text = str(_ + 1), font = ("Calibri", 12), background = "PeachPuff3")
            self.label_cb.place(x = 8, y = self.creationOfCbanswer_list[_])
            self.label_feedback_list.append(Label(self, background = "NavajoWhite2",
                                                        font = ("Calibri", 12), width = 24))
            self.label_feedback_list[_].place(x = 320, y = self.creationOfCbanswer_list[_])

            self.label_answer_cb_list.append(Label(self, background = "light grey",
                                                         font = ("Calibri", 12), width = 24))
            self.label_answer_cb_list[_].place(x = 30, y = self.creationOfCbanswer_list[_])

        if self.users_role_in_game == "cb":
            self.label_feedback_list[Mastermind.counter].config(relief = SUNKEN)  
            self.label_answer_cb_list[0].config(relief = SUNKEN, background = "LightSteelBlue3")
            
        elif self.users_role_in_game == "cm":
            self.label_answer_cb_list[0].config(relief = SUNKEN, background = "LightSteelBlue3")            



    def answerAndFeedbackCbLabels(self, text, code):
        text = list(text)
            
        code = list(code)
        
        self.label_answer_cb_list[Mastermind.counter].config(background = "LightSteelBlue3")
        self.label_answer_cb_list[Mastermind.counter].config(text = " ".join(code))
        self.label_answer_cb_list[Mastermind.counter].place(x = 30,
                                                                      y = self.creationOfCbanswer_list[Mastermind.counter])
        if self.users_role_in_game == "cm":
            if Mastermind.counter >= 1:
                    
                print("counter :", Mastermind.counter)
                self.label_feedback_list[Mastermind.counter - 1].config(text = " ".join(text))
                self.label_feedback_list[Mastermind.counter - 1].place(x = 320,
                                                                    y = self.creationOfCbanswer_list[Mastermind.counter - 1])
                #self.label_feedback_list[Mastermind.counter].config(relief = SUNKEN)
                    
        elif self.users_role_in_game == "cb":
            self.label_feedback_list[Mastermind.counter].config(text = " ".join(text))
            self.label_feedback_list[Mastermind.counter].place(x = 320,
                                                                    y = self.creationOfCbanswer_list[Mastermind.counter])
            #self.label_feedback_list[Mastermind.counter].config(relief = SUNKEN)

        Mastermind.counter += 1
        print("Mastermind.counter", Mastermind.counter)
        if Mastermind.counter < 10:
            self.label_answer_cb_list[Mastermind.counter].config(relief = SUNKEN,
                                                                        background = "LightSteelBlue3")
                
        if self.users_role_in_game == "cm":
            if self.user_cm_feedback_list.count("Red") == self.code_length:
                self.next_move_button['state'] = DISABLED
                HelpAboutWarnings.endOfGamePcWinner(self)

        else:
            if self.feedback_list.count("Red") == self.code_length:
                self.guess_button['state'] = DISABLED
                HelpAboutWarnings.endOfGameWinner(self)

                
        if Mastermind.counter == 10:       
            if self.users_role_in_game == "cb":
                self.guess_button['state'] = DISABLED
                HelpAboutWarnings.endOfTheGameOutOfTries(self)

            else:
                self.next_move_button['state'] = DISABLED
                HelpAboutWarnings.endOfGameUserWinner(self)
              

        
    def creationOfCbFeedback(self):
        self.label_feedback_head = Label(self, text = "Codebreaker's feedback.", font = ("Calibri", 13),
                                         background = "PeachPuff3")
        self.label_feedback_head.place(x = 300, y = 10)
        for __ in range(10):
            self.label_feedback = Label(self, text = str(__ + 1), font = ("Calibri", 12), background = "PeachPuff3")
            self.label_feedback.place(x = 300, y = self.creationOfCbanswer_list[__])
        
            
            
    def topWindowCreationMenuBar(self):
        menubar = Menu(self)
        self.config(menu = menubar)
        file_menu = Menu(menubar, tearoff = 0)

            # Creation of file menu
        menubar.add_cascade(label = "File", menu = file_menu)
        file_menu.add_command(label = "New", command = self.newGameMenuButton)
        file_menu.add_separator()
        file_menu.add_command(label = "Exit", command = self.destroy)

            # Creation of help menu
        helpmenu = Menu(menubar, tearoff = 0)
        helpmenu.add_command(label = "Help Index", command = lambda:HelpAboutWarnings.helpIndex(self))
        helpmenu.add_command(label = "About...", command = lambda:HelpAboutWarnings.about(self))
        menubar.add_cascade(label = "Help", menu = helpmenu)

    

    def codeBreaker(self):
        self.guesses_list.clear()        
        
        if self.code_length == 3:
            
                # textbox_1 check
            users_input_1 = self.textbox_cb_1.get()
            if users_input_1 in self.shorted_colors:
                if users_input_1 == "b": self.guesses_list.append("Blue")
                elif users_input_1 == "y": self.guesses_list.append("Yellow")   
                elif users_input_1 == "o": self.guesses_list.append("Orange")
                elif users_input_1 == "v": self.guesses_list.append("Violet")
                elif users_input_1 == "g": self.guesses_list.append("Green")
                elif users_input_1 == "l": self.guesses_list.append("Lime")
    
                # textbox_2 check
            users_input_2 = self.textbox_cb_2.get()
            if users_input_2 in self.shorted_colors:
                if users_input_2 == "b": self.guesses_list.append("Blue")
                elif users_input_2 == "y": self.guesses_list.append("Yellow")
                elif users_input_2 == "o": self.guesses_list.append("Orange")
                elif users_input_2 == "v": self.guesses_list.append("Violet")
                elif users_input_2 == "g": self.guesses_list.append("Green")
                elif users_input_2 == "l": self.guesses_list.append("Lime")

                # textbox_3 check
            users_input_3 = self.textbox_cb_3.get()
            if users_input_3 in self.shorted_colors:
                if users_input_3 == "b": self.guesses_list.append("Blue")
                elif users_input_3 == "y": self.guesses_list.append("Yellow")   
                elif users_input_3 == "o": self.guesses_list.append("Orange")
                elif users_input_3 == "v": self.guesses_list.append("Violet")
                elif users_input_3 == "g": self.guesses_list.append("Green")
                elif users_input_3 == "l": self.guesses_list.append("Lime")
            return self.guesses_list



        else:
                # textbox_1 check
            users_input_1 = self.textbox_cb_1.get()
            if users_input_1 in self.shorted_colors:
                if users_input_1 == "b": self.guesses_list.append("Blue")
                elif users_input_1 == "y": self.guesses_list.append("Yellow")   
                elif users_input_1 == "o": self.guesses_list.append("Orange")
                elif users_input_1 == "v": self.guesses_list.append("Violet")
                elif users_input_1 == "g": self.guesses_list.append("Green")
                elif users_input_1 == "l": self.guesses_list.append("Lime")
    
                # textbox_2 check
            users_input_2 = self.textbox_cb_2.get()
            if users_input_2 in self.shorted_colors:
                if users_input_2 == "b": self.guesses_list.append("Blue")
                elif users_input_2 == "y": self.guesses_list.append("Yellow")
                elif users_input_2 == "o": self.guesses_list.append("Orange")
                elif users_input_2 == "v": self.guesses_list.append("Violet")
                elif users_input_2 == "g": self.guesses_list.append("Green")
                elif users_input_2 == "l": self.guesses_list.append("Lime")

                # textbox_3 check
            users_input_3 = self.textbox_cb_3.get()
            if users_input_3 in self.shorted_colors:
                if users_input_3 == "b": self.guesses_list.append("Blue")
                elif users_input_3 == "y": self.guesses_list.append("Yellow")   
                elif users_input_3 == "o": self.guesses_list.append("Orange")
                elif users_input_3 == "v": self.guesses_list.append("Violet")
                elif users_input_3 == "g": self.guesses_list.append("Green")
                elif users_input_3 == "l": self.guesses_list.append("Lime")
                # textbox_4 check
            users_input_4 = self.textbox_cb_4.get()
            if users_input_4 in self.shorted_colors:
                if users_input_4 == "b": self.guesses_list.append("Blue")
                elif users_input_4 == "y": self.guesses_list.append("Yellow")   
                elif users_input_4 == "o": self.guesses_list.append("Orange")
                elif users_input_4 == "v": self.guesses_list.append("Violet")
                elif users_input_4 == "g": self.guesses_list.append("Green")
                elif users_input_4 == "l": self.guesses_list.append("Lime")  
            return self.guesses_list 

        

    def printingcode(self, copiedguess, copiedlist):
        
        self.feedback_list.clear()
        guess = list(copiedguess)
        code = list(copiedlist)

        for num in range(len(guess)):
            if guess[num] == code[num]:
                guess[num] = 1
                code[num] = 2
                self.feedback_list.append("Red")

        for num in range(len(guess)):
            if guess[num] in code:
                self.feedback_list.append("White")

        return self.feedback_list
        
    
        
if __name__ == "__main__":

    FirstsSettingsWindow().mainloop()


    
