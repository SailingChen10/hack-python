#this is a number game
import random
random_number=random.randint(0,20)
i= 0
for i in range(9):
    input_number = int(input("Please tell me an integer that ranges from 0 to 20:"))
    if input_number == random_number:
        print ("Bingo!Your answer is right!")
        break
    elif input_number < random_number:
        print("Your answer is less.")
        i=i+1
        k=10-i
        print("You have only %d chances to guess the number."%k)
    else:
        print("Your answer is greater.")
        i=i+1
        k=10-i
        print("You have only %d chances to guess the number."%k)
            
    
