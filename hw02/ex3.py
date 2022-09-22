
def _main_():
    user_enter = int(input('Enter the number'))
    week_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

    if user_enter < 1 or user_enter > 7:
        print('Please enter from 1 to 7')
    else:
        print(week_days[user_enter - 1])

_main_()
