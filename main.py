def bubble_sort(arr, reverse=False):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if reverse:
                # Для сортировки по убыванию
                if arr[j] < arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
            else:
                # Для сортировки по возрастанию
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]


def main():
    print("Введите числа через пробел:")
    numbers = list(map(float, input().split()))

    print("Выберите направление сортировки:")
    print("1 - по возрастанию")
    print("2 - по убыванию")

    choice = input("Ваш выбор (1 или 2): ")

    if choice == "1":
        bubble_sort(numbers, reverse=False)
        print("Отсортированный список по возрастанию:")
    elif choice == "2":
        bubble_sort(numbers, reverse=True)
        print("Отсортированный список по убыванию:")
    else:
        print("Неверный выбор! Сортировка по возрастанию.")
        bubble_sort(numbers, reverse=False)
        print("Отсортированный список по возрастанию:")

    print(numbers)


if __name__ == "__main__":
    main()