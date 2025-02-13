# Problem: Majority Element II (Optional) - https://leetcode.com/problems/majority-element-ii/

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        hash_={}

        answer=[]
        n=math.floor(len(nums)/3)
        for num in nums:
            if num in hash_:
                hash_[num]+=1
            else:
                hash_[num]=1

        for key in hash_:
            if hash_[key]>n:
                answer.append(key)

        return answer

    

        