from itertools import combinations

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = [[]]
        for i in range(1, len(nums)+1):
            for j in combinations(nums, i):
                answer.append(list(j))

        return answer