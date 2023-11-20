start_range = int(input("Enter the starting range (four-digit number): "))
end_range = int(input("Enter the ending range (four-digit number): "))
if start_range < 1000 or end_range > 9999 or start_range > end_range:
    print("Invalid input. Please enter valid four-digit ranges.")
else:
    even_digit_square_numbers = [number for number in range(start_range, end_range + 1)
                                 if all(int(digit) % 2 == 0 for digit in str(number))
                                 and int(number**0.5)**2 == number]

    print("Four-digit numbers with all even digits that are perfect squares:")
    print(even_digit_square_numbers)
