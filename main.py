from calendar import c
import random

# global constant
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "$": 2,
    "&": 4,
    "#": 6,
    "@": 8
}

symbol_value = {
    "$": 6,
    "&": 4,
    "#": 3,
    "@": 2
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def get_slot_spin(rows, cols, symbols):
    all_symbols = []
    # These for loops populate the list. Can we think of a better way to do this without a nested for loop?
    # items will give me the key and the value for each item in dictionary
    for symbol, symbol_count in symbols.items():
        # _ is anonymous. meaning we wont be needing that variable for anything.
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):  # controls how many columns will be populated with symbols
        column = []
        # this ensures we are not editing the same list in memory.
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    # we need to transpose the matrix here.
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()  # empty print just brings us to the next line


# I feel like there is a better way to confirm the input here.
def deposit():
    while True:
        amount = input("How much would you like to deposit? $:")
        if amount.isdigit():  # .isdigit confirms that the number is valid, not float, or negative, or string
            amount = int(amount)  # converts the amount to a integer
            if amount > 0:  # if amount is greater than zero, our input is valid.
                break
            else:
                print("Amount must be greater than zero.")
        else:
            print("please enter a number")

    return amount


def get_number_of_lines():
    while True:
        lines = input(
            "Enter the number of lines to bet on: (1- " + str(MAX_LINES) + "). > ")
        if lines.isdigit():  # .isdigit confirms that the number is valid, not float, or negative, or string
            lines = int(lines)  # converts the lines to a integer
            if 1 <= lines <= MAX_LINES:  # if lines is greater than zero, our input is valid.
                break
            else:
                print("Please enter a valid number of lines.")
        else:
            print("please enter a number")

    return lines


def get_bet():
    while True:
        amount = input("How much would you like to bet on each line? $: ")
        if amount.isdigit():  # .isdigit confirms that the number is valid, not float, or negative, or string
            amount = int(amount)  # converts the amount to a integer
            # if amount is greater than zero, our input is valid.
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} and ${MAX_BET}")
        else:
            print("please enter a number")

    return amount


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You dont have enough money to bet {total_bet}. Your current balance is ${balance}")
        else:
            break

    print(f"you are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}.")

    slots = get_slot_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on: ", *winning_lines) # unpacks the lines list into this print
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"current balance is ${balance}")
        answer = input("Press enter to play. (q to quit)")
        if answer == 'q':
            break
        balance += spin(balance)

    print(f"you left with ${balance}")

main()