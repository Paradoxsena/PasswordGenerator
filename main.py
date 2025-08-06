from string import ascii_letters, digits
import random

characters =  ascii_letters + digits

size = int(input("Enter the password length: "))
password = "".join(random.choice(characters) for _ in range(size))

print("Your password is:{}".format(password))