
                                                 #Number Guessing Game

import random
secret_number = random.randint(1,10)

attempt=3
while attempt>=1:
    a=int(input("Guess the number between 1 and 10: "))
    if a>10 or a<1:
            print("Your guess is out of range. Please guess a number between 1 and 10.")
            continue
    attempt=attempt-1
    
    if a==secret_number:
            print("Congratulations! you guessed the right number")
            break
    

    elif a<secret_number:
            print("Too low. Try again.")
    elif a>secret_number:
            print("Too high. Try again.")
   
    
else:
    print("Number is: ", secret_number, " Better luck next time")
