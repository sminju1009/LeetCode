class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # 버블 정렬 이용
        for i in range(len(nums)-1, 0, -1):
            for j in range(i):
                if nums[j]>nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]

        return nums