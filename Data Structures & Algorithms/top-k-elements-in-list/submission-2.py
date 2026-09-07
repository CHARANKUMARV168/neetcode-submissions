class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        i = 1
        res = []
        for num in nums :
            if num in hash.keys() and num not in res:
                hash[num] = hash[num]+1
            else :
                hash[num] = 1


        sor = dict(sorted(hash.items(), key=lambda x: x[1],reverse=True))

 
        for num in sor.keys():
            if len(res) == k:
                break
            res.append(num)


        return res

