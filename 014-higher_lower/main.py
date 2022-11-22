import random
from art import logo, vs
from game_data import data
from replit import clear

def random_choice():
    return random.choice(data)

def format_data(account):
    name = account['name']
    description = account['description']
    country = account['country']
    return f"{name}, a {description}, from {country}."

def compare_choices(num_a, num_b):
    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    if num_a > num_b:
        correct_answer = 'a'
    else:
        correct_answer = 'b'
        
    if user_choice == correct_answer:
        return True
    else:
        return False
        
game_count = 0
is_game_finished = False

choice_a = random_choice()
print(logo)

while not is_game_finished:
    choice_b = random_choice()
    if choice_a == choice_b:
        choice_b = random_choice()

    print(f"Compare A: {format_data(choice_a)}")
    print(vs)
    print(f"Compare B: {format_data(choice_b)}")
    
    correct = compare_choices(choice_a['follower_count'], choice_b['follower_count'])
    if correct:
        game_count += 1
        clear()
        choice_a = choice_b
        print(logo)
        print(f"You're right! Current score: {game_count}.")
    else:
        is_game_finished = True
        clear()
        print(logo)
        print(f"Sorry, that's wrong. Final score: {game_count}")
    

# Display Logo
# set random for A and B

# Show Compare A: Name, Job, from where
# show VS logo
# print - Against B: name, job, from where
# Ask Who has more followers? Type 'A' or 'B':
# Take input and see if correct

# if correct print You're right! Current score: 1.
# print correct ansewr to A
# random B

# if wrong - end the game Sorry, that's wrong. Final score: 4

