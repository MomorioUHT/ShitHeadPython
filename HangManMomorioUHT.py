temporary = []
guessed = []
GameEnd = False
stepsize = 0
displaying = ''

while True:
    Answer = str(input("Enter Answer : ")).upper()
    if " " in Answer:
        print("Spacing is not allowed!")
    else: break

for i in range(len(Answer)): displaying += '_'
print(' ')
print('Start Guessing!')
print(displaying)
print(' ')

def wrong(letter):
    if letter not in temporary: temporary.append(letter)
    if stepsize == 1:
        print(' ')
        print('=====O')
        print('||.')
        print('||.')
        print('||.')
        print('===')
        print(*temporary)
        print(' ')
    elif stepsize == 2:
        print(' ')
        print('=====O')
        print('||.  |')
        print('||.')
        print('||.')
        print('===')  
        print(*temporary)
        print(' ')     
    elif stepsize == 3:
        print(' ')
        print('=====O')
        print('||. /|')
        print('||.')
        print('||.')
        print('===') 
        print(*temporary)
        print(' ')
    elif stepsize == 4:
        print(' ')
        print('=====O')
        print('||. /|\ ')
        print('||.')
        print('||.')
        print('===')  
        print(*temporary)
        print(' ')
    elif stepsize == 5:
        print(' ')
        print('=====O')
        print('||. /|\ ')
        print('||. /')
        print('||.')
        print('===')
        print(*temporary)
        print(' ')     
    elif stepsize == 6:
        print(' ')
        print('=====O')
        print('||. /|\ ')
        print('||. / \ ')
        print('||.')
        print('===')  
        print(*temporary)
        print(' ')
        print("You Died!")
        print(f"The correct answer is {Answer}")
        print(' ')
        global GameEnd
        GameEnd = True
    
    
    
def correct(letter, underscore_text, correct_text):
    global displaying
    underscore_text_list = [i for i in underscore_text]
    correct_text_list = [i for i in correct_text]
    
    for i in range(len(correct_text_list)):
        if correct_text_list[i] == letter: underscore_text_list[i] = letter
            
    temp = ''
    for i in underscore_text_list: temp += i
    displaying = temp
    print(' ')
    print(displaying)
    print(' ')
    
while GameEnd is False:
    if displaying == Answer:
        print(f"Correct!, The hidden word is {Answer}")
        print(' ')
        GameEnd = True
    else:
        Guess = str(input("Guess >> ")).upper()
        if " " in Guess:
            print("You cannot put space as a guess!")
            print(" ")
        elif len(Guess) > 1:
            print("You can only Guess 1 character per round!")
            print(" ")
        else:
            if Guess in guessed:
                print("You cannot guess the same character as before!")
                print(" ")
            else:
                if Guess not in Answer:
                    stepsize += 1
                    wrong(Guess)
                else:
                    correct(Guess, displaying, Answer)
                guessed.append(Guess)