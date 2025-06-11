task_list = []


def create_task():
    print('\n -- Add task --')
    t_name = input('\n Task name: ')
    t_desc = input('\n Task description: ')
    t_priority = input('\n Task priority: ')

    tasks = {
        'name': t_name,
        'description': t_desc,
        'priority': t_priority
    }

    task_list.append(tasks)

    for i, t in enumerate(task_list, start=1):
        print(f"""{i}. Task name: {t['name']}
    ↳ Description: {t['description']}
    ↳ Priority: {t['priority']}\n""")

    add_task = input('Would you like to add another task? (y/n) ')
    if not add_task:
        print('Exiting to main screen... \n')
    elif add_task.lower() == 'y':
        create_task()
    else:
        print('Exiting to main screen...\n')


def manage_task():
    print('\n -- Task manager -- \n')

    print('\n Please select an option to proceed')
    print('1. View task(s)')
    print('2. Update task')
    print('3. Delete task \n')

    update_choice = input()

    if not task_list:
        print('ERROR! Your task list is empty')
        update_input = input('Would you like to a task? (y/n) \n')
        if update_input.lower() == 'y':
            create_task()
            return
        elif update_input.lower() == 'n':
            print('You must have a task to view (1), update (2) or delete (3)')
            print('Exiting to main screen...\n')

    elif update_choice.lower() == '1':
        print('\n-- Current task list --')

        for i, t in enumerate(task_list, start=1):
            print(f"""{i}. Task name: {t['name']}
        ↳ Description: {t['description']}
        ↳ Priority: {t['priority']}\n""")

    elif update_choice.lower() == '2':
        print('-- Update Trackers --')
        print("\n Please select the index number to update a tracker\n")

        for i, t in enumerate(task_list, start=1):
            print(f"""{i}. Task name: {t['name']}
        ↳ Description: {t['description']}
        ↳ Priority: {t['priority']}\n""")

        up_index = int(input('Select index to update: '))

        if 0 <= up_index < len(task_list):
            print(f'\n {up_index}, {task_list[up_index]}')
            update_name = input('Update task name: ')
            update_desc = input('Update description: ')
            update_pritotiy = input('Update priority: ')

            task_list[up_index]['name'] = update_name
            task_list[up_index]['description'] = update_desc
            task_list[up_index]['priority'] = update_pritotiy

            print(f'Task list for index "{up_index}" has been updated')
        else:
            print('Please update all fields')

    elif update_choice.lower() == '3':
        delete_task()


def delete_task():
    print('\n-- Delete task --\n')

    print("\n Please select the index number to update a tracker\n")

    for i, t in enumerate(task_list, start=1):
        print(f"""{i}. Task name: {t['name']}
            ↳ Description: {t['description']}
            ↳ Priority: {t['priority']}\n""")

    del_index = int(input('Select an index to delete: '))

    if 0 <= del_index < len(task_list):
        task_list.pop(del_index)

        print(f'Task list index {del_index} has been deleted')


def simple_task_manager():
    while True:

        print('// Simple Task Manager \\\\')
        print('Please select an option from the following')
        print('1- Add a task(s)')
        print('2- Manage task(s)')
        print('3- Delete task(s)')

        user_input = input('Choice: ')
        if user_input == '1':
            create_task()
        elif user_input == '2':
            manage_task()
        elif user_input == '3':
            delete_task()
        else:
            print('Please choose one of the above')
        continue


simple_task_manager()


# Clean version with fixes
#
# task_list = []
#
#
# def create_task():
#    print('\n-- Add Task --')
#    while True:
#        t_name = input('Task name: ')
#        t_desc = input('Task description: ')
#        t_priority = input('Task priority: ')
#
#        task = {
#            'name': t_name,
#            'description': t_desc,
#            'priority': t_priority
#        }
#
#        task_list.append(task)
#
#        print('\n-- Current Task List --')
#        display_tasks()
#
#        add_another = input('Would you like to add another task? (y/n): ')
#        if add_another.lower() != 'y':
#            print('Exiting to main screen...\n')
#            break
#
#
# def display_tasks():
#    if not task_list:
#        print('No tasks available.\n')
#        return
#
#    for i, t in enumerate(task_list, start=1):
#        print(f"""{i}. Task name: {t['name']}
#   ↳ Description: {t['description']}
#   ↳ Priority: {t['priority']}\n""")
#
#
# def manage_task():
#    if not task_list:
#        print('ERROR! Your task list is empty.\n')
#        add_task = input('Would you like to add a task? (y/n): ')
#        if add_task.lower() == 'y':
#            create_task()
#        else:
#            print('Returning to main menu...\n')
#        return
#
#    print('\n-- Task Manager --')
#    print('1. View tasks')
#    print('2. Update task')
#    print('3. Delete task')
#
#    choice = input('Choose an option: ')
#
#    if choice == '1':
#        print('\n-- Current Task List --')
#        display_tasks()
#
#    elif choice == '2':
#        print('\n-- Update Task --')
#        display_tasks()
#        try:
#            up_index = int(input('Enter task number to update: ')) - 1
#            if 0 <= up_index < len(task_list):
#                update_name = input('New task name: ')
#                update_desc = input('New description: ')
#                update_priority = input('New priority: ')
#
#                task_list[up_index]['name'] = update_name
#                task_list[up_index]['description'] = update_desc
#                task_list[up_index]['priority'] = update_priority
#
#                print('Task updated successfully.\n')
#            else:
#                print('Invalid task number.\n')
#        except ValueError:
#            print('Please enter a valid number.\n')
#
#    elif choice == '3':
#        delete_task()
#
#
# def delete_task():
#    if not task_list:
#        print('No tasks to delete.\n')
#        return
#
#    print('\n-- Delete Task --')
#    display_tasks()
#    try:
#        del_index = int(input('Enter task number to delete: ')) - 1
#        if 0 <= del_index < len(task_list):
#            deleted_task = task_list.pop(del_index)
#            print(f"Deleted task: {deleted_task['name']}\n")
#        else:
#            print('Invalid task number.\n')
#    except ValueError:
#        print('Please enter a valid number.\n')
#
#
# def simple_task_manager():
#    while True:
#        print('// Simple Task Manager \\\\')
#        print('1 - Add task(s)')
#        print('2 - Manage task(s)')
#        print('3 - Delete task(s)')
#        print('4 - Exit')
#
#        user_input = input('Choice: ')
#        if user_input == '1':
#            create_task()
#        elif user_input == '2':
#            manage_task()
#        elif user_input == '3':
#            delete_task()
#        elif user_input == '4':
#            print('Goodbye!')
#            break
#        else:
#            print('Invalid input. Please choose a valid option.\n')
#
#
# simple_task_manager()
#
