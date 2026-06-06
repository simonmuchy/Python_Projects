db = {
    "Bananas": {
        "price": 0.99,
        "quantity": 50,
        "category": "Fruits"
    },
    "Red Apples": {
        "price": 1.49,
        "quantity": 35,
        "category": "Fruits"
    },
    "Strawberries": {
        "price": 3.99,
        "quantity": 20,
        "category": "Fruits"
    },
    "Broccoli": {
        "price": 1.79,
        "quantity": 25,
        "category": "Vegetables"
    },
    "Carrots": {
        "price": 0.89,
        "quantity": 40,
        "category": "Vegetables"
    },
    "Whole Milk": {
        "price": 3.49,
        "quantity": 30,
        "category": "Dairy"
    },
    "Cheddar Cheese": {
        "price": 4.99,
        "quantity": 15,
        "category": "Dairy"
    },
    "Paper Towels": {
        "price": 4.99,
        "quantity": 20,
        "category": "Home"
    },
    "Dish Soap": {
        "price": 2.29,
        "quantity": 15,
        "category": "Home"
    },
    "Bread Loaf": {
        "price": 2.99,
        "quantity": 25,
        "category": "Other"
    }
}

def total(db):
  total = 0
  for name, values in db.items():
    total += (values["price"] * values["quantity"] )
  return total
  
def most_exp(db):
  item = None
  exp = 0
  for name, value in db.items():
    total = value["price"] * value["quantity"]
    if total > exp:
      exp = total
      item = name
      
  return item,exp
  
def least_exp(db):
  item = None
  cheap = float("inf")

  for name, value in db.items():
        total = value["price"] * value["quantity"]
        
        if total < cheap:
            cheap = total
            item = name

  return item, cheap
      
    
    
category = set()
for v in db.values():
  category.add(v["category"])
cates = [x for x in category]
sorted_cates = sorted(cates)

sorted_category = {}

def category_items(category):
  for key, value in db.items():
    if value["category"] == category:
      sorted_category[key] = {
        "price": value["price"],
        "quantity": value["quantity"]
      }
  return sorted_category


def add_items():
  name = input("Enter Product name: ").title()
  db[name] = {
    "price": float(input("Price: ")),
    "quantity": int(input("Quantity: ")),
    "category": input("Category: ").title()
    }
    

def sorts(Category):
  #if sorted_category:
  if Category:
    i = 1
    for name, items in Category.items():
      print(i,".",name)
      print(" ",items["price"])
      print(" ",items["quantity"])
      i+=1
  else:
    print("No items yet, please add")


def show_menu():
    print("╔════════════════════════════════════╗")
    print("║       Grocery Price Tracker       ║")
    print("╚════════════════════════════════════╝")

    print("\nMenu:\n")

    print("1. Add item")
    print("2. View all items")
    print("3. Calculate total")
    print("4. Filter by category")
    print("5. Find most/least expensive")
    print("6. Remove item")
    print("7. Exit")
    choice = int(input("Enter choice"))
    return choice 

def main():
  choice = show_menu()
  
  if choice == 1:
    while True:
      add_items()
      print("Added")
      print("Enter 0 to add more 1 back")
      choice = input("Enter ")
      if choice == "1":
        main()
        
  elif choice == 2:
    i = 1
    for name, items in db.items():
      t = { items["price"] * items["quantity"]}
      print(f"{i}. {name}")
      print(f"- Price ${items["price"]} x {items["quantity"]} = ${t} ")
      print(f"- Category {items["category"]} ")
      i+=1
    print()
  
  elif choice == 4:
      x = 1
      for i in sorted_cates:
        print(x,f". {i}")
        x +=1
      choice = int(input("Selcect category to filter"))
      
      sorts(category_items(sorted_cates[choice - 1]))
      
  elif choice == 3:
    tota = round(total(db),2)
    print(f"You have a total of ${tota}")
  
  elif choice == 5:
    print("Most expensive")
    name, price = most_exp(db)
    print("  ",name)
    for key, value in db[name].items():
      print(key,value)
    print(f"total price ${price}")
    
    print("Most cheapest")
    item_name, price = least_exp(db)
    print("  ",item_name)
    for key,value in db[item_name].items():
      print(key,value)
    print(f"total price ${price}")

        
        
      
    
      
      
      
      
      
      
      
      
    
  
  
main()
  