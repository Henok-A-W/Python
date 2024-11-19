import random  

def guess_the_number():  
    print("Welcome to 'Guess the Number'!")  
    print("I'm thinking of a number between 1 and 100.")  
    
     
    number_to_guess = random.randint(1, 100)  
    attempts = 0  

    while True:  
        
        guess = input("Enter your guess (or 'exit' to quit): ")  

        if guess.lower() == 'exit':  
            print("Thanks for playing! Goodbye!")  
            break  
        
        try:  
            guess = int(guess)  
            attempts += 1  
        except ValueError:  
            print("Please enter a valid number or 'exit' to quit.")  
            continue  
        
        
        if guess < number_to_guess:  
            print("Too low! Try again.")  
        elif guess > number_to_guess:  
            print("Too high! Try again.")  
        else:  
            print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")  
            break  

if __name__ == "__main__":  
    guess_the_number()