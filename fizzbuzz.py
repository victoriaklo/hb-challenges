def fizzbuzz():
    """Count from 1 to 20 in fizzbuzz fashion."""

    for num in range(1,20):
        if num % 5 == 0 and num % 3 == 0:
            print("fizzbuzz")
        elif num % 3 == 0:
            print("fizz")
        elif num % 5 == 0:
            print("buzz")
        else:
            print(num)

