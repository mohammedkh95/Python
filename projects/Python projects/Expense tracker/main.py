Tracker = []


def add_tracker():
    while True:
        print('-- Add a tracker(s) --')

        # Amount
        amount = input('Total amount: \n')
        if not amount.isdigit():
            print('Amount must be numerical')
            continue

        # Description
        while True:
            description = input('Income (1) / Expense (2): ')
            if description == '1':
                word = 'Income'
                break
            elif description == '2':
                word = 'Expense'
                break
            else:
                print('Invalid input')
                print('Choose 1 or 2 to categorise this expense')
                continue

        # Category
        while True:
            print('Pick a category')
            print('1- Food')
            print('2- Rent')
            print('3- Salary')
            print('4- Misc.')

            category = input('Category type: ')

            if category == '1':
                cat_type = 'Food'
                break
            elif category == '2':
                cat_type = 'Rent'
                break
            elif category == '3':
                cat_type = 'Salary'
                break
            elif category == '4':
                cat_type = 'Misc'
                break
            else:
                print('Invalid input')
                print('Please choose a number between 1 & 4')

        # Store them into a dictionary
        event = {
            'amount': amount,
            'description': word,
            'category': cat_type
        }

        # Append to dictionary
        Tracker.append(event)
        print('Tracker added to list')
        break


def view_tracker():
    print('-- View tracker(s) --')

    if not Tracker:
        print('Your tracker list is empty.')
        choice = input('Would you like to add an expense? (y/n): ')
        if choice.lower() == 'y':
            add_tracker()
        return

    # Print each tracker item nicely
    for i, t in enumerate(Tracker, start=1):
        print(f"{i}. {t['amount']} - {t['description']} - {t['category']}")
        print("\n")


def delete_tracker():
    print('-- Delete tracker list --')

    if not Tracker:
        print('Your tracker list is empty')
        return

    for i, t in enumerate(Tracker, start=1):
        print(
            f"{i}. {t['amount']} - {t['description']} - {t['category']}")

        print('\nAre you sure you want to delete everything?(y/n) ')
        del_track = input('Choice: ')

        if del_track.lower() == 'y':
            Tracker.clear()
            print('Tracker list deleted')
        else:
            print('Tracker list not deleted')


def personal_expense_tracker():
    while True:

        print('// Personal Expense Tracker \\\\')
        print('Please select an option from the following')
        print('1- Add tracker')
        print('2- View tracker')
        print('3- Delete tracker')

        user_input = input('Choice: ')

        if user_input == '1':
            add_tracker()
        elif user_input == '2':
            view_tracker()
        elif user_input == '3':
            delete_tracker()
        else:
            print('Good bye')


personal_expense_tracker()
