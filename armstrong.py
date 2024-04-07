def is_narcissistic_number(number):
    # Calculate the total number of digits in the number
    num_digits = 0
    temp = number
    while temp > 0:
        num_digits += 1
        temp //= 10
    
    # Initialize sum_of_powers to 0
    sum_of_powers = 0
    
    # Calculate the sum of each digit raised to the power of the total number of digits
    temp = number
    while temp > 0:
        digit = temp % 10
        sum_of_powers += digit ** num_digits
        temp //= 10
    
    # Checkk if the sum of powers is equal to the original number
    return sum_of_powers == number

# Test cases
##print(is_narcissistic_number(153))  # Output: True
print(is_narcissistic_number(27879694893054074471405))  # Output: False
