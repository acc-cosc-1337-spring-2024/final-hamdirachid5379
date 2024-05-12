#write functions here, don't add input('') statements here!

#Create a multiplication lists:

from ast import main
#from random import choice


def create_multiplication_table():
    return list
    table = []
    for i in range(1, 6):
        row = [i * j for j in range(1, 11)]
    table.append(row)
    return table

def display_multiplication_table(table):
    for row in table:
        print(" ".join(map(str, row)))

def run():
    numbers = [
        [i for i in range(1, 11)],
        [2 * i for i in range(1, 11)],
        [3 * i for i in range(1, 11)],
        [4 * i for i in range(1, 11)],
        [5 * i for i in range(1, 11)]
    ]

    # Display the multiplication table
    display_multiplication_table(numbers)

    

def main():
    while True:
        # Step 1: Call the function to create and display the multiplication table
        multiplication_table = create_multiplication_table()
        display_multiplication_table(multiplication_table)

        # Step 4: Ask the user if they want to continue
        choice = input("Do you want to continue? (yes/no): ").lower()
        if choice != 'yes':
            break


# Call the main function to start the program
if __name__ == "__main__":
    run()
