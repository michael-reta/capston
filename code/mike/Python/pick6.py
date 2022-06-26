import random


def pick6():
    winning_nums = []
    for i in range(6):
        winning_nums.append(random.randint(1,99))
    print(f"Winning Numbers: {winning_nums}")
    return winning_nums

def play():
    winning_nums = pick6()
    balance = 0
    ticket_nums = []

    for i in range(100000):
        ticket_nums.append(random.randint(1,99))
    print(f"Ticket: {ticket_nums}")
    
    ticket_nums = pick6()
    matches = 0
    balance -= 2
    payout = calculate_payout (winning_nums, ticket_nums)
    balance += payout
    for i in range(len(ticket_nums)):
        if ticket_nums[i] == winning_nums[i]:
            matches.append(ticket_nums[i])
    print("Matches: {matches}")
    
    print('Balance:', balance)

def calculate_payout(winning_nums, ticket_nums):
    payout = [0, 4, 7, 100, 50000, 1000000, 25000000]
    matches = 0
    for num in range(len(ticket_nums)):
        if winning_nums[num] == ticket_nums[num]:
            matches += 1
    return payout[matches]



def play():
    winning_nums = pick6()
    balance = 0
    for i in range(100000):
        ticket_nums = pick6()
        balance -= 2
        payout = calculate_payout (winning_nums, ticket_nums)
        balance += payout
    print('Balance:', balance)
