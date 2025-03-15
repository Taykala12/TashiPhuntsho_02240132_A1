import math

def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_sum(start, end):
    """Calculate the sum of all prime numbers in a given range."""
    return sum(num for num in range(start, end + 1) if is_prime(num))

def length_converter(value, direction):
    """Convert length between meters and feet."""
    if direction.upper() == 'M':
        return round(value * 3.28084, 2)  # Meters to Feet
    elif direction.upper() == 'F':
        return round(value / 3.28084, 2)  # Feet to Meters
    else:
        raise ValueError("Invalid direction. Use 'M' for meters to feet or 'F' for feet to meters.")

def consonant_count(text):
    """Count the number of consonants in a given string."""
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    return sum(1 for char in text if char in consonants)

def min_max_finder(num):
    """Find the minimum and maximum numbers from a list."""
    if not num:
        raise ValueError("No numbers provided.")
    return min(num), max(num)

def is_palindrome(text):
    """Check if a string is a palindrome."""
    cleanedtext = ''.join(char.lower() for char in text if char.isalnum())
    return cleanedtext == cleanedtext[::-1]

# Word counter
import requests

def word(text_file_url):
    response = requests.get(text_file_url)
    text = response.text.lower()
    wlist = ['the', 'was', 'and']
    word= {word: text.count(word) for word in wlist}
    return word

def main():
    while True:
        print("\nMenu:")
        print("1. Prime number sum calculator")
        print("2. Length unit converter")
        print("3. Consonant counter")
        print("4. Min-Max number finder")
        print("5. Palindrome checker")
        print("6. Word counter")
        print("7. Exit")
        
        choice = input("Select a function (1-7): ")
        
        if choice == '1':
            start = int(input("Enter start of range: "))
            end = int(input("Enter end of range: "))
            result = prime_sum(start, end)
            print(f"Sum of prime numbers between {start} and {end}: {result}")
        
        elif choice == '2':
            value = float(input("Enter the length value: "))
            direction = input("Enter conversion direction (M/F): ")
            result = length_converter(value, direction)
            print(f"Converted length: {result}")
        
        elif choice == '3':
            text = input("Enter a text string: ")
            result = consonant_count(text)
            print(f"Number of consonants: {result}")
        
        elif choice == '4':
            numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
            min_num, max_num = min_max_finder(numbers)
            print(f"Smallest: {min_num}, Largest: {max_num}")
        
        elif choice == '5':
            text = input("Enter a text string: ")
            result = is_palindrome(text)
            print(f"Is palindrome: {result}")
        
        elif choice == '6':
            file_url = input("Enter the URL of the text file: ").strip()
            try:
                result = word(file_url)
                print(f"Word counts: {result}")
            except requests.exceptions.RequestException as e:
                print(f"Error fetching the file: {e}")


        
        elif choice == '7':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice.")
        choice = input("do you want to continue with functions (yes/no) : ")
        if choice != 'yes':
            print("EXITING")
            break
        
# Start the game with the main menu


if __name__ == "__main__":
    main()