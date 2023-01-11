def return_10():
    return 10

def add(num_1,num2):
    return num_1 + num2

def subtract(num_1,num_2):
    return num_1 - num_2

def multiply(num_1,num_2):
    return num_1 * num_2

def divide(num_1,num_2):
    return num_1 / num_2

def length_of_string(string):
    return len(string)

def join_string(string_1,string_2):
    return string_1 +string_2

def add_string_as_number(string_1,string_2):
    return int(string_1) + int(string_2)

def number_to_full_month_name(month):
    year =['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    return year[month-1]

def number_to_short_month_name(month):
    short = ''
    full = number_to_full_month_name(month)
    for i in range(3):
        short += full[i]
    return short

def volume_of_cube(length):
    return length * length * length

def reverse_string(word):
    return word[len(word)-1::-1]

def fahrenheit_to_celsius(faren):
    return (faren-32)*5/9
