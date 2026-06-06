# This is a command- line application that collects and displays user information

def is_valid_name(name):
   return name.isalpha()
  
def input_checker(value, validator, message):
  if not validator(value):
    raise ValueError(message)
  return value
  
def get_valid_input(prompt, validator, error):
    while True:
        try:
            value = input(prompt)
            return input_checker(value, validator, error)
        except ValueError as e:
            print(e)
            
def is_valid_email(email):
    if " " in email:
        return False

    if email.count("@") != 1:
        return False

    username, domain = email.split("@")

    if not username:
        return False

    if "." not in domain:
        return False

    return True
  
def validate_phone(phone):
    # Remove spaces
    phone = phone.replace(" ", "")

    # Must contain only digits
    if not phone.isdigit():
        return False

    # Accept 09XXXXXXXX or 9XXXXXXXX
    if len(phone) == 10 and phone.startswith("0"):
        prefix = phone[:3]
    elif len(phone) == 9:
        prefix = "0" + phone[:2]
    else:
        return False

    # Valid network prefixes
    valid_prefixes = {"097", "096", "095", "094"}

    return prefix in valid_prefixes
  
def format_phone(phone):
    phone = phone.replace(" ", "")

    if len(phone) == 10:
        phone = phone[1:]  # remove leading 0

    return f"+260 {phone[:3]} {phone[3:6]} {phone[6:]}"
    
    
def get_valid_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number")
        
first_name = get_valid_input("First name:",is_valid_name,"Name can only contain letters").title()

last_name = get_valid_input("Last name:",is_valid_name," Last name can only contain letters").title()

Age = get_valid_int("How old are you")

email = get_valid_input("Email adress:",is_valid_email,"invalid email adress")

phone_number = format_phone(get_valid_input("Phone number:",validate_phone,"Invalid phone number"))

city = get_valid_input("City name:",is_valid_name,"City name can only contain letters").title()

programs = get_valid_int("Number of programming languages you know")

experience = get_valid_int("level of experience in coding, in years?")

favorite_language = get_valid_input("Favourite programming language:",is_valid_name,"input can only contain letters").title()

try:
  is_learnig = get_valid_input("Are you currently leaning yes/no",is_valid_name,"Name cam only contain letters").lower()
  if is_learnig != "yes" and is_learnig != "no":
    raise ValueError("Answer can only be yes/no")
except ValueError as e:
  print("Error",e)
  is_learnig = get_valid_input("Are you currently leaning Yes/No",is_valid_name,"Name cam only contain letters").lower()
  
if experience == 0 or experience == 1:
  experience_level = "Beginner"
elif experience > 1 and experience <= 2:
  experience_level = "Intermediate"
else: experience_level = "Advanced"

try:
  avg = round(programs / experience,2)
except:
  avg = 0
  

  
message = "Keep up the good work bro"


  
  
print(f"""
╔══════════════════════════════════════════════╗
║          USER INFORMATION SUMMARY           ║
╠══════════════════════════════════════════════╣
║ Name: {first_name} {last_name}
║ Age: {Age} years old
║ Birth Year: {2026 - Age}
║ Email: {email}
║ Phone: {phone_number}
║ City: {city}
║
║ Programming Experience:
║   Languages Known: {programs}
║   Favorite Language: {favorite_language}
║   Years of Experience: {experience} year(s)
║   Experience Level: {experience_level}
║   Avg Languages/Year: {avg}
║   Student Status: {"Yes" if is_learnig else "No"}
║
║ Message: {message}
╚══════════════════════════════════════════════╝
""")
  
  
    
  
  
  
  


