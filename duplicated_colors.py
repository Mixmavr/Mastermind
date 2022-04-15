temp_color_list = []

import random

BU = 'blue'
PL = 'purple'
YE = 'yellow'
OR = 'orange'
GR = 'green'
BL = 'black'

colors = [BU, PL, YE, OR, GR, BL]

##########################
code_length = 5
num_of_dupl_colors = 1

counter = 0

while True:
    if counter <= code_length:
        color = random.choice(colors)
        duplicated_color = temp_color_list.count(color)
        if duplicated_color <= (num_of_dupl_colors - 1): #and len(temp_color_list) < 5:
            temp_color_list.append(color)
            counter += 1
        if len(temp_color_list) == 5:break
print(temp_color_list)



###########################
#for num in range(6):
    #color = random.choice(colors)
    #if color not in temp_color_list:
        #temp_color_list.append(color)
    #Codemaker.codemakers_code_list.append(tuple(Codemaker.temp_color_list))
#print(temp_color_list)


#for num in range(5):
    #if num == 5 and len(temp_color_list) < 5:continue
    #if len(temp_color_list) < 5:
        #color = random.choice(colors)
        #dublicate_color = temp_color_list.count(color)
        #if dublicate_color <= (2 - 1):temp_color_list.append(color)
        
    #len(temp_color_list) < 5:continue
    #Codemaker.codemakers_code_list.append(tuple(Codemaker.temp_color_list))
#print(temp_color_list)

############################

