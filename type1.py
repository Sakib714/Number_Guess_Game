from random import randint

"""
You Have to select a level first and then try to guess the correct number within your level range.

You have no guess limit but a counter, you can see your total attempts after guessing the correct number!
"""


def greet():
    print('Welcome To Number Guess Game Type 1 || - - - - - - -  - - - - - - - - - -  - - - - - \n')

    print('There Are 3 Levels In This Game, Those Are [ Hard ], [ Medium ] and [ Easy ]\n')
    
    print('Enter > h < for level Hard\nEnter > m < for level Medium\nEnter > e < for level Easy\n')

    print('Level Hard Number Range: 1-1000')
    print('Level Medium Number Range: 1-500')
    print('Level Easy Number Range: 1-100\n')





def select_level():
    game_level = input('Enter Your Level: ').lower()

    if game_level not in ["h", "m", "e"]:
        print('Wrong Input! Please, Enter a valid Level Code...')
        select_level()
    
    return game_level
   
   
    
    
def generate_secret_number(level_code_str):
    
    if level_code_str == "h":
        secret_number = randint(1,1000)
        
        
    elif level_code_str == "m":
        secret_number = randint(1,500)
        
        
    else: 
        secret_number = randint(1,100)
        
    return secret_number


    
    
# Calling greet function
greet()



# Asking level
level = select_level()



# Generating Secret Number
secret_number = generate_secret_number(level)



    
user_guess = 0
counter = 0

while user_guess != secret_number:
    
    
    
    
    if user_guess > secret_number:
        if counter>0:
            print('Try Smaller...')
            
        
    elif user_guess < secret_number:
        if counter>0:
            print('Try Bigger...')
            

    else: 
        print('Something Went Wrong!')
        
        
        
    user_guess = int(input("Enter Your Guess: "))
    counter+=1
    
    

if user_guess == secret_number:
        print(f'You Have Guessed It! The number was {secret_number}\n It Takes you {counter} time to guess the correct answer')
        
        
        