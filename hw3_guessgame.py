##Name: Moosa Abbasi
##UID: U37033529
##Brief Description: Guessing Game



import random

target_number = random.randint(1, 100)

tries = 0

while tries < 10:
    try:
        if tries == 0:
            user_guess = int(input("Enter a number between 1 and 100 inclusive: "))
        else:
            user_guess = int(input())
    except ValueError:
        print("Please enter a valid number between 1 and 100:",end = '')
        continue
    
   
    if 1 <= user_guess <= 100:
        tries += 1

        
        if user_guess == target_number:
            print(f"You guessed it right!! You got it in in {tries} guesses.")
            break
        elif user_guess < target_number:
            print("Too low. Try a higher number:", end =" ")
        else:
            print("Too high. Try a lower number:",end = '')

        remaining_tries = 10 - tries
        if remaining_tries > 0:
            None;
        else:
            print(f"Sorry, the number was {target_number}")
        
            break
    elif user_guess < 0:
        print("Really? Please enter a number between 1 and 100:",end = '')
    elif user_guess > 100:
        print("Very funny. Enter a number between 1 and 100 (inclusive)")
