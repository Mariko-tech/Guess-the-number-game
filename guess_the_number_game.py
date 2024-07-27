import random

while True:
    n = int (input ('Please input small number'))
    m = int (input ('Please input large number'))
    if n > m:
        print("Try again. The first number must be smaller than second one.")
    else:
        break

CP_number = random.randint(n, m)
max_attempts = 5
try_count = 0

for count in range (max_attempts):
    user_guess = int (input('Which number created by computer is between the small number and the large number?')) 
    try_count += 1
    if user_guess == CP_number:
        print("That's correct!")
        break
    elif max_attempts - try_count == 0:
        print("Game over! The number is " + str(CP_number))
        break
    else:
        print("Try again! " + str(max_attempts - try_count) + " attempts remaining.")