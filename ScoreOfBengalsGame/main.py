# compute the score of the bengals-bills game 
# store the score of each team in a separate int variable
# use the python random number generator to get the 2 random scores
# assume the scores will be between 50 and 0 inclusive

import random
print("I am going to tell you the score of the upcoming Bengals-Bills Game")
bengals = random.randint(0,50)
bills = random.randint(0,50)
print("Bengals score: ", bengals)
print("Bills score: ", bills)
if bengals > bills:
    print("The Bengals won the game")
else:
    print("The Bills won the game") 

# add logic to simulate a coin flip and print the winning team

print("The following are the coin toss results: ")
coinFlipResult = random.randint(0,1)
# == is the test for equality
if coinFlipResult == 1:
    print("Bengals win")
else:
    print("Bills win")
    
# look up the total capacity of highmark stadium: 71608
# assume a pretzel is $13 and 45% of the fans buy a pretzel
# print the total gross profit to 2 decimal places

pretzel = 13 * 71608
profit = pretzel * .45
print("The gross profit from pretzel sales are ", f'{profit:.2f}') # https://bobbyhadz.com/blog/python-print-float-with-2-decimal-places

