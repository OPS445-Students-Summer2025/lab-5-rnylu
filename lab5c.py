#!/usr/bin/env python3
# Author ID: rlu22

def add(number1, number2):
    # Add two numbers together, return the result, if error return string 'error: could not add numbers'
    try: # if the string cannot be converted into an integer, the exception will catch the error generated
        sum = int(number1) + int(number2) 
        return sum
    except ValueError:
        return "error: could not add numbers"

def read_file(filename):
    # Read a file, return a list of all lines, if error return string 'error: could not read file'
    try:
        f = open(filename, 'r')
        read_data = f.readlines()
        return read_data
    except FileNotFoundError:
        return "error: could not read file"

if __name__ == '__main__':
    print(add(10,5))                        # works
    print(add('10',5))                      # works
    print(add('abc',5))                     # exception
    print(read_file('seneca2.txt'))         # works
    print(read_file('file10000.txt'))       # exception