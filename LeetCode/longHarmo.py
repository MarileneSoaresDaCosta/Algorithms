
"""
tried this... gave an error when [1, 2] >> output zero, when it should be 2

class Solution(object):
    def findLHS(self, nums):

        # :type nums: List[int]
        # :rtype: int

        
        if nums == []:
            return 0
        nums.sort()
        if max(nums) - min(nums) == 0:
            return 0
        maxi = 0
        for i in range(len(nums)-2):
          count = 1
          j = i + 1
          while nums[j] == nums[i] or nums[j] == nums[i]+1:
            count += 1
            if j == len(nums)-1: break
            else: j += 1
          i += 1
          if count > maxi:
            maxi = count
    
        return maxi

# n = Solution()
# print n.findLHS(a)
# b = [1, 2, 3, 4]
# x = Solution()
# print x.findLHS(b)

"""
import collections
a = [3, 3, 2, 1, 2, 2, 7, 5]

def findLHS(nums):
  count = collections.Counter(nums)
  print count 
  return max([count[x] + count[x+1] for x in count if count[x+1]] or [0])


print findLHS(a)

"""
another version
def findLHS(self, A):
    count = collections.Counter(A)
    ans = 0
    for x in count:
        if x+1 in count:
            ans = max(ans, count[x] + count[x+1])
    return ans

"""

