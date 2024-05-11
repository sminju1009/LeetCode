class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        visited = [0] * (n+1)
        visited[0] = 1

        for i in range(1, n+1):
            for w in wordDict:
                if i - len(w) >= 0 and visited[i-len(w)]==1 and s[i-len(w):i]==w:
                    visited[i] = 1

        if visited[-1]==1:
            return True
        else:
            return False