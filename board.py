import random
board=[['-','-','-'],['-','-','-'],['-','-','-']]
def print_board():
  print(*board,sep="\n")
  #(*board,sep="\n") is used to separate list elements on new lines
def whogoesfirst(player):
  player=random.randint(1,2)
  print("Player ",player," goes first.")
  if player == 1:
    return 1
  else:
    return 2
def game():
  print_board()
  

print_board()
whogoesfirst(player)
game()