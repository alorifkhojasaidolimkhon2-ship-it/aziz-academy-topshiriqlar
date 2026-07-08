def calculate(expression):
    """Matematik ifodani hisoblaydi."""
    parts = expression.split()

    if len(parts) != 3:
        return

    try:
        first_number = int(parts[0])
        operator = parts[1]
        second_number = int(parts[2])
    except ValueError:
        return

    if operator == "+":
        print(first_number + second_number)

    elif operator == "-":
        print(first_number - second_number)

    elif operator == "*":
        print(first_number * second_number)

    elif operator == "/":
        if second_number == 0:
            print("Nolga bo'lish mumkin emas")
        else:
            print(first_number / second_number)


def main():
    """Asosiy dastur."""
    while True:
        try:
            expression = input().strip()
        except (EOFError, OSError):
            break

        if not expression:
            continue

        if expression == "exit":
            break

        calculate(expression)


if __name__ == "__main__":
    main()