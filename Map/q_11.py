from array import array


def array_sum(num_arr):
    sum_n = 0
    for n in num_arr:
        sum_n += n
    return sum_n


nums = array('i', [1, 2, 3, 4, 5, -13])
print(array_sum(list(map(int, nums))))

lst = [1, 2, 3, 4, 5, -13]

print(sum(map(int, lst)))
