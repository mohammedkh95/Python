curr_acc = 0
while True:
    print('Welcome to GrassBank ATM')
    choice = input(
        "Please choose an option:\n- Current\n- Savings\n- Deposit\n\nYour choice: ")
    if choice == 'Deposit':
        deposit = input(
            'Would you like to deposit? (Y) to continue), (N) to return to the homescreen?\n\nYour choice: ')
        if deposit.lower() == 'y':
            try:
                deposit_sum = int(
                    input('How much would you like to deposit? '))
                curr_acc += deposit_sum
                print(
                    f'You deposited {deposit_sum}. Your current balance is {curr_acc} \n')
                transaction = input(
                    'Thank you for depsoting. Would you like to perform a transactions? (y/n)')
                if transaction.lower() == 'y':
                    continue
                else:
                    print('Thank you for banking with GrassBank!')
                    break
            except ValueError:
                print("Please input numerical values only")
        elif len(deposit) == 0:
            print("Deposit cancelled! Returning to main screen\n")
            break

    elif choice == 'Savings' or choice == 'Current':
        print(f' - {choice} -')
        while True:
            if curr_acc == 0:
                print('Your bank balance is empty')
                print('Please deposit funds into your account to perform a transaction')
                break
            withdraw = input(
                "How much would you like to withdraw? \n- 50 \n- 100 \n- 150 \n- 200 \n\nAmount:")

            try:
                withdraw = int(withdraw)
                if withdraw in [50, 100, 150, 200]:
                    if withdraw < curr_acc:
                        curr_acc -= withdraw
                        print(
                            f"You withdrew {withdraw}. Your current balnce is {curr_acc}")
                        withdraw_2 = input(
                            'Would you like to perform another transaction? (y/n)')
                        if withdraw_2.lower() == 'y':
                            continue
                        else:
                            print('Transction complete!')
                            print('Thank you for banking with GrassBank!')
                            break
                    elif withdraw == curr_acc:
                        print("Error! You cannot empty your account completely.")
                    elif withdraw > curr_acc:
                        print(
                            'You do not have sufficient funds in your account for this transaction')
                    else:
                        print('Invalid withdrawal amount.')
                        break
            except ValueError:
                print('Please type in a valid amount')
