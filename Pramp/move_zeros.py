def move_zeros(arr):
    i = 0
    zero_index = 0

    while i < len(arr):
        if arr[i] != 0:
            i += 1
            zero_index += 1
        else:
            while i < len(arr) and arr[i] == 0:
                i += 1

            if i < len(arr):
                arr[zero_index], arr[i] = arr[i], arr[zero_index]
                zero_index += 1


a = [2, 0, 7, 0, 6, 0, 8, 9]
move_zeros(a)
print(a)