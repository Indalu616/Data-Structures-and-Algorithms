# Problem: Majority Element II - https://leetcode.com/problems/majority-element-ii/?envType=daily-question&envId=2023-10-05

class Solution(object):
    def majorityElement(self, nums):
       

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