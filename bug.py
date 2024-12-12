def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    total = sum(numbers)
    average = total / len(numbers)
    return average

#Example of the bug
my_list = []
result = calculate_average(my_list) 
print(result) #Output 0

my_list = [10,20,30]
result = calculate_average(my_list) 
print(result) #Output 20.0