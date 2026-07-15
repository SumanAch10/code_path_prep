#  Maximum Average Subarray I (Easy)
# You are given an integer array nums of length n and an integer k. Find the contiguous subarray of length exactly k that has the maximum average value, and return that average. Answers within 10⁻⁵ of the true value are accepted.
# Example 1:
# Input:  nums = [1, 12, -5, -6, 50, 3], k = 4
# Output: 12.75
# Explanation: The window [12, -5, -6, 50] sums to 51, average 51/4 = 12.75

# Example 2:
# Input:  nums = [5], k = 1
# Output: 5.0
# Constraints: 1 <= k <= n <= 10^5, -10^4 <= nums[i] <= 10^4

class Solution:
    def max_sum(self,arr,k)->int:
        l = 0
        r = k 
        window_sum = sum(arr[l:r])
        max_sum = window_sum
        
        while(l<len(arr)-k):
            window_sum += arr[r]
            window_sum-=arr[l]
            
            l += 1
            r += 1
            
            max_sum = max(window_sum,max_sum)
    
        return max_sum / k
    

s1 = Solution()

result = s1.max_sum(arr= [1, 12, -5, -6, 50, 3],k = 4)
print(result)