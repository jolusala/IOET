from utils.file_utils import read_data_file
from utils.calculator import calculate_salary

data = read_data_file('data.txt')

for name, aport in data.items():
    print(f'The amount to pay {name} is: {int(calculate_salary(aport))} USD')