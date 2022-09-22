
roman_numeral = {
    1: 'I',
    2: 'II',
    3: 'III',
    4: 'IV',
    5: 'V',
    6: 'VI',
    7: 'VII',
    8: 'VIII',
    9: 'IX',
    10: 'X'
}

user_input = int(input('Enter number: '))

print(roman_numeral.get(user_input, 'unknown'))