def celsius(input1):
    return float((input1 * (9/5) + 32))


def fahrenheit(input2):
    return float((input2 - 32) * (5/9))


if __name__ == "__main__":
    print("Temperature converter")

    farenheit = float(input("Enter celsius\n"))
    print("Celsius to Fahrenheit")
    print(celsius(farenheit))

    celsius = float(input("Enter fahrenheit\n"))
    print("Fahrenheit  to Celsius")
    print(fahrenheit(celsius))

