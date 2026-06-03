import random

  
def board():
  board =  [
    [x for x in range(i, i + 3)]
    for i in range(1, 10, 3)
    ]
  
"""
def created_box():
  bo = board()
  
  for x in bo:
    for i in x:
      print(i, end=" ")
    print()
  print("_________")
"""
  

  
  

def game():
  board =  [
    [x for x in range(i, i + 3)]
    for i in range(1, 10, 3)
    ]
    
  
  
  
  

  
  chosen = []
  
  
  while len(chosen) < 10:
    #Possible ways to win
    top = (
    board[0][0] == board[0][1] == board[0][2]
    and board[0][0] != "")
    
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
    
    try:
      rand = random.randint(1, 9)
      if rand in chosen:
        raise ValueError("")
      
      if rand not in chosen:
        print(rand,"random")
        
        if rand in [1,2,3]:
            
            ind = board[0].index(rand)
            board[0][ind] = "X"
            chosen.append(rand)
            
        if rand in [4,5,6]:
            ind = board[1].index(rand)
            board[1][ind] = "X"
            chosen.append(rand)
            
        if rand in [7,8,9]:
            ind = board[2].index(rand)
            board[2][ind] = "X"
            chosen.append(rand)
    except ValueError as e:
      print("")
    
    
    
    
    print(chosen)
    for x in board:
      for i in x:
        print(i, end=" ")
      print()
    print("_________")
  
    try:
      if top:
        if board[0][0] == "X":
          print("Computer wins")
          break
        else:
          print("You win!")
          break
      if down:
        if board[1][0] == "X":
          print("Computer wins")
          break
        else:
          print("You win!")
          break
      if below:
          if board[2][0] == "X":
            print("Computer wins")
            break
          else:
            print("You win!")
            break
      if side:
        if board[0][0] == "X":
          print("Computer wins")
          break
        else:
          print("You win!")
          break
          
      if middle:
        if board[0][1] == "X":
          print("Computer wins")
          break
        else:
          print("You win!")
          break
      if last:
        if board[0][2] == "X":
          print("Computer wins")
          break
        else:
          print("You win!")
          break
      if left_slant:
        if board[1][1] == "X":
          print("Computer wins")
          break
        else:
          print("You win!")
          break
      if right_slant:
        if board[1][1] == "X":
          print("Computer wins")
          break
        else:
          print("You win!")
          break
        
      
      choice = int(input("Enter: ")) 
      if choice < 1 or choice > 9:
        raise ValueError("Error")
      if choice in chosen:
        raise ValueError("Number already picked")
          
      if choice in [1,2,3]:
        ind = board[0].index(choice)
        board[0][ind] = 0
        chosen.append(choice)
        
      if choice in [4,5,6]:
        ind = board[1].index(choice)
        board[1][ind] = 0
        chosen.append(choice)
          
      if choice in [7,8,9]:
        ind = board[2].index(choice)
        board[2][ind] = 0
        chosen.append(choice)
       
    except ValueError as e:
      print(e)
      
  print("Game Over")
        
      
  


while True:
  game()
  cho = int(input("0 to quit"))
  if cho == 0:
    break

"""
def actual_board():
  a,b,c,d = "+","-","|"," "
  
  print(a,b*15,a,b*15,a,b*15,a)
  print(c,d*19,c,d*18,c,d*18,c)
  print(c,d*19,c,d*18,c,d*18,c   )
  print(c,d*19,c,d*18,c,d*18,c)
  print(a,b*15,a,b*15,a,b*15,a)
  print(c,d*19,c,d*18,c,d*18,c)
  print(c,d*19,c,d*18,c,d*18,c)
  print(c,d*19,c,d*18,c,d*18,c   )
  print(a,b*15,a,b*15,a,b*15,a)
  print(c,d*19,c,d*18,c,d*18,c)
  print(c,d*19,c,d*18,c,d*18,c)
  print(c,d*19,c,d*18,c,d*18,c  )
  print(a,b*15,a,b*15,a,b*15,a)

actual_board()
"""
  

    

    