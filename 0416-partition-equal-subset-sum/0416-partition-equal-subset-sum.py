class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # 1. 배열의 합이 짝수여야 하기 때문에 홀수면 false
        if sum(nums)%2!=0:
            return False
        # 배열의 합이 짝수인 경우
        else:
            target = sum(nums)//2
            # 한 값이 target과 같은 경우
            for i in range(len(nums)):
                if nums[i]==target:
                    return True
            # target과 같은 값이 없는 경우
            dp = [0] * 10001
            dp[0] = 1
        
            for num in nums:
                idx = target
                while idx-num >= 0 :
                    if dp[idx] or dp[idx-num]:
                        dp[idx] = 1
                    idx -= 1

                if dp[target]: return True