def odd_even():
    print("Check whether a number is Odd or Even.")
    num1 = input("Enter any number: ")
    num2 = int(num1) % 2
    if num2 == 0:
        print(f'Number {num1} is an even number.')
        Que = input("Continue ( Y/n ): ")
        Que.lower()
        if Que == "y":
            odd_even()

        else:
            exit(0)
    elif num1 == 0:
        print(f'Number 0 is neither odd nor even.')
        Que = input("Continue ( Y/n ): ")
        Que.lower()
        if Que == "y":
            odd_even()

        else:
            exit(0)
    else:
        print(f'Number {num1} is an odd number.')
        Que = input("Continue ( Y/n ): ")
        Que.lower()
        if Que == "y":
            odd_even()

        else:
            exit(0)

odd_even()
