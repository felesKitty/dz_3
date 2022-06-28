
def division(numb_1, numb_2):
    try:
        numb_1, numb_2 = int(numb_1), int(numb_2)
        division_n = numb_1 / numb_2
    except (ValueError, ZeroDivisionError):
        return 'You have an error'
    return (division_n)

print(division(input('Enter your first number: '),
input('Enter number for division: ')))