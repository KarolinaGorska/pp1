def f(detector):
    count = 0  # Initialize the count of people in the room.
    max_count = 0  # Initialize the maximum count of people.

    for event in detector:
        if event == '+':
            count += 1
        elif event == '-':
            count -= 1

        # Update the maximum count of people if necessary.
        if count > max_count:
            max_count = count

    return max_count >= 3


print(f("+-+++-+---"))
print(f("+-+-+-+-"))
print(f("+-++-+--"))
print(f("+-++-++-+---"))