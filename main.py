
# global constant
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

# I feel like there is a better way to confirm the input here. 
def deposit():
    while True:
        amount = input("How much would you like to deposit? $:")
        if amount.isdigit(): # .isdigit confirms that the number is valid, not float, or negative, or string
            amount = int(amount) # converts the amount to a integer
            if amount > 0: # if amount is greater than zero, our input is valid. 
                break
            else:
                print("Amount must be greater than zero.")
        else:
            print("please enter a number")

    return amount


def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on: (1- " + str(MAX_LINES) + "). > ")
        if lines.isdigit(): # .isdigit confirms that the number is valid, not float, or negative, or string
            lines = int(lines) # converts the lines to a integer
            if 1 <= lines <= MAX_LINES: # if lines is greater than zero, our input is valid. 
                break
            else:
                print("Please enter a valid number of lines.")
        else:
            print("please enter a number")

    return lines


def get_bet():
    while True:
        amount = input("How much would you like to bet on each line? $: ")
        if amount.isdigit(): # .isdigit confirms that the number is valid, not float, or negative, or string
            amount = int(amount) # converts the amount to a integer
            if MIN_BET <= amount <= MAX_BET: # if amount is greater than zero, our input is valid. 
                break
            else:
                print(f"Amount must be between ${MIN_BET} and ${MAX_BET}")
        else:
            print("please enter a number")

    return amount


def main():
    balance = deposit()
    lines = get_number_of_lines()
    bet = get_bet()
    total_bet = bet * lines
    print(f"you are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}.")

    print(balance, lines, bet)

main()
