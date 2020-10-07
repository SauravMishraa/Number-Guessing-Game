import random

w_n = random.randint(1,100)
game_over = True
guess=1
usr = int(input('user input : '))
while game_over:
  if usr == w_n :
    print(f'You Won in {guess} time')
    game_over = False
  else:
    if usr < w_n:
      print('Too Low')
      usr = int(input('user input : '))
    if usr > w_n:
      print('Too High')
      usr = int(input('user input : '))
    guess += 1
