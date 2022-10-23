# UP-SOLVE
# Weighted Median O(NlogN) with Explanations
# https://leetcode.com/problems/minimum-cost-to-make-array-equal/solutions/2734183/python3-weighted-median-o-nlogn-with-explanations/

class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        arr = sorted(zip(nums, cost))
        total, cnt = sum(cost), 0
        for num, c in arr:
            cnt += c
            if cnt > total // 2:
                target = num
                break
        return sum(c * abs(num - target) for num, c in arr)