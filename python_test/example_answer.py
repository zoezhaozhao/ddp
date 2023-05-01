# Temperature Converter Function

"""
Approach:
I first familiarised myself with the formulas for converting temperatures from Fahrenheit to Celsius and vice versa.

To convert from Fahrenheit to Celsius, we can use the formula C = (F - 32) * (5/9).
To convert from Celsius to Fahrenheit, we can use the formula F = C * (9/5) + 32.

Initially, I implemented these formulas directly within the function, but I encountered an error when a non-numeric value was passed as the temperature. 
To handle this, I introduced a while loop to continuously prompt the user for a numeric temperature until a valid number is provided.

Next, I included a check to ensure the provided scale was either 'F' or 'C', returning an error message if not.

I initially had some trouble with the order of operations in my formulas, but I realised that I needed to use parentheses to ensure the operations were performed in the correct order.

After finalising the function, I tested it with a variety of inputs to ensure that it returned the correct results. 
I noticed that the function sometimes returned long decimal numbers, so I decided to round the result to two decimal places for a cleaner output.
"""

# Resources used:
# - Python Documentation: https://docs.python.org/3/tutorial/floatingpoint.html
# - W3Schools Python While Loops: https://www.w3schools.com/python/python_while_loops.asp
# - Temperature Conversion Formulas: https://www.mathsisfun.com/temperature-conversion.html


def temp_converter():
    while True:
        temp = input("Please enter a temperature: ")
        if temp.replace(".", "", 1).lstrip("-").isdigit():
            temp = float(temp)
            break
        else:
            print("Temperature must be a number. Please try again.")

    scale = input("Please enter the scale ('C' for Celsius or 'F' for Fahrenheit): ")

    if scale.upper() == "C":
        return round(temp * 9 / 5 + 32, 2)
    elif scale.upper() == "F":
        return round((temp - 32) * 5 / 9, 2)
    else:
        return "Error: Scale must be either 'C' for Celsius or 'F' for Fahrenheit."


# Test the function
print(temp_converter())  # Expected output depends on user input
