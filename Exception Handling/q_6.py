def test_index(lst, index):
    try:
        print(lst[index])
    except IndexError:
        print("Error: Index out of range.")


nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
test_index(nums, 2)
test_index(nums, 6)
test_index(nums, 10)
