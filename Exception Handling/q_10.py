def test_list_operation():
    try:
        print("Length of the list:", len(nums))
    except AttributeError:
        print("Error: The list does not have a 'length' attribute.")


nums = [1, 2, 3, 4, 5]
test_list_operation()
