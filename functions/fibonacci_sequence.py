import inspect
import sys

def fibonacci_sequence(sequence_length):
    catch_value_and_type_errors(sequence_length)

    previous_fibonacci_number, current_fibonacci_number = 0, 1
    
    for _ in range(sequence_length - 2):
        previous_fibonacci_number, current_fibonacci_number = current_fibonacci_number, previous_fibonacci_number + current_fibonacci_number
    
    return current_fibonacci_number

def all_previous_fibonacci_sequence_numbers(sequence_length):    
    catch_value_and_type_errors(sequence_length)

    previous_fibonacci_number, current_fibonacci_number = 0, 1
    fibonacci_sequence_numbers = [previous_fibonacci_number, current_fibonacci_number]
    
    for _ in range(sequence_length - 2):
        previous_fibonacci_number, current_fibonacci_number = current_fibonacci_number, previous_fibonacci_number + current_fibonacci_number
        fibonacci_sequence_numbers.append(current_fibonacci_number)

    return fibonacci_sequence_numbers

def catch_value_and_type_errors(sequence_length):
    calling_function_name = inspect.stack()[1][3]

    if type(sequence_length) is not int:
        raise TypeError("In function '" + calling_function_name + "', the 'number_in_sequence' " + 
                        "parameter must be an integer, but got " + str(type(sequence_length)) + " instead.")
    
    if sequence_length == 0:
        raise ValueError("In function '" + calling_function_name + "', the 'number_in_sequence' " + 
                        "parameter cannot be 0, as there are no numbers in an empty sequence.")
    
    if sequence_length < 0:
        raise ValueError("In function '" + calling_function_name + "', the 'number_in_sequence' " + 
                        "parameter cannot be negative, as there are no numbers in a negative sequence.")
    
    if sys.getsizeof(sequence_length) > sys.getsizeof(2147483647):
            raise OverflowError("In function '" + calling_function_name + "', the calculated Fibonacci number " + 
                                "exceeds the maximum size of an integer on this system.")

print(fibonacci_sequence(600000)) #????