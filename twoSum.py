#  using hashmap 

class Solution():
     def twosum(self, nums: list[int], target: int) -> list[int]:
        prevMap = {} # val : index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]   # we return a new list with two elements diff and i so it will look like [n, n]
            prevMap[n] = i
        return []

target = 4;
ar = [3,0,1,2]

sol = Solution()

result = sol.twosum(ar, target)
print(result)
