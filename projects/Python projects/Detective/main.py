
# Detectives
sherlock = [{'intelligence': 95}, {'intuition': 90}, {'strength': 50}]
nancy = [{'intelligence': 85}, {'intuition': 88}, {'strength': 60}]
batman = [{'intelligence': 90}, {'intuition': 85}, {'strength': 80}]

# Suspects
joker = [{'intelligence': 80}, {'intuition': 75}, {'strength': 60}]
moriarty = [{'intelligence': 92}, {'intuition': 80}, {'strength': 55}]
ghost = [{'intelligence': 70}, {'intuition': 60}, {'strength': 40}]


def detective():
    print('\n-- Choose a Detective --')
    print('Sherlock (s), Nancy (n), Batman (b)')

    while True:
        detective_choice = input().strip().lower()

        if not detective_choice:
            print("Please choose a detective to proceed!")
            continue  # restart the loop

        if detective_choice in ['s', 'sherlock']:
            detective_choice = ('Sherlock', sherlock)
        elif detective_choice in ['n', 'nancy']:
            detective_choice = ('Nancy', nancy)
        elif detective_choice in ['b', 'batman']:
            detective_choice = ('Batman', batman)
        else:
            print('You have not selected a detective')
            continue

        print(f'\n-- {detective_choice[0]} stats --')
        for choice in detective_choice[1]:
            for key, value in choice.items():
                print(f'{key.capitalize()}: {value}')

        # Confirming selection
        while True:
            print(
                f'Confirm detective selection? "{detective_choice[0]}" (y/n)')
            confirm_choice = input().strip().lower()

            if confirm_choice == 'y':
                print(f'Chosen detective: {detective_choice[0]}')
                return detective_choice
            elif confirm_choice == 'n':
                print('Who would you like to choose?')
                print('Sherlock (s), Nancy (n), Batman (b)')
                break
            else:
                print('Please confirm with y/n.')


def villain():
    print('\n-- Choose a Detective --')
    print('Joker (j), Moriarty (m), Ghost (g)')

    while True:
        villain_choice = input().strip().lower()

        if not villain_choice:
            print('Please choose a villain to proceed')
            continue

        if villain_choice in ['j', 'Joker']:
            villain_choice = ('Joker', joker)
        elif villain_choice in ['m', 'Moriarty']:
            villain_choice = ('Moriarty', moriarty)
        elif villain_choice in ['g', 'Ghost']:
            villain_choice = ('Ghost', ghost)
        else:
            print('You have not selected a detective')
            continue

        print(f'\n-- {villain_choice[0]} stats --')
        for stats in villain_choice[1]:
            for key, value in stats.items():
                print(f'{key.capitalize()}: {value}')

        # confirm choice
        while True:
            print(
                f'Confirm villain selection? "{villain_choice[0]}" (y/n)')
            confirm_choice = input().strip().lower()

            if confirm_choice == 'y':
                print(f'Chosen villain: {villain_choice[0]}')
                return villain_choice
            elif confirm_choice == 'n':
                print('Who would you like to choose?')
                print('Joker (j), Moriarty (m), Ghost (g)')
                break
            else:
                print('Please confirm with y/n.')


def fight(selected_hero, selected_villain):
    print('-- Fight! --')
    print(f'{selected_hero[0]} VS. {selected_villain[0]}')

    # comparing hero vs villain stats to see who is the winner
    print('Fight based on which attrbiute?')
    print('\n Intelligence (1), Intuition (2), Strength (3)?\n')

    att_choice = input('Attribute choice: ').strip().lower()

    # logic

    if att_choice in ['1', 'intelligence']:
        stat_index = 0
    elif att_choice in ['2', 'intuition']:
        stat_index = 1
    elif att_choice in ['3', 'strength']:
        stat_index = 2
    else:
        print('Invalid choice')
        return

    stat = list(selected_hero[1][stat_index].keys())[0]

    hero_attribute = selected_hero[1][stat_index][stat]
    villain_attribute = selected_villain[1][stat_index][stat]

    if hero_attribute > villain_attribute:
        print(
            f'Hero has higher {stat} ({hero_attribute} > {villain_attribute})')
    elif hero_attribute < villain_attribute:
        print(
            f'Villain has higher {stat} ({hero_attribute} > {villain_attribute})')
    else:
        print(f'Both have equal {stat} ({hero_attribute})')


def rpg_fight():
    selected_hero = None
    selected_villain = None

    while True:
        print('\n// Hero V. Villain \\\\')
        print('1- View Hero')
        print('2- View Villain')
        print('3- Fight!')
        print('4- Exit')

        fight_choice = input().strip()

        if fight_choice == '1':
            selected_hero = detective()
        elif fight_choice == '2':
            selected_villain = villain()
        elif fight_choice == '3':
            if selected_hero and selected_villain:
                fight(selected_hero, selected_villain)
            else:
                print("Please choose both a hero and a villain before fighting!")
                return rpg_fight()
        elif fight_choice == '4':
            print('Goodbye!')
            break
        else:
            print('Invalid choice, try again.')


rpg_fight()
