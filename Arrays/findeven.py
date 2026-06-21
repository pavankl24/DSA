class Even:
    def find(self, nums):
        count = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                count += 1
        return count

obj = Even()
nums = [12, 345, 2, 6, 7896]

print(obj.find(nums))