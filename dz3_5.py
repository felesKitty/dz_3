
numbers = 0
try:
    while numbers != 'Q':
        for N in map(int, input('For exit type "Q" \n '
                                'Enter numbers with spaces ').split()):
            numbers += N
        print(numbers)
except ValueError:
    print(numbers)
