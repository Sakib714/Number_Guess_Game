from random import randint


"""
in this guess game you have to select how many times you want to play. This programme will excecute a new secret number each time when you guess a number.

This programme also prints your score
"""

# Greetings

print('Welcome to Guess Game Part- 3 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('Your Guess Range Is (1-10)\n')

spider = int(input('How many time do you want to play: '))

score = 0
for i in range(spider):
    user_guess = int(input("Enter Your Guess Number: "))
    secret_number = randint(1, 10)
    
    if user_guess == secret_number:
        score+=1
        print('You Guessed It! 🎉🎉🎉')
        print(f'The Number Was {secret_number}')
        
        
    elif user_guess > secret_number or user_guess < secret_number:
        print(f'Wrong Answer! Secret Number Was {secret_number}')
        
    else:
        print('Something wente wrong!')
        
        
print('Your Score is ', score)

# Parcentage Calculation

percentage = (score/10)*100

print('You Corrected ',percentage, '%')