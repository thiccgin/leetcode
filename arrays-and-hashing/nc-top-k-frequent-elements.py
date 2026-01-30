class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq = {}

        for n in nums:
            if n not in freq:
                freq[n] = 1
            else:
                freq[n] += 1
        
        arr = []
        for num, count in freq.items():
            arr.append([count, num])
        arr.sort()

        while len(res) < k:
            res.append(arr.pop()[1])

        return res