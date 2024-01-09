class Pair:
    @staticmethod
    def twoSum(nums, target):
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return lookup[target - num], i
            lookup[num] = i


print("index1 = %d\nindex2 = %d" % Pair().twoSum((10, 20, 10, 40, 50, 60, 70), 50))
