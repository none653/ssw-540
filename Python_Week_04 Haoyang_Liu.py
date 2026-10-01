def guess_my_number():
    
    print("Please think of a number between 0 and 50.")
    print("I will try to guess it! Answer with 'higher', 'lower', or 'correct'.")
    
    low = 0       
    high = 50     
    attempts = 0  
    
    while True:
        
        guess = (low + high) // 2
        attempts += 1
        
        
        print(f"My guess is: {guess}")
        user_feedback = input("Is your number higher, lower, or correct? ").strip().lower()
        
        if user_feedback == "correct":
            
            print(f"Success! I guessed your number {guess} in {attempts} attempts.")
            break
        elif user_feedback == "higher":
           
            low = guess + 1
        elif user_feedback == "lower":
           
            high = guess - 1
        else:
           
            print("Invalid input. Please type 'higher', 'lower', or 'correct'.")
            attempts -= 1


guess_my_number()
