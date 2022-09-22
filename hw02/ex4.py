
def calculate_area():
    width = int(input('Enter width: '))
    height = int(input('Enter height: '))

    return width * height

rectangle1 = calculate_area()
rectangle2 = calculate_area()

if rectangle1 > rectangle2:
    print('rectangle1 is greater than rectangle2')
elif rectangle1 < rectangle2:
    print('rectangle2 is greater than rectangle1')
else:
    print('Both are the same')
