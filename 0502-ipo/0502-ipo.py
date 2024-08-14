class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        pc = list(zip(capital, profits))
        pc.sort()

        q = []
        idx = 0

        for i in range(k):
            while idx<n and pc[idx][0] <= w:
                heappush(q, -pc[idx][1])
                idx += 1

            if len(q)==0:
                break

            w += -heappop(q)

        return w