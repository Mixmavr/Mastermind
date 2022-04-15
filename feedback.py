code = ['a','b','c','d','e']

guess = ['f','c','g','r','d']

feedback_list = []

for i in range(len(code)):
    if code[i] == guess[i]:
        code[i] = 1
        guess[i] = 2
        feedback_list.append('red')
for j in range(len(guess)):
    if guess[j] in code:
        feedback_list.append('white')

print(feedback_list)

