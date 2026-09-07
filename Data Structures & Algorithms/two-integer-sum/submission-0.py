class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res =[]
        hash ={}
        i = 0
        for num in nums :
            if target-num in hash :
                res.append(hash[target-num])
                res.append(i)

            else :
                hash[num] = i
                i = i + 1
        return res