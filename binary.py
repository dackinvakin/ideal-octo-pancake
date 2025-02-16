def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

arr = sorted(map(int, input("Введите отсортированный массив через пробел: ").split()))
target = int(input("Введите число для поиска: "))

index = binary_search(arr, target)
if index != -1:
    print(f"Число {target} найдено в массиве на позиции {index}.")
else:
    print(f"Число {target} не найдено в массиве.")