import random
import time

  
def tik_tak_board():
  return [
    [x for x in range(i, i + 3)]
    for i in range(1, 10, 3)
    ]

#purpose of this function is to dertimine what the roe is
def place_mark(board,chosen,mark,number):
  row = (number - 1) // 3
  index = board[row].index(number)
  board[row][index] = mark
  chosen.append(number)
"""  
def board_print(board):
  for x in board:
    for i in x:
      print(i, end=" ")
    print()
  print("_______________")
"""  
  
  

def board_print(board):
    print("+-------+-------+-------+")
    for row in board:
        print("|          |         |        |")
        print(f"| {str(row[0]):^5}   | {str(row[1]):^5} | {str(row[2]):^5} |")
        print("|          |         |        |")
        print("+-------+-------+-------+")
def win_check(board):
  
  top = (
    board[0][0] == board[0][1] == board[0][2]
    and board[0][0] != "")


  down = (
    board[1][0] == board[1][1] == board[1][2]
    and board[1][0] != "")


  below = (
    board[2][0] == board[2][1] == board[2][2]
    and board[2][0] != "")

  side = (
    board[0][0] == board[1][0] == board[2][0]
    and board[0][0] != "")


  middle = (
    board[0][1] == board[1][1] == board[2][1]
    and board[0][1] != "")
    

  last = (
    board[0][2] == board[1][2] == board[2][2]
    and board[0][2] != "")


  left_slant = (
    board[0][0] == board[1][1] == board[2][2]
    and board[0][0] != "")


  right_slant = (
    board[0][2] == board[1][1] == board[2][0]
    and board[0][2] != "")
  
  
  if top:
    if board[0][0] == "X":
      return "X"
    else:
      return "O"
  if down:
    if board[1][0] == "X":
      return "X"
    else:
      return "O"
  if below:
    if board[2][0] == "X":
      return "X"
    else:
      return "O"
  if side:
    if board[0][0] == "X":
      return "X"
    else:
      return "O"
          
  if middle:
    if board[0][1] == "X":
      return "X"
    else:
      return "O"
  if last:
    if board[0][2] == "X":
      return "X"
    else:
      return "O"
  if left_slant:
    if board[1][1] == "X":
      return "X"
    else:
      return "O"
  if right_slant:
    if board[1][1] == "X":
      return "X"
    else:
      return "O"
  

def game(user_input,num=0):
  board = tik_tak_board()
  chosen = []
  
  winner = False
  turn = user_input
  while len(chosen) < 9:
    
    if turn == "computer":
      try:
        rand = random.randint(1, 9)
        if rand in chosen:
          raise ValueError("")
        
        if rand not in chosen:
          #print(rand,"random")
          
          place_mark(board,chosen,number=rand,mark="X"
            )
          print("Computer's turn")
          
          time.sleep(2)
          print("Computer has picked",rand)
          board_print(board)
          
          result = win_check(board)
          if result == "X": 
            print("Computer wins")
            winner = True
            break
          elif result == "O": 
            print("You win")
            winner = True
            break
          turn = "user"
        """ 
        if rand in [1,2,3]:
              
          ind = board[0].index(rand)
          board[0][ind] = "X"
          chosen.append(rand)
          turn = "user"
              
        if rand in [4,5,6]:
          ind = board[1].index(rand)
          board[1][ind] = "X"
          chosen.append(rand)
          turn = "user"
              
        if rand in [7,8,9]:
          ind = board[2].index(rand)
          board[2][ind] = "X"
          chosen.append(rand)
          turn = "user"
        """
          
      except ValueError as e:
        print(e)
    if len(chosen) == 9:
        break
  
      
    
  
  
    if turn == "user":

      try:
        if num == 1:
          board_print(board)
          num *=0
        choice = int(input("Enter your turn: "))
        
        
        if choice < 1 or choice > 9:
          raise ValueError("Error")
        if choice in chosen:
          raise ValueError("Number already picked")
          
        place_mark(board,chosen,number=choice,mark="O")
        board_print(board)
        
        result = win_check(board)
        if result == "X":
          print("Computer wins")
          winner = True
          break
        elif result == "O":
          print("You win")
          winner = True
          break
          
        turn = "computer"
      
        """
        if choice in [1,2,3]:
          ind = board[0].index(choice)
          board[0][ind] = "O"
          chosen.append(choice)
          turn = "computer"
          
        if choice in [4,5,6]:
          ind = board[1].index(choice)
          board[1][ind] = "O"
          chosen.append(choice)
          turn = "computer"
            
        if choice in [7,8,9]:
          ind = board[2].index(choice)
          board[2][ind] = "O"
          chosen.append(choice)
          turn = "computer"
        """
  
         
      except ValueError as e:
        print(e)
      
  if len(chosen) == 9 and not winner:
    print("Draw game")
  
  

def main():
    print("=" * 35)
    print("        TIC - TAC - TOE")
    print("=" * 35)

    while True:
        print("\nMenu")
        print("-" * 35)
        print("1. You start first")
        print("2. Computer starts first")
        print("0. Quit")
        print("-" * 35)

        try:
            choice = int(input("Select an option: "))

            if choice == 1:
                game("user",1)

            elif choice == 2:
                game("computer")

            elif choice == 0:
                print("\nThanks for playing. Goodbye!")
                break

            else:
                print("Invalid choice. Select 0, 1, or 2.")

        except ValueError:
            print("Please enter a valid number.")


main()


    

    