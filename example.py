# Import the math module for mathematical functions and constants
import math

# Function to calculate the area of a circle
def calculate_area(radius):
    """
    Calculate the area of a circle given its radius.
    Formula: Area = π * radius^2
    """
    return math.pi * radius**2

# Main function to take user input and display the result
def main():
    # Ask the user to enter the radius of the circle
    radius = float(input("Enter the radius of the circle: "))
    
    # Ensure the radius is non-negative
    if radius < 0:
        print("Radius cannot be negative. Please enter a valid radius.")
        return
    
    # Call the calculate_area function
    area = calculate_area(radius)
    
    # Display the result
    print(f"The area of the circle with radius {radius} is {area:.2f}")

# Execute the main function
if __name__ == "__main__":
    main()