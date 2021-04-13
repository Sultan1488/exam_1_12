# def func(num_1, num_2, num_3):
#     for month in range(num_2):
#         num_1 = num_3 / 100 / 12 * num_1 + num_1
#         amount_for_the_year = f'Amount for the year: {num_1}'
#     return amount_for_the_year
# deposit = int(input('Enter the deposit amount: '))
# months = int(input('Enter the number of months: '))
# annual_percentage = int(input('Enter the annual percentage: '))
# print(func(deposit, months, annual_percentage))

# while i == desired_amount:

def func(num_1, num_2, num_3):
    months = 0
    while months != 0:
        while num_1 == num_2:
    # for month in range(num_2):
            num_1 = num_3 / 100 / 12 * num_1 + num_1
            amount_for_the_year = f'Amount for the year: {num_1}'
        months += 1
    return months
deposit = int(input('Enter the deposit amount: '))
desired_amount = int(input('Enter the desired amount: '))
annual_percentage = int(input('Enter the annual percentage: '))
print(func(deposit, desired_amount, annual_percentage))


