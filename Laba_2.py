def fibbonachi(n):
    if n < 0:
        raise ValueError("n должно быть неотрицательным")

    if n == 0:
        return []

    if n == 1:
        return [0]

    numbers = [0, 1]

    for i in range(2, n):
        numbers.append(numbers[-1] + numbers[-2])

    return numbers


def bubble_sort(numbers):
    for i in range(len(numbers)):
        swapped = False

        for j in range(0, len(numbers)-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                swapped = True

        if not swapped:
            break

    return numbers


def calculator(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        return a / b
    else:
        raise ValueError("такой оператор пока не поддерживается")

