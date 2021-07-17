import random

def guess(limit):
    random_num = random.randint(0,limit)
    guess = -1
    tip_num = 1
    while guess != random_num:
        give_tips(limit, tip_num, random_num)
        guess = int(input(f"Guess a number between 0 and {limit}: "))
        tip_num += 1

        if guess != random_num:
            print("Sorry, you guessed wrong.\n")

    print(f"Congrats! You guessed the number correctly!")

def give_tips(limit, ntip, randInt):
    type = random.randint(1,3)

    if type == 1:
        divisor = -1
        while divisor == -1:
            test_n = random.randint(1,randInt)
            if randInt % test_n == 0:
                divisor = test_n
        print(f"Tip #{ntip}: The number is divisible by {divisor}")

    elif type == 2:
        smaller = random.randint(0, randInt-1)
        print(f"Tip #{ntip}: The number is larger than {smaller}")

    else:
        larger = random.randint(randInt+1, limit)
        print(f"Tip #{ntip}: The number is smaller than {larger}")


u_input = int(input("Choose a limit for your random number: "))
guess(u_input)