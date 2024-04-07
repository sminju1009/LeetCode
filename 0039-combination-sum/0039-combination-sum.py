class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(csum, idx, path):
            if csum<0:
                return
            if csum==0:
                ret.append(path[:])
                return

            for i in range(idx, len(candidates)):
                dfs(csum-candidates[i], i, path+[candidates[i]])

        ret = []
        dfs(target, 0, [])
        return ret