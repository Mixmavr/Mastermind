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
##p = 'Pink'
#available_colors = ['Blue', 'Yellow', 'Orange', 'Green', 'Violet', 'Pink']
#shorted_colors = ['b', 'y', 'o', 'v', 'g', 'p']


#duplicate_colors_in_code = True
#duplicate_colors_in_code = False

#code_length = 4

creationOfCbanswer_list = [410, 370, 330, 290, 250, 210, 170, 130, 90, 50]


##def mainmenu():
##    mastermind = Mastermind()
##    mastermindscode = MastermindsCode()
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

##class MainControler():
##    def __init__(self):
##        self.run()
##        
##    
##    def run(self):
##        #generalselections = Generalselections()
##        #mastermind = Mastermind()
##        #m_1 = MastermindsCode()
##        #mastermind = Mastermind()
##        
##        #m_1 = MastermindsCode()
##        #mastermind.mainloop()
##        pass



       
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


##class FirstsSettingsWindow(tk.Tk):
##    def __init__(self):
##        super().__init__()


FirstsSettingsWindow = tk.Tk()

FirstsSettingsWindow.geometry("390x380")
FirstsSettingsWindow.title("Mastermind Settings")

##        # Call of radio buttons method
##        self.creationOfRadioButtons()

        # Creation of start button and label
start_button = ttk.Button(FirstsSettingsWindow, text = "Start the game", command = lambda:opengamewindow())
start_button.place(x = 30, y = 335)
good_luck_label = ttk.Label(FirstsSettingsWindow, text = "and Good Luck !!!")
good_luck_label.place(x = 118, y = 338)

    
        # Call of menubar in settings window
#settingsWindowCreationMenuBar()

        # Windows selections header
general_header = ttk.Label(FirstsSettingsWindow, text = "First settings of the game.")
general_header.place(x = 10, y = 10)
general_header.config(font = ("Calibri", 15))

        # User's role in the game
role_header = ttk.Label(FirstsSettingsWindow, text = '''1. Choose your role in the game write in the box
    'cb' for Codebreaker or 'cm' for Codemaker.''')
role_header.place(x = 10, y = 50)
role_textbox = ttk.Entry(FirstsSettingsWindow, width = 10)
role_textbox.place(x = 330, y = 57)
role_textbox.config(width = 5, font = ("Calibri", 12))

        # Total number of colors settings
num_of_colors_header = ttk.Label(FirstsSettingsWindow, text = "2. Choose the number of colors in game, '5' or '6'.")
num_of_colors_header.place(x = 10, y = 107)
num_of_colors_textbox = ttk.Entry(FirstsSettingsWindow, width = 10)
num_of_colors_textbox.place(x = 330, y = 105)
num_of_colors_textbox.config(width = 5, font = ("Calibri", 12))


        # Code length settings
code_length_header = ttk.Label(FirstsSettingsWindow, text = "3. Choose the code length, '3' or '4'.")
code_length_header.place(x = 10, y = 157)
code_length_textbox = ttk.Entry(FirstsSettingsWindow, width = 10)
code_length_textbox.place(x = 330, y = 155)
code_length_textbox.config(width = 5, font = ("Calibri", 12))


        # Duplication in random codemaker's code
duplicate_colors_in_code_header = ttk.Label(FirstsSettingsWindow, text = "4. Choose duplicated colors in codemaker's code, 'y' or 'n'.")
duplicate_colors_in_code_header.place(x = 10, y = 207)
duplicate_colors_in_code_textbox = ttk.Entry(FirstsSettingsWindow, width = 10)
duplicate_colors_in_code_textbox.place(x = 330, y = 205)
duplicate_colors_in_code_textbox.config(width = 5, font = ("Calibri", 12))


        # Name of user player
users_name_header = ttk.Label(FirstsSettingsWindow, text = "5. Insert your name.")
users_name_header.place(x = 10, y = 257)
users_name_textbox = ttk.Entry(FirstsSettingsWindow, width = 10)
users_name_textbox.place(x = 290, y = 255)
users_name_textbox.config(width = 10, font = ("Calibri", 12))    

    
    
def opengamewindow():
    #entered_value = int(settings_textbox.get())
    #print(entered_value)
    #print(type(entered_value))
    #entered_value = int(settings_textbox.get())
    #passtheentryvalue = passtheentryvalue(entryvalue = settings_textbox)
    #passtheentryvalue = 
    
    selected_settings = [0, 0, 0, 0, 0]
    selected_number_of_colors = 0
    selected_code_length = 0
    selected_duplicate_colors = 0
    #print("1", type(selected_number_of_colors))
    if role_textbox.get() in ["cm"]:
        selected_role = "cm"
        selected_settings[0] = selected_role
    elif role_textbox.get() in ["cb"]:
        selected_role = "cb"
        selected_settings[0] = selected_role
        
    if num_of_colors_textbox.get() in ["5"]:
        #a = int(settings_textbox)
        selected_number_of_colors = 5
        selected_settings[1] = selected_number_of_colors
        #print("2", type(selected_number_of_colors))
        #mastermind = Mastermind(number_of_colors = selected_number_of_colors)
    elif num_of_colors_textbox.get() in ["6"]:
        #a = int(settings_textbox)
        selected_number_of_colors = 6
        selected_settings[1] = selected_number_of_colors
        #print("3", type(selected_number_of_colors))
        #mastermind = Mastermind(number_of_colors = selected_number_of_colors)

    if code_length_textbox.get() in ["3"]:
        selected_code_length = 3
        selected_settings[2] = selected_code_length
        
    elif code_length_textbox.get() in ["4"]:
        selected_code_length = 4
        selected_settings[2] = selected_code_length

    if duplicate_colors_in_code_textbox.get() in ["y"]:
        selected_duplicate_colors = "True" # It means True
        selected_settings[3] = selected_duplicate_colors
    elif duplicate_colors_in_code_textbox.get() in ["n"]:
        selected_duplicate_colors = "False" # It means False
        selected_settings[3] = selected_duplicate_colors

    if len(users_name_textbox.get()) > 0:
        inserted_users_name = users_name_textbox.get()
        selected_settings[4] = inserted_users_name
        print("user's name :", selected_settings[4])
    elif not users_name_textbox.get():
        selected_settings[4] = 0
    
    print("\n\t\tselected_settings", selected_settings)

    if 0 not in selected_settings:
        #mastermind = Mastermind(number_of_colors = selected_settings[0], code_length = selected_settings[1])
        mastermind = Mastermind(users_role_in_game = selected_settings[0], number_of_colors = selected_settings[1],
                   code_length = selected_settings[2],
                   duplicate_colors_in_code = selected_settings[3])
        mastermind.grab_set()
    else:print("Error Input")
    #else: Mastermind.errorInputWarning
        #mastermind = Mastermind()




        
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

        

        
#class Mastermind(tk.Tk):
class Mastermind(tk.Toplevel):#, FirstsSettingsWindow):

    #firstssettingswindow = FirstsSettingsWindow()
    #mastermindscode = MastermindsCode()

    #counter = 0
    def __init__(self, users_role_in_game, number_of_colors, code_length, duplicate_colors_in_code):#passtheentryvalue):#convert_to_int()):#5):#number_of_colors = firstssettingswindow.settings_textbox.get()
        # Creation of necessary lists
        #print(type(number_of_colors))
        Mastermind.counter = 0
        
        self.users_role_in_game = users_role_in_game
        print("self.users_role_in_game", self.users_role_in_game)
        self.number_of_colors = number_of_colors
        self.code_length = code_length
        self.duplicate_colors_in_code = duplicate_colors_in_code
        
        self.available_colors = ['Blue', 'Yellow', 'Orange', 'Green', 'Violet', 'Lime'][:self.number_of_colors]
        self.shorted_colors = ['b', 'y', 'o', 'g', 'v', 'l'][:self.number_of_colors]
        Mastermind.color = []
        Mastermind.guesses_list = []
        Mastermind.feedback_list = []
        Mastermind.label_answer_cb_list = []
        Mastermind.label_feedback_list = []
        Mastermind.user_codemaker_list = []

        super(Mastermind, self).__init__()

        
##        # Creation of main window
##        self.geometry("550x590")
##        self.title('Mastermind game')
##        self.configure(background = "PeachPuff3")


##        # color table information
##        self.label_info_head_upper = Label(self, text = "Color table info.", font = ("Calibri", 12),
##                                     background = "PeachPuff3")
##        self.label_info_head_upper.place(x = 8, y = 518)
##        self.label_info_head_down = Label(self, text = "The available colors to choose are bellow:",
##                                          font = ("Calibri", 12),
##                                     background = "PeachPuff3")
##        self.label_info_head_down.place(x = 8, y = 538)
##
##        if self.number_of_colors == 5:
##            self.label_info = Label(self, text = "b = Blue,  y = Yellow,  o = Orange,  g = Green,  v = Violet",
##                                font = ("Calibri", 12), background = "PeachPuff3")
##            self.label_info.place(x = 8, y = 558)
##        else:
##            self.label_info = Label(self, text = "b = Blue,  y = Yellow,  o = Orange,  g = Green,  v = Violet, l = Lime",
##                                font = ("Calibri", 12), background = "PeachPuff3")
##            self.label_info.place(x = 8, y = 558)
           
        # menubar creation
        self.mainWindowCreationMenuBar()
        
        # codebreaker's answer labels
        self.creationOfCbanswernumAndLabels()

        # codebreaker's answer feedback
        self.creationOfCbFeedback()



        # When User is Codebreaker.
        if self.users_role_in_game == "cb":
            # Creation of main window
            self.geometry("550x590")
            self.title('Mastermind game')
            self.configure(background = "PeachPuff3")

            # Creation of User - Codebrekaer's Guess button
            self.guess_button = ttk.Button(self, text = "Guess", command = lambda:self.comandOfGuessButton(creationofcode = self.creationOfCode))

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

            
            # Creation of textboxes
            if self.code_length == 3:
                self.label_cb_ins_box_head = Label(self, text = "Codebreaker's input.", font = ("Calibri", 13),
                                               background = "PeachPuff3")
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


            else:
                self.label_cb_ins_box_head = Label(self, text = "Codebreaker's input.", font = ("Calibri", 13),
                                               background = "PeachPuff3")
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
                self.textbox_4 = ttk.Entry(self)
                self.textbox_4.place(x = 180, y = 480)
                self.textbox_4.config(width = 5, background = "SkyBlue3", font = ("Calibri", 12))



        # When User is Codemaker.
        elif self.users_role_in_game == "cm":

            # Creation of main window
            self.geometry("550x700")
            self.title('Mastermind game')
            self.configure(background = "PeachPuff3")

            # Creation of User - Codebrekaer's Guess button
            self.creation_code_button = ttk.Button(self, text = "Create the code", command = lambda:self.creationUsersCmCodeCommand())
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
                
            

            if self.code_length == 3:
                self.label_cm_ins_box_head = Label(self, text = "Codemeaker's input.", font = ("Calibri", 13),
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

            else:
                self.label_cm_ins_box_head = Label(self, text = "Codemeaker's input.", font = ("Calibri", 13),
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


    def creationUsersCmCodeCommand(self):
        if self.code_length == 3:
            # textbox_1 check
            users_cm_input_1 = self.textbox_cm_1.get()
            print(users_cm_input_1)
            if users_cm_input_1 in self.shorted_colors:
                if users_cm_input_1 == "b": Mastermind.user_codemaker_list.append("Blue")
                elif users_cm_input_1 == "y": Mastermind.user_codemaker_list.append("Yellow")   
                elif users_cm_input_1 == "o": Mastermind.user_codemaker_list.append("Orange")
                elif users_cm_input_1 == "v": Mastermind.user_codemaker_list.append("Violet")
                elif users_cm_input_1 == "g": Mastermind.user_codemaker_list.append("Green")
                elif users_cm_input_1 == "l": Mastermind.user_codemaker_list.append("Lime")
    
            # textbox_2 check
            users_cm_input_2 = self.textbox_cm_2.get()
            if users_cm_input_2 in self.shorted_colors:
                if users_cm_input_2 == "b": Mastermind.user_codemaker_list.append("Blue")
                elif users_cm_input_2 == "y": Mastermind.user_codemaker_list.append("Yellow")
                elif users_cm_input_2 == "o": Mastermind.user_codemaker_list.append("Orange")
                elif users_cm_input_2 == "v": Mastermind.user_codemaker_list.append("Violet")
                elif users_cm_input_2 == "g": Mastermind.user_codemaker_list.append("Green")
                elif users_cm_input_2 == "l": Mastermind.user_codemaker_list.append("Lime")

            # textbox_3 check
            users_cm_input_3 = self.textbox_cm_3.get()
            if users_cm_input_3 in self.shorted_colors:
                if users_cm_input_3 == "b": Mastermind.user_codemaker_list.append("Blue")
                elif users_cm_input_3 == "y": Mastermind.user_codemaker_list.append("Yellow")   
                elif users_cm_input_3 == "o": Mastermind.user_codemaker_list.append("Orange")
                elif users_cm_input_3 == "v": Mastermind.user_codemaker_list.append("Violet")
                elif users_cm_input_3 == "g": Mastermind.user_codemaker_list.append("Green")
                elif users_cm_input_3 == "l": Mastermind.user_codemaker_list.append("Lime")

            self.creation_code_button['state'] = DISABLED    
            self.users_cm_code_label = ttk.Label(self, text = Mastermind.user_codemaker_list, font = ("Calibri", 13), width = 22,
                                                 relief = SUNKEN, background = "cyan")
            self.users_cm_code_label.place(x = 30, y = 480)
            #self.users_cm_code_label.config(relief = SUNKEN, background = "cyan")
            return Mastermind.user_codemaker_list



        else:
            # textbox_cm_1 
            users_cm_input_1 = self.textbox_cm_1.get()
            if users_cm_input_1 in self.shorted_colors:
                if users_cm_input_1 == "b": Mastermind.user_codemaker_list.append("Blue")
                elif users_cm_input_1 == "y": Mastermind.user_codemaker_list.append("Yellow")   
                elif users_cm_input_1 == "o": Mastermind.user_codemaker_list.append("Orange")
                elif users_cm_input_1 == "v": Mastermind.user_codemaker_list.append("Violet")
                elif users_cm_input_1 == "g": Mastermind.user_codemaker_list.append("Green")
                elif users_cm_input_1 == "l": Mastermind.user_codemaker_list.append("Lime")
    
            # textbox_cm_2 
            users_cm_input_2 = self.textbox_cm_2.get()
            if users_cm_input_2 in self.shorted_colors:
                if users_cm_input_2 == "b": Mastermind.user_codemaker_list.append("Blue")
                elif users_cm_input_2 == "y": Mastermind.user_codemaker_list.append("Yellow")
                elif users_cm_input_2 == "o": Mastermind.user_codemaker_list.append("Orange")
                elif users_cm_input_2 == "v": Mastermind.user_codemaker_list.append("Violet")
                elif users_cm_input_2 == "g": Mastermind.user_codemaker_list.append("Green")
                elif users_cm_input_2 == "l": Mastermind.user_codemaker_list.append("Lime")

            # textbox_cm_3 
            users_cm_input_3 = self.textbox_cm_3.get()
            if users_cm_input_3 in self.shorted_colors:
                if users_cm_input_3 == "b": Mastermind.user_codemaker_list.append("Blue")
                elif users_cm_input_3 == "y": Mastermind.user_codemaker_list.append("Yellow")   
                elif users_cm_input_3 == "o": Mastermind.user_codemaker_list.append("Orange")
                elif users_cm_input_3 == "v": Mastermind.user_codemaker_list.append("Violet")
                elif users_cm_input_3 == "g": Mastermind.user_codemaker_list.append("Green")
                elif users_cm_input_3 == "l": Mastermind.user_codemaker_list.append("Lime")
            # textbox_cm_4 
            users_cm_input_4 = self.textbox_cm_4.get()
            if users_cm_input_4 in self.shorted_colors:
                if users_cm_input_4 == "b": Mastermind.user_codemaker_list.append("Blue")
                elif users_cm_input_4 == "y": Mastermind.user_codemaker_list.append("Yellow")   
                elif users_cm_input_4 == "o": Mastermind.user_codemaker_list.append("Orange")
                elif users_cm_input_4 == "v": Mastermind.user_codemaker_list.append("Violet")
                elif users_cm_input_4 == "g": Mastermind.user_codemaker_list.append("Green")
                elif users_cm_input_4 == "l": Mastermind.user_codemaker_list.append("Lime")

            self.creation_code_button['state'] = DISABLED    
            self.users_cm_code_label = ttk.Label(self, text = Mastermind.user_codemaker_list, font = ("Calibri", 13), width = 22,
                                                 relief = SUNKEN, background = "cyan")
            self.users_cm_code_label.place(x = 30, y = 480)
            #self.users_cm_code_label.config(relief = SUNKEN, background = "cyan")
            return Mastermind.user_codemaker_list #else:
                

        #self.creationOfCode()#, duplicate_colors_in_code = FirstsSettingsWindow.settings(self))

    def newGameMenuButton(self):
        self.destroy()
        Mastermind(self.users_role_in_game, self.number_of_colors, self.code_length, self.duplicate_colors_in_code)
        
    def comandOfGuessButton(self, creationofcode):
        #self.guess_button = ttk.Button(self, text = "Guess", command = lambda:e)
        #a = self.creationOfCode(colors = available_colors, duplicate_colors_in_code
        #                                                                = duplicate_colors_in_code)
        #while True:
        #creationofcode = self.creationOfCode(colors = self.available_colors, duplicate_colors_in_code
                                                                       # = duplicate_colors_in_code)
        #creationofcode = self.creationOfCode(colors = self.available_colors, duplicate_colors_in_code
                                                                        #= duplicate_colors_in_code)
            
            #b = self.codeBreaker()
            #c = self.codeBreaker()
        codebreaker = self.codeBreaker()
            #self.validationOfGuess()
        if self.validationOfCbGuess(guesscbreturnablevalue = codebreaker) == 1:
            
        
                #d = self.printingcode(copiedguess = codebreaker, copiedlist = creationofcode)
            printingcode = self.printingcode(copiedguess = codebreaker, copiedlist = creationofcode)

        
                #e = self.answerAndFeedbackCbLabels(text = d,code = codebreaker)
            answerandfeedbackcblabels = self.answerAndFeedbackCbLabels(text = printingcode,
                                                                           code = codebreaker)
        else:self.errorInputWarning()



    def validationOfCbGuess(self, guesscbreturnablevalue):        
        guesscbreturnablevalue = list(Mastermind.guesses_list)
        if len(guesscbreturnablevalue) != self.code_length:
            return 2 # It means True
        elif len(guesscbreturnablevalue) == self.code_length:
            return 1 # It means False
        #else: return 1 # It means False




#######################################################################################################################
    def creationOfCode(self, colors, duplicate_colors_in_code):
        #available_colors_tuple = tuple(colors)
        available_colors_list = list(colors)
        print("available_colors_list", available_colors_list)
        if len(Mastermind.color) == self.code_length:
            #print("1", Mastermind.color)
            return Mastermind.color

        #if duplicate_colors_in_code is False:
        if duplicate_colors_in_code == "False":
            #if len(MastermindsCode.color) == code_length:
                #return MastermindsCode.color
            #else:t
            Mastermind.color = random.sample(available_colors_list, k = self.code_length)
            print("without duplicate colors :", Mastermind.color)
            return Mastermind.color
        elif duplicate_colors_in_code == "True":
        #elif duplicate_colors_in_code is True:
            Mastermind.color = random.choices(available_colors_list, k = self.code_length)
            print("with duplicate colors :", Mastermind.color)
            return Mastermind.color




       
    def creationOfCbanswernumAndLabels(self):
        self.label_head_cb = Label(self, text = "Codebreaker's answers.", font = ("Calibri", 13),
                                   background = "PeachPuff3")
        self.label_head_cb.place(x = 8, y = 10)
        for _ in range(10):
            #self.label_cb = Label(self, text = str(_ + 1) + "  ----")
            self.label_cb = Label(self, text = str(_ + 1), font = ("Calibri", 12), background = "PeachPuff3")
            self.label_cb.place(x = 8, y = creationOfCbanswer_list[_])
            Mastermind.label_feedback_list.append(Label(self, background = "NavajoWhite2",
                                                        font = ("Calibri", 12), width = 24))
            Mastermind.label_feedback_list[_].place(x = 320, y = creationOfCbanswer_list[_])

            Mastermind.label_answer_cb_list.append(Label(self, background = "light grey",
                                                         font = ("Calibri", 12), width = 24))
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
            Mastermind.label_answer_cb_list[Mastermind.counter].place(x = 30,
                                                                      y = creationOfCbanswer_list[Mastermind.counter])

            Mastermind.label_feedback_list[Mastermind.counter].config(text = text)
            Mastermind.label_feedback_list[Mastermind.counter].place(x = 320,
                                                                     y = creationOfCbanswer_list[Mastermind.counter])

            Mastermind.counter += 1
            if Mastermind.counter < 10:
                #Mastermind.label_answer_cb_list[Mastermind.counter].config(background = "light blue")
                Mastermind.label_answer_cb_list[Mastermind.counter].config(relief = SUNKEN,
                                                                           background = "LightSteelBlue3")
                
            if Mastermind.counter == 10:
                self.guess_button['state'] = DISABLED
                Mastermind.endOfTheGameOutOfGuesses(self)
                
            elif Mastermind.feedback_list.count("Red") == self.code_length:
                self.guess_button['state'] = DISABLED
                Mastermind.endOfGameWinner(self)
#######################################
        #elif Mastermind.counter == 9:
            #Mastermind.endOfTheGame(self)
        #else: print("End of the game")
        
    def creationOfCbFeedback(self):
        self.label_feedback_head = Label(self, text = "Codebreaker's feedback.", font = ("Calibri", 13),
                                         background = "PeachPuff3")
        self.label_feedback_head.place(x = 300, y = 10)
        for __ in range(10):
            #self.label_feedback = Label(self, text = "feedback " + str(__ + 1))
            self.label_feedback = Label(self, text = str(__ + 1), font = ("Calibri", 12), background = "PeachPuff3")
            self.label_feedback.place(x = 300, y = creationOfCbanswer_list[__])
        #self.label_2 = Label(self, text = "2")
        #self.label_2.place(x = 20, y = 300)
            #self.label.grid(column = 0, row = 0)
            
    def mainWindowCreationMenuBar(self):
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
        helpmenu.add_command(label = "Help Index", command = lambda:HelpAndAbout.helpIndex(self))
        helpmenu.add_command(label = "About...", command = lambda:HelpAndAbout.about(self))
        menubar.add_cascade(label = "Help", menu = helpmenu)

    #def inputList(self):
        #users_input_1 = (self.textbox_1.get()).split("-")
        #return users_input_1

    def codeBreaker(self):
        Mastermind.guesses_list.clear()
        #self.guesses_list = []
        #self.guesses_list.clear() # Clears the list
        
        
        if self.code_length == 3:
            
            # textbox_1 check
            users_input_1 = self.textbox_1.get()
            if users_input_1 in self.shorted_colors:
                if users_input_1 == "b": Mastermind.guesses_list.append("Blue")
                elif users_input_1 == "y": Mastermind.guesses_list.append("Yellow")   
                elif users_input_1 == "o": Mastermind.guesses_list.append("Orange")
                elif users_input_1 == "v": Mastermind.guesses_list.append("Violet")
                elif users_input_1 == "g": Mastermind.guesses_list.append("Green")
                elif users_input_1 == "l": Mastermind.guesses_list.append("Lime")
    
            # textbox_2 check
            users_input_2 = self.textbox_2.get()
            if users_input_2 in self.shorted_colors:
                if users_input_2 == "b": Mastermind.guesses_list.append("Blue")
                elif users_input_2 == "y": Mastermind.guesses_list.append("Yellow")
                elif users_input_2 == "o": Mastermind.guesses_list.append("Orange")
                elif users_input_2 == "v": Mastermind.guesses_list.append("Violet")
                elif users_input_2 == "g": Mastermind.guesses_list.append("Green")
                elif users_input_2 == "l": Mastermind.guesses_list.append("Lime")

            # textbox_3 check
            users_input_3 = self.textbox_3.get()
            if users_input_3 in self.shorted_colors:
                if users_input_3 == "b": Mastermind.guesses_list.append("Blue")
                elif users_input_3 == "y": Mastermind.guesses_list.append("Yellow")   
                elif users_input_3 == "o": Mastermind.guesses_list.append("Orange")
                elif users_input_3 == "v": Mastermind.guesses_list.append("Violet")
                elif users_input_3 == "g": Mastermind.guesses_list.append("Green")
                elif users_input_3 == "l": Mastermind.guesses_list.append("Lime")
            return Mastermind.guesses_list



        else:
            # textbox_1 check
            users_input_1 = self.textbox_1.get()
            if users_input_1 in self.shorted_colors:
                if users_input_1 == "b": Mastermind.guesses_list.append("Blue")
                elif users_input_1 == "y": Mastermind.guesses_list.append("Yellow")   
                elif users_input_1 == "o": Mastermind.guesses_list.append("Orange")
                elif users_input_1 == "v": Mastermind.guesses_list.append("Violet")
                elif users_input_1 == "g": Mastermind.guesses_list.append("Green")
                elif users_input_1 == "l": Mastermind.guesses_list.append("Lime")
    
            # textbox_2 check
            users_input_2 = self.textbox_2.get()
            if users_input_2 in self.shorted_colors:
                if users_input_2 == "b": Mastermind.guesses_list.append("Blue")
                elif users_input_2 == "y": Mastermind.guesses_list.append("Yellow")
                elif users_input_2 == "o": Mastermind.guesses_list.append("Orange")
                elif users_input_2 == "v": Mastermind.guesses_list.append("Violet")
                elif users_input_2 == "g": Mastermind.guesses_list.append("Green")
                elif users_input_2 == "l": Mastermind.guesses_list.append("Lime")

            # textbox_3 check
            users_input_3 = self.textbox_3.get()
            if users_input_3 in self.shorted_colors:
                if users_input_3 == "b": Mastermind.guesses_list.append("Blue")
                elif users_input_3 == "y": Mastermind.guesses_list.append("Yellow")   
                elif users_input_3 == "o": Mastermind.guesses_list.append("Orange")
                elif users_input_3 == "v": Mastermind.guesses_list.append("Violet")
                elif users_input_3 == "g": Mastermind.guesses_list.append("Green")
                elif users_input_3 == "l": Mastermind.guesses_list.append("Lime")
            # textbox_4 check
            users_input_4 = self.textbox_4.get()
            if users_input_4 in self.shorted_colors:
                if users_input_4 == "b": Mastermind.guesses_list.append("Blue")
                elif users_input_4 == "y": Mastermind.guesses_list.append("Yellow")   
                elif users_input_4 == "o": Mastermind.guesses_list.append("Orange")
                elif users_input_4 == "v": Mastermind.guesses_list.append("Violet")
                elif users_input_4 == "g": Mastermind.guesses_list.append("Green")
                elif users_input_4 == "l": Mastermind.guesses_list.append("Lime")  
            return Mastermind.guesses_list #else:

        

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
        
##    def about(self):
##        messagebox.showinfo(title = "About", message = '''Mastermind game.
##A creation of Mavrogiannis Michail
##and Panourgias Panagiotis
##for Open Hellenic Univercity
##and PLHPRO lesson,
##Academic Year 2022.''')
##
##    def helpIndex(self):
##        messagebox.showinfo("Help Index", '''Press color buttons to fill empty boxes and guess
##the color combination that Codemaker is hiding
##Good Luck and enjoy...''')
    
        
if __name__ == "__main__":

    FirstsSettingsWindow.mainloop()
    #FirstsSettingsWindow().mainloop()
    
    #print(Mastermind.color)
    #firstsetwin = FirstsSettingsWindow()
    #firstsetwin.mainloop()
    #print(MastermindsCode.color)
    #Mastermind().mainloop()

    #mainmenu()
    #MainControler()
    #Mastermind().mainloop()
    #Mastermind().mainloop()
