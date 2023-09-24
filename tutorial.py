# def insertion_sort(arr):
#     for j in range(1, len(arr)):
#         key = arr[j]
#         i = j - 1
#         while i >= 0 and arr[i] > key:
#             arr[i + 1] = arr[i]
#             i -= 1
#         arr[i + 1] = key
#
# # Example usage:
# my_list = [12, 11, 13, 5, 6]
# insertion_sort(my_list)
# print("Sorted array:", my_list)

def reverse_insertion_sort(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] < key:
            arr[i + 1] = arr[i]
            i -= 1
            arr[i + 1] = key

my_list = [12, 11, 13, 5, 6]
reverse_insertion_sort(my_list)
print("new array :", my_list)