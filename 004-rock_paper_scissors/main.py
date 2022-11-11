rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

choice = int(input("What do you chooose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

cpu = random.randint(0,2)
list = [rock, paper, scissors]

if choice == 0:
  if cpu == 0:
    result = 'You tied'
  elif cpu == 1:
    result = 'You lost'
  else:
    result = 'You won'
elif choice == 1:
  if cpu == 0:
    result = 'You won'
  elif cpu == 1:
    result = 'You tied'
  else:
    result = 'You lost'
else:
  if cpu == 0:
    result = 'You lost'
  elif cpu == 1:
    result = 'You won'
  else:
    result = 'You tied'


print(list[choice])
print('Computer chose:')
print(list[cpu])
print(result)
