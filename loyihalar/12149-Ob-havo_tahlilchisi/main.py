def add_temperature(temperatures, command):
    """Haroratni ro'yxatga qo'shadi."""
    parts = command.split()

    if len(parts) != 2:
        return

    try:
        temperature = int(parts[1])
    except ValueError:
        print("Xato: son kiriting")
        return

    temperatures.append(temperature)
    print(f"Qabul: {temperature}")

    if temperature > 35:
        print("Ogohlantirish: jazirama!")
    elif temperature < 0:
        print("Ogohlantirish: ayoz!")


def show_statistics(temperatures):
    """Statistikani chiqaradi."""
    if not temperatures:
        return

    minimum = min(temperatures)
    maximum = max(temperatures)
    average = sum(temperatures) / len(temperatures)

    print(f"Min: {minimum} | Maks: {maximum} | O'rtacha: {average:.1f}")


def show_trend(temperatures):
    """Trendni chiqaradi."""
    if len(temperatures) < 3:
        print("Trend: barqaror")
        return

    first = temperatures[-3]
    second = temperatures[-2]
    third = temperatures[-1]

    if first < second < third:
        print("Trend: ko'tarilmoqda")
    elif first > second > third:
        print("Trend: pasaymoqda")
    else:
        print("Trend: barqaror")


def show_report(temperatures):
    """Yakuniy hisobotni chiqaradi."""
    print("=== OB-HAVO HISOBOTI ===")

    count = len(temperatures)
    print(f"Kunlar: {count}")

    if count == 0:
        print("Min: 0 | Maks: 0 | O'rtacha: 0.0")
        print("Issiq kunlar: 0")
        print("Sovuq kunlar: 0")
        return

    minimum = min(temperatures)
    maximum = max(temperatures)
    average = sum(temperatures) / count

    hot_days = 0
    cold_days = 0

    for temperature in temperatures:
        if temperature > 35:
            hot_days += 1
        if temperature < 0:
            cold_days += 1

    print(f"Min: {minimum} | Maks: {maximum} | O'rtacha: {average:.1f}")
    print(f"Issiq kunlar: {hot_days}")
    print(f"Sovuq kunlar: {cold_days}")


def main():
    """Asosiy dastur."""
    temperatures = []

    while True:
        try:
            command = input().strip()
        except (EOFError, OSError):
            break

        if not command:
            continue

        if command == "exit":
            break

        if command.startswith("add "):
            add_temperature(temperatures, command)

        elif command == "stat":
            show_statistics(temperatures)

        elif command == "trend":
            show_trend(temperatures)

        elif command == "report":
            show_report(temperatures)


if __name__ == "__main__":
    main()