# A simple if-else statement assignment
print('You come across an old knight in a cave sitting before a table of cups.')
print('The knight says, "You must choose. But choose wisely. For as the true Grail will bring you life, a false Grail will take it from you."')
sit = input('Do you approach? (y/n)') # Decistion to approach the knight
if sit == 'y':
    print('Before you are three cups. A golden cup, a silver cup, and a wooden cup.')
    choose = input('Which do you choose? (g/s/w)') # Decition on which cup
    if choose == 'w':
        print('You have chosen... wisely.')
    else:
        print('You scream as you turn into a skeleton and are reduced to dust.')
        print('"You chose... poorly," says the knight.')
else:
    print('Farewell.')
input('Press ENTER to exit')
