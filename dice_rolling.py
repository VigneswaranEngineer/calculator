import random

player1_score = 0
player2_score = 0

for i in range(10):
    player1_value = random.randint(1,6)
    player2_value = random.randint(1,6)
    print('player 1 rolled : ',player1_value)
    print('player 2 rolled : ',player2_value)
    if player1_value>player2_value:
       print('player 1 wins!')
       player1_score = player1_score+1
    elif player2_value>player1_value:
        print('player 2 wins!')
        player2_score = player2_value+1
    else:
        print("It's a draw!")
    input('press enter to continue')
print('##game over##')
print('player 1 score :',player1_score)
print('player 2 score :',player2_score)
