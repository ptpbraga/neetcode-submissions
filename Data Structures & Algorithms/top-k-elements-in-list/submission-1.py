from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = defaultdict(int)
        for i in nums:
            h[i]+=1
        
        b = [[] for _ in range(len(nums)+1)]

        for chave, valor in h.items():
            b[valor].append(chave)

        results = []
        for i in range(len(nums), 0, -1):
            for val in b[i]:
                results.append(val)
                if len(results)==k: 
                    return results