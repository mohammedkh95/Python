contacts = []

while True:
    print('-- Contact book --')
    print('-- Please dial a number next to the desired option to proceed.\n')
    print('1- Add contacts')
    print('2- View all contacts')
    print('3- Delete contact list')
    print('4- Other')

    user_input = input('Please select an option: \n\n')

    if user_input == '1':
        while True:
            print('-- Add contact --')
            name = input('Please enter full name: ')
            if not name.strip():
                print('Name field cannot be empty')
                continue
            try:
                phone = int(input('Please enter phone: '))
                contact = {
                    'name': name,
                    'phone': phone
                }
                contacts.append(contact)
                print(f'{contact} has been saved to the list!')
                add_another = input(
                    'Would you like to add another contact? (y/n)')

                if add_another.lower() == 'y':
                    continue
                else:
                    print('Exiting...')
                    break
            except ValueError:
                print('Only numerical data is allowed.')
                continue

    elif user_input == '2':
        print('-- View contact list --')
        while True:
            if len(contacts) != 0:
                print(contacts)
                break

            elif len(contacts) == 0:
                print('Contact list is empty!')
                print('Please add a contact to see full list')
                print('\n')
                break

    elif user_input == '3':
        print('-- Delete Contact list --')
        delete = input(
            'This will delete the entire list. Are you sure? (y/n) ')

        while True:
            if delete.lower() == 'y':
                contacts.clear()
                print('Contact list has been deleted')
                break
            elif delete.lower() == 'n':
                print('Exiting...')
                break

    elif user_input.lower() == '4':
        print('Option not currently available')

    else:
        print('Goodbye!')
        break
