from random import randint

def greet():
    print('Welcome To Guess Game Type - 2.\nYou Have To Enter Your Guess Number Range First To Start Playing.')
    
    
num_range = int(input('Enter Your Upper Bound Number: '))

# generate a secret number

secret_number = randint(1, num_range)

# Calling Greet Function
greet()


flag = True
while flag:
    user_guess = int(input('Enter Your Guess Number: '))
    
    if user_guess == secret_number:
        flag = False
        print('You Got it!')
        print(f'The Secret Number Was {secret_number}')
        
    elif user_guess > secret_number:
        print('Try Smaller...')
        
    elif user_guess < secret_number:
        print('Try Bigger...')
        
    else:
        print('Something Went Wrong!')