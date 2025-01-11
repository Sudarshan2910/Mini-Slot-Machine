import random
MAX_LINES=3
MAX_BET=100
MIN_BET=1

ROWS=3
COLS=3

symbols_count={
    "A":2,
    "B":4,
    "C":6,
    "D":8
}
symbols_value={
    "A":5,
    "B":4,
    "C":3,
    "D":2
}

def get_slot_machine_spin(rows,cols,symbols):
    all_symbols=[]
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns=[]
    for _ in range(cols):
        column=[]
        current_symbol=all_symbols[:]
        for _ in range(rows):
            value=random.choice(current_symbol)
            current_symbol.remove(value)
            column.append(value)
        
        columns.append(column)
    print(columns)
    return columns
    
def print_slot_machine_spin(columns):
    for row in range(len(columns[0])):
        # print(len(columns[0]))
        for i,column in enumerate(columns):
            # print(i)
            if i!=len(columns)-1:
                print(column[row],end=" | ")
            else:
                print(column[row],end="")
        print()

def check_winnings(columns,lines,bet,values):
    winnings=0
    winning_lines=[]
    for line in range(lines):
        symbol=columns[0][line]
        for column in columns:
            symbol_to_check=column[line]
            if symbol!=symbol_to_check:
                break
        else:
            winnings+=values[symbol]*bet
            winning_lines.append(line+1)
    return winnings, winning_lines
def deposit():
    while(True):
        amount=input("Enter amount you want to deposit in $ ")

        if amount.isdigit():
            amount=int(amount)
            if amount >0:
                break
            else :
                print("amount must be greater than zero")
        else:
            print("Enter valid amount in numbers")
        
    return amount


def get_number_of_line():
    while True:
        lines=input("Enter the numbers of lines to bet on (1-"+str(MAX_LINES)+")? ")
        
        if lines.isdigit():
            lines=int(lines)
            if lines >0 and lines<=MAX_LINES:
                break
            else:
                print("please enter a valid number of lines")
        else:
            print("Enter a number")
        
    return lines

def get_bet():
    while(True):
        amount=input("Enter amount you want to bet on each line in $ ")

        if amount.isdigit():
            amount=int(amount)
            if MIN_BET<=amount<=MAX_BET:
                break
            else :
                print(f"amount must be in range of {MIN_BET} - {MAX_BET} ")
        else:
            print("Enter valid amount in numbers")
        
    return amount
def spin(balance):
    lines=get_number_of_line()
    
    while True:
        bet=get_bet()
        total_bet=bet*lines
        if total_bet>balance:
            print("Bet amount exceeds your current balance! please enter a less bet amount ")
        else:
            break
    
    print(f"You placed ${bet} on each line which sums up and equals to ${total_bet}")
    slots=get_slot_machine_spin(ROWS,COLS,symbols_count)
    print_slot_machine_spin(slots)
    winning , winning_lines=check_winnings(slots,lines,bet,symbols_value)
    print(f"Your winning is ${winning}")
    print(f"lines you won on are: ",*winning_lines)
    return winning - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer=input("Press enter to play (q to quit)")

        if answer=='q':
            break
        balance+=spin(balance)

    print(f"you left with ${balance}")
main()
