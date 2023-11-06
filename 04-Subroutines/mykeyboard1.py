def read_number():
    while True:
        try:
            user_input = int(input("Enter a number: "))
            return user_input
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def main():
    n1 = read_number()
    n2 = read_number()
    return n1, n2

if __name__ == "__main__":
    num1, num2 = main()
    print(f"{num1} + {num2} = {num1 + num2}")