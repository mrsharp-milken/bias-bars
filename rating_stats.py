"""
File: rating_stats.py
----------------------
This file defines a program that allows a user to calculate
baseline summary statistics about a datafile of professor review
data. 
"""


def calculate_rating_stats(filename):
    """
    This function analyzes the professor review data in the given
    file to calculate the percentage of reviews for both men and
    women that fall in the "high rating" bucket, which is a numerical
    rating that is greater than 3.5.

    The resulting information is printed to the console.
    """
    # Open the file and read all lines
    with open(filename, 'r') as file:
        # Skip the header
        

        # Initialize counters
        
        
        # Loop through each line in the file
        for line in file:
            # This print is just to show you this code works
            print(line)

            # Count the ratings
            
        
        # Calculate percentages
        
        # Print the results
        

def main():
    # Ask the user to input the name of a file
    filename = input("Which data file would you like to load? ")

    # Calculate review distribution statistics by gender for
    # that file. This function should print out the results of
    # the analysis to the console.
    calculate_rating_stats(filename)


if __name__ == '__main__':
    main()
