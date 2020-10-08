#comment added 
# made with python while loop and random.randint()
import random

w_n = random.randint(1,60)
game_over = True
guess=1
while game_over:
  usr = int(input('user input : '))
  if usr == w_n :
    print(f'You Won in {guess}th time')
    game_over = False
  else:
    if usr < w_n:
      print('Too Low')
    elif usr > w_n:
      print('Too High')
    guess += 1
