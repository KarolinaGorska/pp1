import random
def generate_number():
    n = random.randint(1,9)
    return n


if __name__ == "__main__":
    print(generate_number())