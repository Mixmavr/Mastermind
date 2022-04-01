import random

BU = 'blue'
PL = 'purple'
YE = 'yellow'
OR = 'orange'
GR = 'green'
BL = 'black'

RED = 'red'
WHITE = 'white'

#codebrakersCode = [BL, PL,]

codebrakersCode = [BL, PL, OR, YE, PL]
five_colors = [BU, PL, YE, OR, GR, BL]


class Codemaker():
    codemakers_code_list = []
    temp_color_list = []
    codemakersFeedback_list = []
    #counter = 0
    def __init__(self, code_length):
        self.code_length = code_length
        #self.run()
        pass


    def codemakersCodeCreation(self):
        for color in range(Codemaker.code_length):
            Codemaker.codemakers_code_list.append(random.choice(five_colors))
        return Codemaker.codemakers_code_list


    def showCodemakersCode(self):
        if len(Codemaker.codemakers_code_list) == 0:print("\nEmpty color list... \nTry again\n")
        else:return print("\n", Codemaker.codemakers_code_list, "\n")


    def clearCodemakersCodelist(self):
        del Codemaker.codemakers_code_list[:]
        return Codemaker.codemakers_code_list


    def codemakersFeedback(self):
        for color_1 in range(Codemaker.code_length):
            if codebrakersCode[color_1] == Codemaker.codemakers_code_list[color_1]:
                print(codebrakersCode[color_1])
                print(Codemaker.codemakers_code_list[color_1])
                codebrakersCode[color_1] = 'cb'
                Codemaker.codemakers_code_list[color_1] = 'cm'
                Codemaker.codemakersFeedback_list.append(RED)
                #del Codemaker.codemakers_code_list[0]
        for color_2 in codebrakersCode:
            if color_2 in Codemaker.codemakers_code_list:Codemaker.codemakersFeedback_list.append(WHITE)
        return Codemaker.codemakersFeedback_list
    
##############################################

    #def run(self):
        #while True:
            #reply = input('Give the max number of colors, "4" or "5": ')
            #if not reply:break
            #elif reply.isdigit():
                #reply = int(reply)
                #if reply in (4,5):
                    #reply = int(reply)
                    #Codemaker.code_length = reply
                    #print(Codemaker.codemakersCodeCreation(self))
                    #Codemaker.clearCodemakersCodelist(self)
            
#if __name__ == "__main__":Codemaker()

##############################################

class Menu():
    #reply_list = []
    def __init__(self):
        while True:
            reply = input('Give the max number of colors, "4" or "5": ')
            if not reply:break
            elif reply.isdigit():
                reply = int(reply)
                if reply in (4,5):
                    #reply = int(reply)
                    Codemaker.code_length = reply
                    print(Codemaker.codemakersCodeCreation(self))
                    Codemaker.clearCodemakersCodelist(self)
                    #print("\nGuess Feedback", Codemaker.codemakersFeedback(self))
            


if __name__ == "__main__":Menu()

###########################################








        
