import random
print('INSTRUCTIONS :\n------------\n1. You are allowed to choose a number between 1 and 10\n2. You will get three chances in a trial\n3. You will be hinted on every wrong attempt...so do hve a check\n\nThats all BEST OF LUCK..!!')
play_game='y'
while(play_game=='y'):
    system_guess=random.randint(1,10)
    user_guess=int(input('Make a Guess between (1,10) : '))
    count=1
    while(user_guess!=system_guess):
        print("You had a wrong guess...")

        if(count==3):
            break
        elif(user_guess>system_guess):
            print('You are exceeding actual guesss....')
        else:
            print('You are preceding actual guesss...')

        count+=1
        user_guess=int(input('Try another guesss... '))

    if(user_guess==system_guess):
        print('Hurrayyy!!!...You Won in {} attempts'.format(count))
    else:
        print('You Lose...')
        print('Actual guess was... ',system_guess)
    play_game=input('Do you want to play one more time (y/n) : ')

print('Game Over\n----------')
