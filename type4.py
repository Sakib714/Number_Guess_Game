from random import randint


"""
Play Infinite time Guess Game with This Programme. It's A Never Ending Programme Untell Your Computer Die!
"""

print('WElcome To Guess Game Part - 4')
print('Play Infinite time Guess Game with This Programme. It\'s A Never Ending Programme Untell Your Computer Die!')
print('Please Guess A Number Between (1,10)')

while True:
    user_guess = int(input('Enter Your Guess: '))
    secret_number = randint(1,10)
    
    if user_guess == secret_number:
        print('You Guessed It! 🎉🎉🎉')
        
    elif user_guess not in range(1,10):
        print('Guess a number between 1-10')
        
    elif user_guess != secret_number:
        print(f'Wrong Input!\nSecret Number Was {secret_number}\n\n')
        
    else:
        print('Something Went Wront')