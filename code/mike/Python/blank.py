"""
Have the computer play pick6 many times and determine net balance.
Initially the program will pick 6 random numbers as the 'winner'. Then try playing pick6 100,000 times,
with the ticket cost and payoff below. A ticket contains 6 numbers, 1 to 99, and the number of matches
between the ticket and the winning numbers determines the payoff. Order matters, if the winning numbers
are [5, 10] and your ticket numbers are [10, 5] you have 0 matches. If the winning numbers are [5, 10, 2]
and your ticket numbers are [10, 5, 2], you have 1 match. Calculate your net winnings
(the sum of all expenses and earnings).
- a ticket costs $2
- if 1 number matches, you win $4
- if 2 numbers match, you win $7
- if 3 numbers match, you win $100
- if 4 numbers match, you win $50,000
- if 5 numbers match, you win $1,000,000
- if 6 numbers match, you win $25,000,000
One function you might write is pick6() which will generate a list of 6 random numbers, which can then be
used for both the winning numbers and tickets. Another function could be num_matches(winning, ticket)
which returns the number of matches between the winning numbers and the ticket.
Steps
1. Generate a list of 6 random numbers representing the winning tickets
2. Start your balance at 0
3. Loop 100,000 times, for each loop:
4. Generate a list of 6 random numbers representing the ticket
5. Subtract 2 from your balance (you bought a ticket)
6. Find how many numbers match
7. Add to your balance the winnings from your matches
8. After the loop, print the final balance
Version 2
The ROI (return on investment) is defined as (earnings - expenses)/expenses.
Calculate your ROI, print it out along with your earnings and expenses.
"""

# import random


# def pick6():
#     winning_nums = []
#     for i in range(6):
#         winning_nums.append(random.randint(1,99))
#         print(f"Winning Numbers: {winning_nums}")
    # return winning_nums

# def play_lotto():
#     # winning_nums = pick6()
#     # balance = 0
    

#     for i in range(100000):
#         ticket_nums = []
#         for i in range(6):
#             ticket_nums.append(random.randint(1,99))
#     print(f"Ticket: {ticket_nums}")
#     return ticket_nums

import random

winning = []


def pick6():

    for i in range(6):
        random_num = random.randint(1, 99)
        winning.append(random_num)
    print(f"Winning Numbers: {winning}")
    return winning


def num_matches():
    balance = 0
    expenses = 0
    earnings = 0

    for i in range(1000):
        ticket = []
        for j in range(6):
            random_nums = random.randint(1, 99)
            ticket.append(random_nums)
        print(f"Ticket: {ticket}")
        balance -= 2
        expenses -= 2
        matches = []
        for i in range(len(ticket)):
            if ticket[i] == winning[i]:
                matches.append(ticket[i])
                print(f"Matches: {matches}")
                if len(matches) == 1:
                    balance += 4
                    earnings += 4
                elif len(matches) == 2:
                    balance += 7
                    earnings += 7
                elif len(matches) == 3:
                    balance += 100
                    earnings += 100
                elif len(matches) == 4:
                    balance += 50000
                    earnings += 50000
                elif len(matches) == 5:
                    balance += 1000000
                    earnings += 1000000
                elif len(matches) == 6:
                    balance += 25000000
                    earnings += 25000000