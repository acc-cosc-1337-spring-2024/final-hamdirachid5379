#write functions here, don't add input('') statements here!
def test_config():
    return True

def main():
    # Ask the user to enter a series of 5 numbers
    numbers = []
    for i in range(5):
        number = float(input(f"Enter number {i+1}: "))
        numbers.append(number)

    # Calculate the lowest number
    lowest = min(numbers)

    # Calculate the highest number
    highest = max(numbers)

    # Calculate the total of the numbers
    total = sum(numbers)

    # Calculate the average of the numbers
    average = total / len(numbers)

    # Display the results
    print(f"series of 5 numbers:{numbers} ")
    print(f"Lowest number: {lowest}")
    print(f"Highest number: {highest}")
    print(f"Total of the numbers: {total}")
    print(f"Average of the numbers: {average}")

if __name__ == "__main__":
    main()
