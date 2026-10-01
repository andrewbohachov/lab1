def fibonacci_number(n):
    if n <= 0:
        return "Число має бути більше нуля"
    elif n == 1 or n == 2:
        return 1

    a, b = 1, 1
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b

try:
    num = int(input("Введіть порядковий номер n: "))
    result = fibonacci_number(num)
    print(f"Результат F({num}) = {result}")
except ValueError:
    print("Введіть ціле число.")
