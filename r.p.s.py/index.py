import random

choices = ['rock','paper','scissors']

computer = random.choice(choices)
player = None

while player not in choices:
    player = input('rock, paper, or scissors?: ').lower()
if player == computer:
    print('computer: ',computer)
    print('player: ',player)
    print('Tie!')
elif player =='rock':
    if computer == 'paper':
        print('computer: ',computer)
        print('player: ',player)
        print('You lose')
    if computer == 'scissers':
        print('computers: ',computer)
        print('player: ',player)
        print('you win!')

elif player =='scissers':
    if computer == 'rock':
        print('computers: ',computer)
        print('player: ',player)
        print('You lose')
    if computer == 'paper':
        print('computers: ',computer)
        print('player: ',player)
        print('you win!')
elif player =='paper':
    if computer == 'scissers':
        print('computer: ',computer)
        print('player: ',player)
        print('You lose')
    if computer == 'scisser':
        print('computer: ',computer)
        print('player: ',player)
        print('you win!')
#print('computer: ',computer)
#print('player: ',player)