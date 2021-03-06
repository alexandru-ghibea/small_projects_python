"""
Create a program that generates a random password for
 1. n specified letters e.g. 13 letter password
 2. n specified symbols e.g. @#$
 3. n specified numbers e.g. 1/2/3
"""
import random
import string

all_letters = string.ascii_letters
numbers = string.digits

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the PyPassword Generator!")

while True:
  try:
     number_of_letters = int(input("How many letters would you like in your password ?: "))
  except ValueError:
     print("Not an integer!")
     continue
  else:
     print("Yes an integer!")
     break
while True:
    try:
        number_of_symbols = int(input("How many symbols would you like?: "))
    except ValueError:
        print("Not an integer!")
        continue
    else:
        print("Yes an integer!")
        break
while True:
    try:
        number_of_numbers = int(input("How many numbers would you like?: "))
    except ValueError:
        print("Not an integer!")
        continue
    else:
        print("Yes an integer!")
        break

letters_to_use = ''.join(random.choice(all_letters) for x in range(number_of_letters))
numbers_to_use = ''.join(random.choice(numbers) for x in range(number_of_numbers))
symbols_to_use = ''.join(random.choice(symbols) for x in range(number_of_symbols))
password_v1 = (letters_to_use + numbers_to_use + symbols_to_use)
print(f"Here is your password 1 version :{password_v1}")

"""
For added complexity to the password you can shuffle the password.
"""

password_v2 = "".join(random.sample(password_v1,len(password_v1)))
print(f"Here is your password 2 version :{password_v2}")
