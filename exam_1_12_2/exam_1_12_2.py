def func(num_1, num_2, num_3):
    months = 0
    while num_1 < num_2:
        num_1 = num_3 / 100 / 12 * num_1 + num_1
        months += 1
        number_of_months = f'The number of months required to accumulate the desired amount: {months}'
    return number_of_months
deposit = int(input('Enter the deposit amount: '))
desired_amount = int(input('Enter the desired amount: '))
annual_percentage = int(input('Enter the annual percentage: '))
print(func(deposit, desired_amount, annual_percentage))
