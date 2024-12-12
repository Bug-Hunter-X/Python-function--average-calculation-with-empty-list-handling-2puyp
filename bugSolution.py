def calculate_average(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    total = sum(numbers)
    average = total / len(numbers)
    return average

#Example of the bug
try:
    my_list = []
    result = calculate_average(my_list) 
    print(result) 
except ValueError as e:
    print("Error:", e)

try:
    my_list = [10,20,30]
    result = calculate_average(my_list) 
    print(result) #Output 20.0
except ValueError as e:
    print("Error:",e) 