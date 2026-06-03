import random
import time

def random_generator(start: int, end: int)-> int:
  return random.randint(start, end)
  
"""
def generated_lists(end = 10, guess= 3):
  return [
  random_generator(1, 10) for _ in range(guess)
  ]"""

def user_guess(level, guess = 3):
  user_guess = []
  
  while len(user_guess) < guess:
    try:
      choice = int(input("Enter your guess: "))
      if choice < 1 or choice > level:
        raise ValueError(f"Please choose from 1 to {level}")
      elif choice in user_guess:
        raise ValueError("Number selected already chosen!")
      else:
        user_guess.append(choice)
        
    except ValueError as e:
      if "invalid" in str(e):
        print("Invalid input")
      else:
        print("Error",e)
      
  return user_guess

 
def generated_lists(end: int = 10, guess: int = 3) -> list:
    if guess > end:
        guess = end
    
    return random.sample(range(1, end + 1), guess)
 
def operation(lst_1, lst_2):
  list_3 = set()
  
  for x in lst_2:
    if x in lst_1:
      list_3.add(x)
  return list_3
  
def list_create(level, guess=3):
  print(f"Pick {guess} numbers from 1 to {level} to guess hidden numbers")
  print("X"*guess,"Are the hidden numbers")
  list = generated_lists(level, guess)
  list_2 = user_guess(level, guess)
  list_3 = operation(list, list_2)
  
  
  
  print(list)
  print(list_2)
  
  if list_3:
    print(f"Congrats, The number(s) you succefully guessed are {', '.join(map(str, sorted(list_3)))} in {list}")
  else:
    print("No items guessed unfortunatly!!!")
    
    
def Level_one():
  print("Level 1")
  print("""
  1. Bigginer\n
  2. Intermediate\n
  3. Hard
  4. Exit
  """)
  while True:
    try:
      choice = int(input("Enter your choice: "))
      if choice not in [1,2,3,4]:
        raise ValueError("invalid input")
      
      else:
        break
    except ValueError as e:
      print("Error:",e)
    
  
  if choice == 1:
    choice == "y"
    while choice:
      list_create(10)
      choice = input("Play again Y/N: ").lower()
      if choice == "n":
        return Level_one()
    
  elif choice == 2:
    choice == "y"
    while choice:
      list_create(20, 5)
      choice = input("Play again Y/N: ").lower()
      if choice == "n":
        return Level_one()
  
  elif choice == 3:
    choice == "y"
    while choice:
      list_create(50, 8)
      choice = input("Play again Y/N: ").lower()
      if choice == "n":
        return Level_one()
  else:
    print("Thanks for playing....")
    return
    

Level_one()



  
  
  
    
    
  

  
  
  
    
  

  