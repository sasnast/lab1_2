def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def main():
    print("Введите числа через пробел:")
    numbers = list(map(float, input().split()))

    bubble_sort(numbers)

    print("Отсортированный список:")
    print(numbers)


if __name__ == "__main__":
    main()